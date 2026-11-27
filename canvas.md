# Canvas — PreClassCoach · Track A

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | Track A — EdTech, hướng A1 Trợ lý học tập. Lát cắt: từ log pre-class của chính học viên, chọn tối đa 3 điểm kiến thức cần ôn nhất và soạn lộ trình ôn 15 phút trước buổi học. |
| 2 | Người dùng chính | Học viên AI20K có học pre-class trên preclass-online.com, tối trước buổi học muốn ôn đúng phần mình hổng thay vì học lại từ đầu. Phía nhận chuyển ca: lab coach. |
| 3 | Pain một câu | Khi ôn pre-class trước buổi học, học viên có những câu sai lần đầu nhưng hiếm khi làm lại chính câu đó trên hệ thống, nên nhóm chọn hỗ trợ chỉ ra phần cần ôn từ log. |
| 4 | Bằng chứng đầu · CP2 | **424/2.478** lượt trả lời lần đầu có chấm bị sai (17,1%). Chỉ **2/424** lượt sai có lần làm lại được chấm (0,5%). Ví dụ Day02, mục `select_rule_workflow_agent_level` có lần đầu sai và không ghi nhận lần làm lại có chấm cho cùng học viên và câu hỏi. [Ví dụ từ log BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/answers.csv#L61). Cách đếm và các ví dụ khác ở [hồ sơ bằng chứng](evidence/summary.md). |
| 5 | Lát cắt MỘT CÂU | Với học viên hỏi nên ôn gì trong 15 phút, hệ thống chọn tối đa ba điểm từ log theo quy tắc và model soạn hoạt động ôn cho từng điểm đã chọn, hoặc hệ thống báo thiếu dữ liệu khi log chưa đủ. |
| 6 | AI tự làm đến đâu + lý do | AI tự lên lộ trình ôn khi có log; không có log thì báo chưa đủ dữ liệu, không bịa. Lý do: nêu sai một điểm "hổng" không có trong log làm học viên ôn lệch và mất niềm tin; báo thiếu dữ liệu chỉ tốn một câu hỏi. Log chỉ đổi khi lab coach kiểm chứng — hệ thống không tự sửa log, không xem log người khác, không làm hộ bài. |
| 7 | Phân công có tên | Bình (đội trưởng) — dữ liệu, bằng chứng và checkpoint · Đạt — bản chạy thử và video · Nam — đánh giá và chi phí · Mai — chấm độc lập và slide. Danh sách và vai trò ở [TEAMS.md](TEAMS.md). |
| — | (CP2) Đã đổi gì so với CP1 | Bổ sung số đo và ví dụ từ log pre-class, mô tả rõ phần code chọn điểm và phần model soạn hoạt động ôn. Bộ câu thử hiện có 24 câu, gồm 17 câu từ dữ liệu thật. Dữ liệu chạy thử gồm 17 hồ sơ đã tổng hợp. |
