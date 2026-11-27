"""Đếm bằng chứng pain từ data/preclass (BTC cấp, đã ẩn danh).
Cách đếm (viết trước khi đếm, guide 1.2):
- Học viên có hoạt động = hv xuất hiện trong events.csv.
- Mục đã hoàn thành: completed_items.csv, item_code theo lesson_id (program-dayNN:...).
- Trả lời lần đầu có chấm: answers.csv, lan_thu=1 và was_correct True/False.
- Làm lại = cùng hv + cùng ref có lan_thu>=2.
Giờ trong file là UTC; ở đây chỉ đếm theo program-day trong lesson_id nên không cần đổi giờ.
Chạy: python3 analyze_preclass.py <thư mục data/preclass>
"""
import sys, pandas as pd

d = sys.argv[1] if len(sys.argv) > 1 else '.'
learners = pd.read_csv(f'{d}/learners.csv')
events = pd.read_csv(f'{d}/events.csv', usecols=['hv', 'lesson_id'])
comp = pd.read_csv(f'{d}/completed_items.csv')
ans = pd.read_csv(f'{d}/answers.csv')
chat = pd.read_csv(f'{d}/chat.csv')

active = events['hv'].nunique()
print(f'Tai khoan: {len(learners)} | co hoat dong: {active}')

events['day'] = events['lesson_id'].str.extract(r'(program-day\d+)')[0]
byday = events.dropna(subset=['day']).groupby('day')['hv'].nunique().sort_index()
print('Hoc vien hoat dong theo ngay:'); print(byday.to_string())

per_student = comp.groupby('hv').size()
print(f'Hoan thanh >=1 muc: {comp["hv"].nunique()}/{active} ({comp["hv"].nunique()/active:.0%})'
      f' | trung vi {per_student.median():.0f} muc/nguoi | <=3 muc: {(per_student<=3).sum()} nguoi')

g = ans[ans['was_correct'].notna() & (ans['was_correct'] != '')].copy()
g['wc'] = g['was_correct'].astype(str).str.lower()
first = g[g['lan_thu'] == 1]
wrong = first[first['wc'] == 'false']
retried_keys = set(map(tuple, g[g['lan_thu'] >= 2][['hv', 'ref']].values.tolist()))
retried = wrong[['hv', 'ref']].apply(tuple, axis=1).isin(retried_keys).sum()
print(f'Lan dau co cham: {len(first)} | sai lan dau: {len(wrong)} ({len(wrong)/len(first):.1%})'
      f' | trong do lam lai: {retried} ({retried/len(wrong):.1%})')
print(f'Hoc vien tung sai lan dau: {wrong["hv"].nunique()} | tung nhan AI: {chat["hv"].nunique()}/{active} ({chat["hv"].nunique()/active:.0%})')
