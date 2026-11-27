"""Trang web demo nhỏ cho PreClassCoach — chỉ để trình diễn, phần được chấm vẫn là run.py.

Chạy:  python web_demo.py            (mở http://localhost:8000)
Trang web gọi đúng codebase/agent.py answer() và data/progress.json như bản dòng lệnh.
Chỉ dùng thư viện chuẩn. Không nối hệ thống thật nào.
"""
import json
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "codebase"))
from agent import answer  # noqa: E402

PAGE = """<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PreClassCoach — demo</title>
<style>
body{font-family:system-ui,Arial,sans-serif;background:#0f172a;color:#e2e8f0;margin:0}
.wrap{max-width:760px;margin:0 auto;padding:24px 16px 48px}
h1{font-size:22px;margin:8px 0 4px}.sub{color:#94a3b8;font-size:14px;margin-bottom:16px}
#log{display:flex;flex-direction:column;gap:10px;margin-bottom:14px}
.msg{padding:10px 14px;border-radius:12px;white-space:pre-wrap;line-height:1.5;font-size:15px}
.u{background:#1d4ed8;align-self:flex-end;max-width:85%}
.a{background:#1e293b;border:1px solid #334155;align-self:flex-start;max-width:92%}
form{display:flex;gap:8px}input{flex:1;padding:12px;border-radius:10px;border:1px solid #334155;background:#020617;color:#e2e8f0;font-size:15px}
button{padding:12px 18px;border:0;border-radius:10px;background:#2563eb;color:#fff;font-size:15px;cursor:pointer}
.hint{color:#64748b;font-size:13px;margin-top:10px}
</style></head><body><div class="wrap">
<h1>PreClassCoach</h1>
<div class="sub">Ôn đúng phần bạn hổng trong 15 phút — từ log pre-class của chính bạn (data BTC đã ẩn danh, 17 học viên mẫu).</div>
<div id="log"></div>
<form id="f"><input id="q" placeholder="VD: Mình là học viên L0526. Trước buổi học tiếp theo mình nên ôn gì?" autocomplete="off">
<button>Gửi</button></form>
<div class="hint">Thử thêm: L0001 (chưa có hoạt động) · xin xem log của bạn khác · nhờ làm hộ bài lab — hệ thống sẽ xử lý theo quy tắc.</div>
</div><script>
const log=document.getElementById('log'),f=document.getElementById('f'),q=document.getElementById('q');
function add(t,c){const d=document.createElement('div');d.className='msg '+c;d.textContent=t;log.appendChild(d);window.scrollTo(0,document.body.scrollHeight)}
f.onsubmit=async e=>{e.preventDefault();const text=q.value.trim();if(!text)return;add(text,'u');q.value='';
 const r=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({text})});
 const j=await r.json();add(j.output,'a')};
</script></body></html>"""


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/ask":
            self.send_response(404); self.end_headers(); return
        n = int(self.headers.get("Content-Length", 0))
        payload = json.loads(self.rfile.read(n).decode("utf-8") or "{}")
        out = answer(payload.get("text", ""), session_id="web")
        if isinstance(out, dict):
            out = out.get("output", "")
        body = json.dumps({"output": out}, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    print("PreClassCoach demo: http://localhost:%d" % port)
    HTTPServer(("127.0.0.1", port), H).serve_forever()
