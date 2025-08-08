from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

# ======== 你的配置 =========
TELEGRAM_TOKEN = "7924949987:AAENogVoFXJfyi9p3WivYV4yhX9Zw2WT5wQ" 
CHAT_ID = "5366773464"
# ==========================

@app.route("/", methods=["GET"])
def home():
    return "✅ TradingView → Telegram Webhook 已运行"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # 从 TradingView 获取字段
    symbol = data.get("symbol", "未知品种")
    price = data.get("price", "未知价格")
    note = data.get("note", "")

    # 时间戳（北京时间）
    now = datetime.utcnow().timestamp() + 8 * 3600
    time_str = datetime.fromtimestamp(now).strftime("%Y-%m-%d %H:%M:%S")

    # 格式化推送消息
    message = f"""
🔔 TradingView 预警触发
——————————————
📅 时间: {time_str}
📈 品种: {symbol}
💰 价格: {price}
📝 备注: {note}
"""

    # 发送到 Telegram
    url = f"https://api.telegram.org/bot7924949987:AAENogVoFXJfyi9p3WivYV4yhX9Zw2WT5wQ}/sendMessage"
    payload = {
        "chat_id": 5366773464,
        "text": message.strip()
    }
    requests.post(url, data=payload)

    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
