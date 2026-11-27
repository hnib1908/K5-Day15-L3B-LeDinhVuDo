# Kế hoạch phỏng vấn + dùng thử — PreClassCoach

Mục tiêu: **≥3 người ngoài nhóm, ≥5 trích dẫn nguyên văn (bỏ tên)** trước **CP3 10:00 Thứ Bảy 28/11**.
File này chỉ là khung hỏi — trích dẫn chỉ điền sau khi phỏng vấn thật, không bịa.

## 1. Phỏng vấn (10–15 phút/người, mỗi thành viên hỏi 1 người)

Tin nhắn hẹn: *"Chào bạn, nhóm mình đang tìm hiểu cách mọi người học pre-class trong khoá. Bạn cho mình hỏi 10–15 phút về lần gần nhất bạn học pre-class được không? Không giới thiệu sản phẩm gì cả."*

5 câu hỏi (chỉ hỏi việc đã xảy ra, không hỏi "bạn có thích tính năng này không"):

1. Lần gần nhất bạn mở trang pre-class là khi nào, trước buổi học nào? Bạn làm được tới đâu thì dừng?
2. Lần đó có câu nào bạn trả lời sai ngay lần đầu không? Sau đó bạn làm gì — làm lại, tra lại bài, hay bỏ qua?
3. Trước buổi học, bạn quyết định ôn phần nào bằng cách nào? Có lần nào bạn ôn lệch phần mình đang hổng không?
4. Tháng qua, có lần nào bạn bỏ luôn không học pre-class nữa không? Lần đó vì sao?
5. Khi không biết mình đang hổng ở đâu, bạn thường làm gì tiếp theo (hỏi bạn, hỏi AI, đoán, bỏ qua)?

Ghi chép: chép `TEMPLATE.md` thành `P1.md`, `P2.md`, `P3.md` trong `evidence/interviews/`
— mỗi người một file, ghi nguyên văn 1–2 câu/trích dẫn vào mục "Trích nguyên văn".
Sau đó cộng dồn ≥5 câu vào `evidence/summary.md` mục "Nguồn 2" và 2 câu vào
`slides/outline.md` trang 1.

Lịch gợi ý: 1–2 người trong giờ nghỉ chiều nay (trước CP2 19:30), người còn lại
sáng mai 8:00–9:30, chừa 30 phút điền file trước 10:00.

## 2. Dùng thử thật (bonus CP4, 2–3 người ngoài nhóm, ~10 phút/người)

Chạy `python run.py` (hoặc `python web_demo.py` → http://localhost:8000), giao 3 việc:

1. "Bạn là học viên L0010, hỏi xem nên ôn gì trong 15 phút" — quan sát: họ có hiểu
   lộ trình 3 điểm không, có hỏi lại chỗ nào không.
2. "Bạn là L0001 (chưa có hoạt động nào), hỏi tương tự" — quan sát phản ứng khi
   hệ thống báo chưa đủ dữ liệu thay vì bịa điểm ôn.
3. "Thử xem log của bạn khác / nhờ làm hộ bài" — quan sát phản ứng khi bị từ chối.

Ghi vào `validation/log.md` (theo bảng có sẵn): việc giao, quan sát đầu tiên,
chỗ do dự/hiểu sai, trích nguyên văn, mức nghiêm trọng. Hỏi cuối:
*"Nếu mai không được dùng nữa, bạn thấy: rất tiếc / hơi tiếc / không sao?"*
Toàn lời khen = phiên chưa đạt, giao việc khó hơn.
