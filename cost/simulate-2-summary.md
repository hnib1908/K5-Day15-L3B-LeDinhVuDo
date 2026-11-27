# Tóm tắt mô phỏng simulate-2@20261128-003411

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| on_truoc_buoi | 20 | 1 | 155 | 175 | 0.7 | 0.9 |
| on_ky_hon | 19 | 2 | 336 | 377 | 1.5 | 2.0 |
| hoi_them | 11 | 3 | 509 | 542 | 2.3 | 2.8 |

Tỉ lệ đạt dùng để tính: 24/24 (100%) — lượt run-2@20261127-043723

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (200 người) | Chi phí / tháng — cơ sở (436 người) | Chi phí / tháng — cao (700 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.5-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00057 (≈ 15 ₫) | $0.00057 (≈ 15 ₫) | $0.00032 (≈ 8 ₫) | $1.31 (≈ 34.090 ₫) | $2.86 (≈ 74.316 ₫) | $4.59 (≈ 119.315 ₫) | $0.0066 (≈ 170 ₫) |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00057 (≈ 15 ₫) | $0.00057 (≈ 15 ₫) | $0.00032 (≈ 8 ₫) | $1.31 (≈ 34.090 ₫) | $2.86 (≈ 74.316 ₫) | $4.59 (≈ 119.315 ₫) | $0.0066 (≈ 170 ₫) |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.8) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.5-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
- Tỷ giá: 1 USD = 26.010 ₫ (Vietcombank ban ra 26.010 VND/USD ngay 27/11/2026 (mua CK 25.630). Dung gia ban ra de quy doi chi phi; kiem lai khi nop CP4).
