"""Nối model — chỗ DUY NHẤT gọi model AI. Hợp đồng: xem docs/connect-model.md.

Provider hỗ trợ qua .env: fake (mặc định) · gemini · openai · anthropic · ollama.
Chỉ dùng thư viện chuẩn (urllib). Token lấy từ usage của API, không ước lượng.
Không dán API key vào file này — key nằm trong .env (đã .gitignore).
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()


def post_json(url, headers, body, timeout=60):
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))


def call_openai(system, user):
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json("https://api.openai.com/v1/chat/completions",
                     {"Authorization": "Bearer " + API_KEY},
                     {"model": MODEL_NAME, "messages": messages})
    u = data["usage"]
    return {"text": data["choices"][0]["message"]["content"],
            "tokens_in": u["prompt_tokens"], "tokens_out": u["completion_tokens"]}


def call_claude(system, user):
    data = post_json("https://api.anthropic.com/v1/messages",
                     {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
                     {"model": MODEL_NAME, "max_tokens": 1024, "system": system or "",
                      "messages": [{"role": "user", "content": user}]})
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    u = data["usage"]
    return {"text": text, "tokens_in": u["input_tokens"], "tokens_out": u["output_tokens"]}


def call_gemini(system, user):
    if MODEL_PROVIDER == "vertex":
        # Vertex AI Express: endpoint aiplatform, key qua query ?key= (dang nhom dang dung).
        url = "https://aiplatform.googleapis.com/v1/publishers/google/models/%s:generateContent?key=%s" % (MODEL_NAME, API_KEY)
        headers = {}
    else:
        # AI Studio: key cu dang "AIza" va key moi dang "AQ." deu goi endpoint generativelanguage.
        # Gui key qua header x-goog-api-key (hop le cho ca hai dang; key "AQ." bi tu choi neu dua vao ?key=).
        url = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % MODEL_NAME
        headers = {"x-goog-api-key": API_KEY}
    body = {"contents": [{"role": "user", "parts": [{"text": user}]}]}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    data = post_json(url, headers, body)
    parts = data["candidates"][0]["content"]["parts"]
    text = "".join(p.get("text", "") for p in parts)
    u = data.get("usageMetadata", {})
    return {"text": text,
            "tokens_in": u.get("promptTokenCount", 0), "tokens_out": u.get("candidatesTokenCount", 0)}


def call_ollama(system, user):
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    data = post_json("http://localhost:11434/api/chat", {},
                     {"model": MODEL_NAME, "messages": messages, "stream": False}, timeout=300)
    return {"text": data["message"]["content"],
            "tokens_in": data.get("prompt_eval_count", 0), "tokens_out": data.get("eval_count", 0)}


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}
    if MODEL_PROVIDER == "openai":
        r = call_openai(system, user)
    elif MODEL_PROVIDER in ("anthropic", "claude"):
        r = call_claude(system, user)
    elif MODEL_PROVIDER in ("gemini", "vertex"):
        r = call_gemini(system, user)
    elif MODEL_PROVIDER == "ollama":
        r = call_ollama(system, user)
    else:
        raise NotImplementedError("MODEL_PROVIDER=%s chưa hỗ trợ — dùng gemini/openai/anthropic/ollama" % MODEL_PROVIDER)
    return {"text": r["text"], "model": MODEL_NAME,
            "tokens_in": int(r["tokens_in"]), "tokens_out": int(r["tokens_out"])}
