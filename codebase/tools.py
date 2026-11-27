"""Công cụ của PreClassCoach — chỉ đọc data/progress.json (tổng hợp từ data preclass BTC).

get_student_progress(ma_hv): log tổng hợp của đúng học viên đó (KC sai lần đầu,
mục chưa xong, điểm ưu tiên do CODE tính theo quy tắc spec §4) hoặc None.
flag_for_mentor(ma_hv, ly_do): tạo ca nhờ lab coach kiểm chứng — chỉ tạo ca,
không tự sửa log, không gửi gì ra ngoài.
"""
import json
import os

from tracing import tool

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "progress.json")
with open(DATA, encoding="utf-8") as f:
    PROGRESS = json.load(f)

_flags = []


@tool
def get_student_progress(ma_hv):
    rec = PROGRESS.get((ma_hv or "").strip().upper())
    return rec


@tool
def flag_for_mentor(ma_hv, ly_do):
    case = {"case_id": "FLAG-%03d" % (len(_flags) + 1), "ma_hoc_vien": ma_hv, "ly_do": ly_do,
            "trang_thai": "cho lab coach kiem chung"}
    _flags.append(case)
    return case
