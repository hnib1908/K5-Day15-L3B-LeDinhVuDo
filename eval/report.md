# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Số lấy từ `python run.py score` sau khi điền cột `pass`. Chấm theo từng pass_criterion; phần kiểm tự động (đối chiếu mã KC/mục với data/progress.json) + đọc tay các câu từ chối.
> Ghi chú xuất xứ: hai lượt đầu được thực hiện ngày 27/11/2026 trên bản sao kiểm thử cùng code và dữ liệu, dùng `gemini-3.5-flash-lite` với key Gemini cá nhân của một thành viên. Lượt xác nhận bằng key Vertex của nhóm được ghi ở mục 5.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | run-1@20261127-042010 | 24/24 | 100% | 4/4 | 15/15 | 5/5 | đạt |
| 2 | run-2@20261127-043723 | 24/24 | 100% | 4/4 | 15/15 | 5/5 | đạt |

Token trung bình / câu: lượt 1 — vào 124, ra 177 · lượt 2 — vào 77, ra 81.
Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

Không có câu trượt ở lượt 1. Hai điểm yếu quan sát được (không làm trượt nhưng tốn kém / thiếu ổn định):

| Nhóm | Số câu | Câu | Mô tả |
|---|---|---|---|
| Output dài hơn cần thiết | 15 câu có lộ trình | B01-B14, B21 | model diễn đạt trung bình 177 token ra/câu; lộ trình 15 phút cần ngắn để học viên đọc nhanh |
| Model không trả lời, phải dùng bản code lắp | 1 | B10 | lượt gọi model không cho token (0/0) — cổng dự phòng của code tự lắp lộ trình đúng, câu vẫn đạt; cho thấy bản code lắp phải luôn sẵn sàng |

## 3. Một cải tiến đã làm (trước lượt 2)
Thêm vào prompt diễn đạt: "mỗi điểm tối đa 60 từ" (codebase/agent.py, hàm _llm_plan). Không đổi quy tắc chọn điểm, không đổi chuẩn "đạt", không sửa câu thử.

## 4. Kết quả lượt 2 + còn lại
- Lượt 2: 24/24 (100%), token ra trung bình giảm 177 → 81 (-54%), token vào 124 → 77.
- Còn lại: (a) chưa có người dùng thật dùng thử — làm ở validation/ trước CP4; (b) dataset mới 17 học viên mẫu — mở rộng ra toàn bộ học viên có hoạt động khi dùng thật; (c) câu hỏi gợi mở vẫn theo mẫu chung cho từng KC, chưa cá nhân hóa theo nội dung bài học (data BTC không cấp nội dung câu trả lời).

## 5. Lượt xác nhận CP3 bằng Vertex của nhóm

- Run ID `run-3@20261127-234732`. Nhóm chạy `python run.py eval --wait 6` trên cùng bộ 24 câu, dùng `gemini-3.5-flash-lite` qua Vertex với key nhóm và prompt tại thời điểm chạy.
- Ngày 28/11/2026, đội trưởng Bình xác nhận kết quả chấm đối chiếu của Codex đạt **24/24 (100%)** theo tiêu chí CP2, gồm 4/4 câu thường, 15/15 câu khó và 5/5 câu từ chối. Có 15 câu ghi nhận token từ Vertex và 9 câu được xử lý bằng quy tắc cục bộ. Lượt chạy có 0 lỗi kỹ thuật.
- B11 nêu đúng ba mục cần ôn nhưng diễn giải cụm “hóa đơn ticket” thành bài toán giá vé. Đây là điểm cần cải thiện trong cách model viết gợi ý ôn.
- [Kết quả từng câu](run-3.csv) · [Trace](../traces/run-3.jsonl).
