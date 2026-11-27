# Đào data — cách đếm và kết quả (data/preclass BTC cấp)

## 1. Cách đếm — viết TRƯỚC khi chạy
- Data dùng: bộ `data/preclass` (events.csv, answers.csv, completed_items.csv, chat.csv, learners.csv), 05/11-25/11/2026, Day01-Day13. Chỉ đọc README + từ điển cột trước khi đếm.
- Định nghĩa: học viên có hoạt động = mã hv xuất hiện trong events.csv (mẫu số 436, không phải 721 tài khoản). Trả lời lần đầu có chấm = answers.csv, lan_thu=1, was_correct True/False. Làm lại = cùng hv + cùng ref có lan_thu>=2. Mục hoàn thành theo completed_items.csv.
- Script: `evidence/count_preclass.py` (chạy: `python3 evidence/count_preclass.py <thư mục data/preclass>`) — chạy lại phải ra đúng số dưới đây.
- Repo chỉ chứa số tổng hợp này; không chép nguyên file data BTC.

## 2. Kết quả (chạy 27/11/2026)

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| Học viên có hoạt động / tổng tài khoản | 436 / 721 | 60% | 285 tài khoản không có hoạt động nào |
| Học viên còn hoạt động Day01 → Day12 | 417 → 26 | còn 6% | Day13: 50 người; giảm đều theo ngày |
| Hoàn thành >=1 mục học / có hoạt động | 192 / 436 | 44% | trung vị 6 mục/người; 76 người xong <=3 mục |
| Sai ở lần trả lời đầu / lượt lần đầu có chấm | 424 / 2.478 | 17,1% | bài pre/post sai 20,3% |
| Lượt sai lần đầu được làm lại (cùng câu) | 2 / 424 | 0,5% | gần như không ai quay lại sửa |
| Học viên từng nhắn hỏi AI / có hoạt động | 145 / 436 | 33% | |

## 3. Kết luận cho lát cắt
Pain không phải "thiếu nội dung" mà là "không ai chỉ lại phần hổng": sai lần đầu xong là bỏ, mục học bỏ dở, rồi bỏ luôn pre-class. Lát cắt chọn: biến chính log đó thành lộ trình ôn 15 phút cá nhân, mọi điểm nêu ra đều tra được về log.
