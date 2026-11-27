# Canvas — PreClassCoach · Track A

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | Track A — EdTech, hướng A1 Trợ lý học tập. Lát cắt: từ log pre-class của chính học viên, chọn tối đa 3 điểm kiến thức cần ôn nhất và soạn lộ trình ôn 15 phút trước buổi học. |
| 2 | Người dùng chính | Học viên AI20K có học pre-class trên preclass-online.com, tối trước buổi học muốn ôn đúng phần mình hổng thay vì học lại từ đầu. Phía nhận chuyển ca: lab coach. |
| 3 | Pain một câu | Học viên — đang học pre-class trước buổi học — trả lời sai lần đầu ở một số điểm kiến thức và bỏ dở nhiều mục học, mà không có gì chỉ lại cho họ phần hổng — nên vào buổi học thật với lỗ hổng cũ và dần bỏ pre-class. |
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm | Giả thuyết: học viên sai lần đầu thì gần như không quay lại sửa, và phần lớn không hoàn thành các mục pre-class. Nguồn kiểm chính: đào data preclass BTC cấp (05/11-25/11/2026) — cách đếm ghi trước ở evidence/data-mining.md, script evidence/count_preclass.py. Kiểm lại bằng phỏng vấn >=3 học viên ngoài nhóm (lấy >=5 trích dẫn nguyên văn, bỏ tên). Số đầu tiên điền ở CP2. |
| 5 | Lát cắt MỘT CÂU | Một học viên · hỏi "mình nên ôn gì trong 15 phút" · AI quyết định chọn tối đa 3 điểm ôn từ log của chính học viên đó (KC sai lần đầu trước, mục chưa xong sau), hoặc báo chưa đủ dữ liệu khi học viên chưa có hoạt động · học viên nhận lộ trình ôn đúng phần mình hổng, mọi điểm nêu ra đều tra được về log. |
| 6 | AI tự làm đến đâu + lý do | AI tự lên lộ trình ôn khi có log; không có log thì báo chưa đủ dữ liệu, không bịa. Lý do: nêu sai một điểm "hổng" không có trong log làm học viên ôn lệch và mất niềm tin; báo thiếu dữ liệu chỉ tốn một câu hỏi. Log chỉ đổi khi lab coach kiểm chứng — hệ thống không tự sửa log, không xem log người khác, không làm hộ bài. |
| 7 | Phân công có tên | Thành viên 2 (L3B) — bằng chứng pain (đào data preclass) + bộ câu thử. [ĐIỀN các thành viên còn lại + MSSV + phần việc; đội trưởng ở dòng 1 TEAMS.md] |
| — | (CP2) Đã đổi gì so với CP1 | Đổi hướng từ A2 (trợ lý Discord, bằng chứng phải tự thu) sang A1 theo data preclass BTC cấp — quyết định TRƯỚC khi nộp CP1 nên CP1 nộp thẳng bản này. Benchmark chốt 24 câu (17/24 từ data thật), chuẩn "đạt" chốt ở spec §7, dataset runtime là tổng hợp 17 học viên mẫu từ data thật. |
