"""PreClassCoach — workflow cố định (spec §4).

Nguyên tắc: điểm ôn do CODE chọn từ log (công cụ), model chỉ diễn đạt.
Mọi mã KC/mục trong câu trả lời phải nằm trong danh sách ưu tiên của công cụ —
kiểm lại sau khi model trả (cổng trích dẫn), sai thì dùng bản code tự lắp.
Hệ thống không xem log của học viên khác, không làm hộ bài, không nhận log
do người dùng dán, không tự sửa log.
"""
import re

import ai
from tools import flag_for_mentor, get_student_progress
from tracing import note

HV_RE = re.compile(r"\bL\d{4}\b")


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


def _assembled_plan(rec):
    prio = rec["uu_tien_on"]
    lines = ["Dựa trên log pre-class của bạn (%s): đã hoàn thành %d mục, hoạt động %d ngày học."
             % (rec["ma_hoc_vien"], rec["so_muc_da_xong"], len(rec["ngay_hoat_dong"])),
             "Lộ trình ôn 15 phút — 3 điểm ưu tiên nhất từ log của chính bạn:"]
    for i, p in enumerate(prio, 1):
        if p["loai"] == "kc_sai_lan_dau":
            lines.append("%d. %s — điểm kiến thức bạn trả lời sai ở lần đầu (%s). "
                         "Việc ôn (~5 phút): mở lại phần này và tự trả lời: vì sao đáp án lần trước chưa đúng, điểm này dùng khi nào?"
                         % (i, p["ma"], p["ngay"]))
        else:
            lines.append("%d. %s — mục học bạn chưa hoàn thành (%s). "
                         "Việc ôn (~5 phút): mở mục này và học/xong phần còn thiếu."
                         % (i, p["ma"], p["ngay"]))
    lines.append("Mọi điểm ở trên đều lấy từ log của bạn; hệ thống không thêm điểm nào ngoài log.")
    return "\n".join(lines)


def _llm_plan(rec):
    prio = rec["uu_tien_on"]
    facts = "\n".join("- %s (%s, %s)" % (p["ma"], p["loai"], p["ngay"]) for p in prio)
    system = ("Bạn là trợ lý ôn tập pre-class. Chỉ được dùng đúng các điểm kiến thức/mục học "
              "trong danh sách được cấp, ghi nguyên mã của chúng. Mỗi điểm kèm 1 câu hỏi gợi mở "
              "hoặc 1 việc ôn cụ thể, mỗi điểm tối đa 60 từ, tổng ~15 phút. Không bịa điểm nào khác, không làm hộ bài tập.")
    user = ("Học viên %s đã hoàn thành %d mục. Danh sách điểm ưu tiên ôn (do hệ thống chọn từ log):\n%s\n"
            "Hãy viết lộ trình ôn 15 phút ngắn gọn bằng tiếng Việt, giữ nguyên các mã trên."
            % (rec["ma_hoc_vien"], rec["so_muc_da_xong"], facts))
    try:
        out = ai.call_model(system, user)["text"]
    except Exception:
        return _assembled_plan(rec)
    codes = [p["ma"] for p in prio]
    universe = {x["ma"] for x in rec["kc_sai_lan_dau"]} | {x["ma"] for x in rec["muc_chua_xong"]}
    mentioned = set(re.findall(r"[a-z][a-z0-9]+(?:_[a-z0-9]+){1,}", out)) | set(HV_RE.findall(out))
    extra = {m for m in mentioned if m in universe and m not in codes}
    if extra or any(c not in out for c in codes):
        return _assembled_plan(rec)
    return out


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
