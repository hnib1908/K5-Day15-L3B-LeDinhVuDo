# Tổng kết bằng chứng — PreClassCoach

Với vai trò đội trưởng, tôi phụ trách tổng hợp bằng chứng cho lát cắt ôn pre-class. Nhóm chúng tôi dùng log hành vi để đo số lần trả lời sai và số lần quay lại làm chính câu đó.

## Nguồn 1 · Log pre-class của BTC

Bộ log ghi hoạt động từ **05/11 đến 25/11/2026**. Nhóm đếm những lượt lần đầu có kết quả đúng hoặc sai. Một lượt sai được tính là có làm lại khi cùng học viên và cùng câu hỏi có lượt thứ hai trở lên được chấm trong bộ log. Cách lọc và tính nằm ở [báo cáo đào dữ liệu](data-mining.md) và [script đếm](count_preclass.py). [Mô tả dữ liệu BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/README.md)

- **424/2.478 lượt lần đầu có chấm bị sai (17,1%)**.
- **2/424 lượt sai lần đầu có lần làm lại được chấm (0,5%)**.
- **192/436 học viên có hoạt động được ghi nhận hoàn thành ít nhất một mục (44,0%)**.

### Năm ví dụ từ log đã ẩn danh

Bảng giữ mã điểm kiến thức, ngày học và trạng thái chấm. Từ “làm lại” ở đây chỉ lượt làm lại có chấm trong kỳ quan sát.

| Ngày học | Mã điểm kiến thức | Điều ghi nhận trong log | Nguồn BTC |
|---|---|---|---|
| Day01 | `chatbot_is_app_around_model` | Sai lần đầu. Chưa ghi nhận lượt làm lại. | [answers.csv, dòng 3](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/answers.csv#L3) |
| Day02 | `select_rule_workflow_agent_level` | Sai lần đầu. Chưa ghi nhận lượt làm lại. | [answers.csv, dòng 61](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/answers.csv#L61) |
| Day03 | `agent_architecture_components` | Sai lần đầu. Chưa ghi nhận lượt làm lại. | [answers.csv, dòng 676](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/answers.csv#L676) |
| Day04 | `system_prompt_antipatterns` | Cùng học viên và câu hỏi, lần đầu sai và lần hai đúng. | [Lần đầu](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/answers.csv#L331) · [Lần hai](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/answers.csv#L372) |
| Day13 | `bounded_retry_cost` | Sai lần đầu ở câu hỏi dưới video. Chưa ghi nhận lượt làm lại. | [answers.csv, dòng 3756](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass/answers.csv#L3756) |

**Kết luận của nhóm.** Log ủng hộ giả thuyết rằng rất ít lượt sai lần đầu được làm lại và hơn nửa số học viên có hoạt động chưa có mục hoàn thành được ghi nhận trong giai đoạn này. Nhóm chọn dùng log để gợi ý điểm cần ôn trước buổi học. Lý do học viên ít làm lại và số phút có thể tiết kiệm vẫn cần kiểm chứng với học viên.

## Nguồn 2 · Phỏng vấn dự kiến

Repo hiện có [kế hoạch phỏng vấn](interviews/ke-hoach-phong-van.md). Nhóm dự kiến hỏi ít nhất ba học viên ngoài nhóm về lần gần nhất họ trả lời sai hoặc bỏ dở pre-class và cách họ chọn phần để ôn. Kết quả sẽ được ghi theo số người và trích lời đã ẩn danh sau khi có ghi chép thực tế.
