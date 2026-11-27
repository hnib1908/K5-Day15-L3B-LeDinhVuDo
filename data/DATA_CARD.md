# Data card — dữ liệu bản chạy thử dùng

## Dataset 1 · Log pre-class tổng hợp theo học viên — `data/progress.json`

| | |
|---|---|
| Dùng để làm gì | nguồn cho công cụ `get_student_progress` · nền cho bộ câu thử |
| Từ đâu | chưng cất từ bộ `data/preclass` BTC cấp (log hành vi preclass-online.com 05/11-25/11/2026, đã ẩn danh sẵn: mã học viên dạng Lxxxx, không tên/email) — KHÔNG commit nguyên file BTC vào repo nhóm, chỉ giữ tổng hợp của 17 học viên mẫu phục vụ benchmark/demo |
| Xử lý những bước gì | script `~/build_dataset.py` của nhóm (mô tả ở evidence/data-mining.md): KC sai lần đầu = answers.csv với lan_thu=1 và was_correct=False; mục chưa xong = item_code thuộc các buổi học viên đã hoạt động trừ đi completed_items của học viên đó; điểm ưu tiên do code tính theo quy tắc spec §4 (KC sai lần đầu trước — ngày gần nhất trước — rồi mục chưa xong, tối đa 3) |
| Số dòng / số đoạn | 17 học viên mẫu: 10 có KC sai lần đầu, 4 có hoạt động nhưng không sai lần đầu, 3 chưa có hoạt động nào |
| Phiên bản / ngày lấy | v1 · 27/11/2026 |
| Nhãn | data_that_da_tong_hop (dữ liệu thật đã ẩn danh, chỉ giữ tổng hợp) |
| Giới hạn | bản thật sẽ gồm mọi học viên; ở bản chạy thử chỉ 17 học viên mẫu có trong benchmark. Data không chứa nội dung câu trả lời của học viên (BTC chỉ cấp độ dài), nên hệ thống chỉ nêu mã điểm kiến thức, không trích bài làm của ai. |

## Dataset 2 · Bộ câu thử — `eval/benchmark.csv`
24 câu ngay từ CP2 (4 thuong · 15 kho · 5 tu_choi, gồm 2 câu tấn công: dán log giả, ra lệnh bỏ qua log). 17/24 câu source `data_that` (lấy từ dòng thật của preclass, mã đã ẩn danh), 7 câu `tu_viet`. Không sửa expected của câu cũ sau CP2.

## Dataset 3 · Bằng chứng pain (không dùng để chạy thử)
Đào data preclass (số tổng hợp + script đếm trong `evidence/`) + ghi chép phỏng vấn >=3 học viên ngoài nhóm (chỉ giữ trích dẫn bỏ tên).
