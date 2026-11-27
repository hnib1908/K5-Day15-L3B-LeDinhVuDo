# Chi phí khi dùng thật — PreClassCoach

## 1. Đầu vào
- **Persona** (`cost/personas.yaml`): 3 kiểu — on_truoc_buoi (50%, 8 phiên/người/tháng, 1 lượt/phiên), on_ky_hon (30%, 12 phiên, 2 lượt), hoi_them (20%, 16 phiên, 3 lượt). Số lần dùng là *(tự ước tính)* theo nhịp 13 ngày học trong data; kiểm lại bằng phỏng vấn trước CP4.
- **Số người dùng thật**: thấp 200 · cơ sở 436 · cao 700. Nguồn: data/preclass BTC — 436 học viên có hoạt động / 721 tài khoản; cao 700 là *(tự ước tính)* nếu mở cả khóa.
- **Giá**: gemini-3.5-flash-lite và gemini-3.1-flash-lite — vào $0.25, ra $1.50 / 1M token (https://ai.google.dev/gemini-api/docs/pricing, xem 27/11/2026 — kiểm lại khi nộp CP4).
- **Tỉ lệ đạt** dùng để tính: 24/24 (100%) — lượt run-1@20261127-042010.
- Token đo trên model gemini-3.5-flash-lite; tính giá cho cả hai model trên (giá bằng nhau nên kết quả bằng nhau).
- Lượt mô phỏng chạy trên bản sao kiểm thử cùng code/data bằng key cá nhân của thành viên (xem eval/report.md); nhóm chạy lại bằng key nhóm trước CP4.

## 2. Kết quả mô phỏng
Lượt mô phỏng: `cost/simulate-1.csv` · simulate-1@20261127-043548 · 50 phiên · seed 42 · phiên lỗi 0/50. Token/phiên trung bình theo persona: 87/119 (vào/ra) · 236/353 · 249/341.

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| gemini-3.5-flash-lite | $0.00043 | $0.00043 | $0.95 | $2.07 | $3.33 | $0.0048 |
| gemini-3.1-flash-lite | $0.00043 | $0.00043 | $0.95 | $2.07 | $3.33 | $0.0048 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt (100% ở run-1).

## 3. So với impact
- Impact / người / tháng (spec §2): ~15 phút ôn đúng trọng tâm mỗi lần dùng thay vì học lại từ đầu — ở kịch bản cơ sở, 436 người x ~10 phiên x 15 phút ≈ 65.400 phút/tháng *(tự ước tính)*, đổi lấy $2.07/tháng chi phí model.
- Kết luận chi phí: chi phí model không phải rào cản; rào cản thật là độ phủ dữ liệu (mới 17 học viên mẫu) và việc học viên có quay lại ôn hay không — đo ở validation.
