"""PreClassCoach — workflow cố định (spec §4).

Nguyên tắc: điểm ôn do CODE chọn từ log (công cụ), model chỉ diễn đạt.
Mọi mã KC/mục trong câu trả lời phải nằm trong danh sách ưu tiên của công cụ —
kiểm lại sau khi model trả (cổng trích dẫn), sai thì dùng bản code tự lắp.
Hệ thống không xem log của học viên khác, không làm hộ bài, không nhận log
do người dùng dán, không tự sửa log.
"""
import json
import re
from pathlib import Path

import ai
from tools import flag_for_mentor, get_student_progress
from tracing import note

HV_RE = re.compile(r"\bL\d{4}\b")
# The log is the source for days and codes. The labels describe them for learners.
with (Path(__file__).resolve().parents[1] / "data" / "lesson_labels.json").open(encoding="utf-8") as label_file:
    LESSON_LABELS = json.load(label_file)


def _norm(s):
    return (s or "").lower()


def _self_hv(text):
    m = re.search(r"(?:mình là|em là|tôi là|học viên)\s*(L\d{4})", text)
    if m:
        return m.group(1)
    codes = HV_RE.findall(text)
    return codes[0] if codes else None


def _other_hv(text, self_hv):
    for c in HV_RE.findall(text):
        if c != self_hv:
            return c
    return None


def _assembled_plan(rec, suggestions=None):
    prio = rec["uu_tien_on"]
    suggestions = suggestions or {}
    lines = ["Dựa trên log pre-class của bạn (%s): đã hoàn thành %d mục, hoạt động %d ngày học."
             % (rec["ma_hoc_vien"], rec["so_muc_da_xong"], len(rec["ngay_hoat_dong"])),
             "Lộ trình ôn 15 phút từ log của bạn:"]
    for i, p in enumerate(prio, 1):
        code = p["ma"]
        day = p["ngay"].replace("program-day", "Day ", 1)
        topic = LESSON_LABELS["days"].get(p["ngay"])
        lesson = f"{day} — {topic}" if topic else day
        if p["loai"] == "kc_sai_lan_dau":
            label = LESSON_LABELS["knowledge"].get(code, code.replace("_", " ").capitalize())
            reason = "Bạn trả lời sai điểm này ở lần đầu."
            default = "Xem lại câu hỏi và tự giải thích vì sao đáp án lần trước chưa đúng."
        else:
            slug = code.rsplit(":", 1)[-1]
            label = LESSON_LABELS["items"].get(slug, slug.replace("-", " ").capitalize())
            reason = "Log ghi mục này chưa hoàn thành."
            default = f"Mở {label} trên Preclass Online, đọc yêu cầu và làm tiếp phần còn thiếu."
        advice = suggestions.get(code, default)
        lines.extend([
            "",
            f"{i}. {lesson}",
            f"   Mục cần ôn (~5 phút): {label}",
            f"   Lý do: {reason}",
            f"   Việc ôn: {advice}",
            f"   Mã đối chiếu: {code}",
        ])
    return "\n".join(lines)


def _llm_plan(rec):
    prio = rec["uu_tien_on"]
    knowledge_labels = LESSON_LABELS["knowledge"]
    # A lesson title alone is not enough to infer the contents of an unfinished item.
    knowledge = {
        p["ma"]: knowledge_labels[p["ma"]]
        for p in prio
        if p["loai"] == "kc_sai_lan_dau" and p["ma"] in knowledge_labels
    }
    if not knowledge:
        return _assembled_plan(rec)

    facts = "\n".join(f"- {code}: {label}" for code, label in knowledge.items())
    system = ("Bạn là trợ lý ôn tập pre-class. Trả một đối tượng JSON. Mỗi khóa là nguyên mã "
              "được cấp, mỗi giá trị là một câu hỏi gợi mở hoặc một việc ôn cụ thể bằng tiếng Việt, "
              "tối đa 60 từ. Dùng đúng tất cả các mã được cấp làm khóa. Trong phần gợi ý, "
              "không lặp lại mã, không đoán tên bài, ngày học hay đường dẫn. Không bịa điểm khác, "
              "không làm hộ bài tập.")
    user = "Viết gợi ý ôn cho các điểm ưu tiên sau, theo đúng định dạng JSON:\n%s" % facts
    try:
        raw = ai.call_model(system, user)["text"].strip()
    except Exception:
        return _assembled_plan(rec)

    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", raw, re.DOTALL | re.IGNORECASE)
    try:
        suggestions = json.loads(fenced.group(1) if fenced else raw)
    except json.JSONDecodeError:
        return _assembled_plan(rec)

    if not isinstance(suggestions, dict) or suggestions.keys() != knowledge.keys():
        return _assembled_plan(rec)
    universe = {x["ma"] for x in rec["kc_sai_lan_dau"]} | {x["ma"] for x in rec["muc_chua_xong"]}
    other_codes = universe - knowledge.keys()
    for code, suggestion in suggestions.items():
        if not isinstance(suggestion, str) or not suggestion.strip():
            return _assembled_plan(rec)
        if any(other in suggestion for other in other_codes):
            return _assembled_plan(rec)
        suggestions[code] = " ".join(suggestion.split())
    return _assembled_plan(rec, suggestions)


def answer(text, session_id="app"):
    t = _norm(text)
    self_hv = _self_hv(text)
    other = _other_hv(text, self_hv)

    if other and re.search(r"bạn|ban|của|coi|xem|tra", t):
        note("guard/tool")
        return ("Mình không tra cứu được dữ liệu học tập của học viên khác (%s) — mỗi người chỉ xem được log của chính mình. "
                "Bạn gửi mã của chính bạn, mình lên lộ trình ôn từ log của bạn." % other)

    if re.search(r"làm giúp|làm hộ|làm luôn|giải hộ|viết sẵn code|viết code.*nộp|làm bài.*giúp", t):
        note("guard/tool")
        return ("Mình không làm hộ bài lab hay bài nộp. Mình giúp được phần ôn: từ log của chính bạn, "
                "mình chỉ ra điểm kiến thức đang hổng và câu hỏi gợi mở để bạn tự làm được bài.")

    if re.search(r"điểm danh|hạn nộp|deadline|phòng học|lich hoc|lịch học", t):
        note("guard/tool")
        return ("Phần điểm danh / hạn nộp / lịch phòng nằm ngoài phạm vi của mình — mình chỉ hỗ trợ ôn tập từ log pre-class. "
                "Bạn xem kênh thông báo chính thức của khóa hoặc hỏi TA cho các thông tin đó.")

    if not self_hv:
        note("guard/tool")
        return ("Cho mình mã học viên của bạn (dạng Lxxxx, ví dụ L0526) để mình tra đúng log pre-class của bạn. "
                "Mình không đoán và không lấy log của người khác.")

    rec = get_student_progress(self_hv)

    if re.search(r"bỏ qua log|khen mình|giỏi hết|đừng nhắc", t):
        note("guard/tool")
        head = ("Mình không bỏ qua log và không nói khác sự thật học tập của bạn — phần hổng còn trong log thì mình vẫn nêu để bạn ôn kịp. ")
        return head + (_assembled_plan(rec) if rec and rec["co_hoat_dong"] else
                       "Hiện log chưa ghi hoạt động nào của bạn nên mình chưa nêu được điểm ôn cụ thể.")

    if rec is None or not rec["co_hoat_dong"]:
        note("guard/tool")
        return ("Chưa đủ dữ liệu: log pre-class chưa ghi hoạt động nào của học viên %s nên mình không nêu điểm ôn cụ thể nào "
                "(nêu ra là bịa). Bạn bắt đầu từ bài đầu tiên của ngày học gần nhất, hoặc hỏi lab coach để được hướng dẫn trực tiếp." % self_hv)

    note("guard/tool")

    if re.search(r"log.*sai|kiểm tra lại|kiem tra lai|học hết rồi mà", t):
        case = flag_for_mentor(self_hv, "hoc vien bao log khong dung, can kiem chung")
        note("guard/tool")
        return ("Mình không tự sửa log theo lời kể — log chỉ đổi khi lab coach kiểm chứng (mình đã tạo ca %s). "
                "Trong lúc chờ, đây là tình hình log đang ghi:\n%s" % (case["case_id"], _assembled_plan(rec)))

    if not rec["uu_tien_on"]:
        return ("Theo log, bạn đã hoàn thành các mục đã mở và không có điểm nào sai ở lần đầu — chưa có điểm ôn ưu tiên. "
                "Cứ học tiếp bài của ngày tiếp theo.")

    if ai.MODEL_PROVIDER == "fake":
        return _assembled_plan(rec)
    return _llm_plan(rec)
