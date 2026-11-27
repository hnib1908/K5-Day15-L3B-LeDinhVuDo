# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Định dạng nào cũng được (PDF, PPTX, HTML…); hoặc nộp link slide (Drive, Canva, Google Slides…) ở form CP4, để ai có link cũng xem được.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau và số liệu từ log | `evidence/summary.md`, `evidence/data-mining.md` | Có số liệu · chờ trích dẫn từ Bình |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ☑ |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ☑ |
| 4 | Demo live | B07 và B15 · video dự phòng ở chế độ cục bộ | `eval/benchmark.csv`, `eval/run-2.csv` | Có bản dự phòng cục bộ · chờ video/link của Đạt |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · hai lượt chạy · đối chiếu 5 output | `eval/report.md`, `eval/cham-doc-lap.md` | Có số liệu · chờ kết quả người chấm độc lập |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ☑ |
| 7 | Kết luận | Thử cùng học viên rồi quyết định mở rộng | `evidence/data-mining.md`, `eval/report.md`, `cost/simulate-1-summary.md` | ☑ |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ☑ |

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần):

| Trang | Người nói |
|---|---|
| Bìa · 1 Người dùng & pain · 2 Vì sao chọn | Vũ Văn Bình |
| 3 Giải pháp · 4 Demo live | Lê Tuấn Đạt |
| 5 Đánh giá · 6 Chi phí | Đinh Hoài Nam |
| 7 Kết luận · 8 Nếu có thêm 1 tuần | Đỗ Thanh Mai |

Nguồn slide: `slides/demo-slides.html` → xuất `demo-slides.pdf` (lệnh ở đầu file HTML).

---

# Nội dung từng trang (chép vào Canva / Google Slides — mọi số có nguồn ở cột phải của bảng trên)

**Trang 1 — Người dùng & pain**
Học viên AI20K học pre-class trước buổi học — và không biết mình hổng ở đâu.
- Sai lần đầu: 424/2.478 lượt (17,1%) — chỉ 2/424 lượt (0,5%) được làm lại (data preclass BTC, evidence/data-mining.md)
- Chỉ 192/436 học viên có hoạt động (44%) hoàn thành >=1 mục học
- Người còn hoạt động: Day01 417 → Day12 26
- Chờ Bình bổ sung ≥2 trích dẫn nguyên văn đã ẩn danh từ phỏng vấn vào `evidence/summary.md` để đưa lên slide.

**Trang 2 — Vì sao chọn bài này**
Impact: 436 học viên có hoạt động x ~8 lần/tháng x 15 phút ôn lệch ≈ 52.000 phút/tháng (thừa số thời gian tự ước tính, spec §2).
Đã loại: tutor trả lời học thuật dưới video (không đo kịp chất lượng, data không cấp nội dung bài) — lát cắt này đo được bằng đối chiếu log.

**Trang 3 — Giải pháp**
Một học viên · hỏi "ôn gì trong 15 phút" · hệ thống chọn tối đa 3 điểm từ log của chính học viên (KC sai lần đầu → mục chưa xong), không có log thì báo chưa đủ dữ liệu.
Điểm ôn do CODE chọn, model chỉ diễn đạt; cổng kiểm lại mọi mã trong câu trả lời phải nằm trong log. Không xem log người khác, không làm hộ bài, không tự sửa log.

**Trang 4 — Demo live**
Ca thường: L0010 hỏi ôn gì → lộ trình 3 điểm (2 KC sai lần đầu + 1 mục chưa xong).
Ca khó: L0001 chưa có hoạt động → "chưa đủ dữ liệu". Dự phòng ngay trên máy: `demo-preclasscoach.mp4` ở gốc repo, dựng từ lần chạy cục bộ của `python run.py` cho B07 và B15. Chờ video hoặc link công khai của Đạt. Có thể chạy web demo bằng `python web_demo.py`.

**Trang 5 — Đánh giá thế nào**
Benchmark 24 câu (4 thường · 15 khó · 5 từ chối), 17/24 câu từ data thật của BTC.
Chuẩn "đạt": >=80% tổng, 100% câu khó + từ chối không bịa điểm ngoài log, 100% từ chối đúng quy tắc.
Lượt 1 run-1@20261127-042010: 24/24 (100%) → cải tiến prompt (<=60 từ/điểm) → Lượt 2 run-2@20261127-043723: 24/24 (100%), token ra 177 → 81.
Codex đối chiếu từ phiếu che nhãn: 5/5 khớp cột `pass`, đạt ngưỡng 4/5. Xem bản nháp gửi Nam trong `eval/cham-doc-lap.md`. Chờ Bình xác nhận người viết metric và Mai hoặc người do Bình chỉ định hoàn tất lượt chấm độc lập.

**Trang 6 — Chi phí khi dùng thật**
Mô phỏng 50 phiên (simulate-1, tỷ lệ đạt từ run-1): chi phí model $0.00043/task thành công. Ba kịch bản: 200 người → $0.95/tháng, 436 → $2.07/tháng, 700 → $3.33/tháng (gemini-3.5-flash-lite). Dự toán dùng tần suất theo `cost/personas.yaml`. Ước tính tác động trang 2 dùng giả định 8 lần/người/tháng từ `spec.md` §2.

**Trang 7 — Kết luận**
GO có điều kiện: số đo đạt chuẩn ở cả 2 lượt, chi phí không đáng kể; điều kiện là kiểm chứng với người dùng thật (validation) và mở rộng dataset từ 17 học viên mẫu ra toàn bộ học viên có hoạt động.

**Trang 8 — Nếu có thêm 1 tuần**
1. Nối dữ liệu trực tiếp từ trang pre-class thay vì file chưng cất; mở rộng đủ 436 học viên.
2. Câu hỏi gợi mở theo nội dung từng KC (cần data nội dung bài học).
3. Đo tiếp vòng 2 của pain: học viên được gợi ý ôn có quay lại làm lại câu sai không (đúng metric hành vi 2/424 hiện tại).
