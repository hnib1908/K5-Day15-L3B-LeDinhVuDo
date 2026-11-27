# Khai báo dùng AI

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Muse (trợ lý lập trình) | Dựng codebase/agent.py, tools.py, web_demo.py theo spec nhóm chốt | Chạy run.py check/eval, đọc lại từng guard; mọi output đều qua cổng đối chiếu log | Thành viên 2 |
| Prompt / thiết kế lời gọi mô hình | Muse | Soạn prompt diễn đạt + giới hạn 60 từ/điểm ở lượt cải tiến | Kiểm bằng 2 lượt eval thật 24/24 | Thành viên 2 |
| Đào data (viết script đếm, gợi ý nhãn) | Muse | Viết evidence/count_preclass.py + build_dataset.py chưng cất progress.json | Chạy lại script ra đúng số đã ghi; đối chiếu tay các tổng 424/2.478, 192/436, 417→26 | Thành viên 2 |
| Rà câu hỏi phỏng vấn / khảo sát | — | Chưa dùng (nhóm tự phỏng vấn, ghi ở evidence/) | — | [thành viên phụ trách evidence] |
| Viết câu thử (benchmark) | Script của nhóm + Muse | 17 câu data_that sinh bằng script từ dòng thật của preclass (mã đã ẩn danh); 7 câu tu_viet do Muse soạn theo kịch bản spec §5 | Đọc lại từng pass_criterion; không sửa expected sau CP2 | Thành viên 2 |
| Sinh data synthetic (nếu có) | — | Không có data synthetic — dataset runtime là tổng hợp từ data thật của BTC | — | — |
| Chấm cột pass bằng LLM (nếu có) | Không dùng LLM chấm | Chấm bằng kiểm đối chiếu mã KC/mục với progress.json + đọc tay câu từ chối | Đọc lại toàn bộ 24 output của run-1/run-2 | Thành viên 2 |
| Slide, văn bản | Muse | Soạn nháp canvas/spec/slide từ số liệu thật của nhóm | Nhóm đọc lại, chịu trách nhiệm nội dung khi nộp | Cả nhóm |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
