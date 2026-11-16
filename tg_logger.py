import os, time, threading, requests
from datetime import datetime, timezone

TOKEN = os.getenv("8502713384:AAEUJkJ1sfjqajpkQdMoFpKneLoBolno1oY")
CHAT_ID = os.getenv("-1004368342495")
START = time.time()
_counter = {"n": 0}

def _send(text):
    if not TOKEN or not CHAT_ID:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"},
            timeout=10,
        )
    except Exception as e:
        print("TG send error:", e)

def log_health(ip, ua, ms, status):
    _counter["n"] += 1
    up = int(time.time() - START)
    h, m = up // 3600, (up % 3600) // 60
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    text = (
        f"✅ <b>/health ping #{_counter['n']}</b>\n"
        f"🕒 {now}\n"
        f"📡 IP: <code>{ip}</code>\n"
        f"🤖 UA: <code>{ua[:80]}</code>\n"
        f"⚡ Javob: {ms:.0f} ms | Status: {status}\n"
        f"⏱ Uptime: {h} soat {m} daq"
    )
    threading.Thread(target=_send, args=(text,), daemon=True).start()
