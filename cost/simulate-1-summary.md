# Tóm tắt mô phỏng simulate-1@20261127-043548

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| on_truoc_buoi | 20 | 1 | 87 | 119 | 0.7 | 0.9 |
| on_ky_hon | 19 | 2 | 236 | 353 | 1.5 | 2.0 |
| hoi_them | 11 | 3 | 249 | 341 | 2.3 | 2.8 |

Tỉ lệ đạt dùng để tính: 24/24 (100%) — lượt run-1@20261127-042010

- Tự chọn: lượt run-N mới nhất đã chấm xong, chạy bằng đúng model đang đo (run-1.csv). Muốn dùng lượt khác (vd lượt 2): thêm `--rate-from eval/run-2.csv`.

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (200 người) | Chi phí / tháng — cơ sở (436 người) | Chi phí / tháng — cao (700 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00043 | $0.00043 | $0.00024 | $0.9511 | $2.07 | $3.33 | $0.0048 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00043 | $0.00043 | $0.00024 | $0.9511 | $2.07 | $3.33 | $0.0048 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.5-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
