from flask import Flask, request
import requests
from datetime import datetime

app = Flask(__name__)

TELEGRAM_TOKEN = "7924949987:AAENogVoFXJfyi9p3WivYV4yhX9Zw2WT5wQ"
CHAT_ID = "-1002506581103"

@app.route("/", methods=["GET"])
def home():
    return "✅ TradingView → Telegram Webhook 已运行"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    symbol = data.get("symbol", "未知品种")
    price = data.get("price", "未知价格")
    note = data.get("note", "") 

    now = datetime.utcnow().timestamp() + 8 * 3600
    time_str = datetime.fromtimestamp(now).strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
🔔 TradingView 预警触发
——————————————
📅 时间: {time_str}
📈 品种: {symbol}
💰 价格: {price}
📝 备注: {note} 

    url = f"https://api.telegram.org/bot{7924949987:AAENogVoFXJfyi9p3WivYV4yhX9Zw2WT5wQ}/sendMessage"
    payload = {
        "chat_id": -1002506581103
        "text": message.strip()
    }
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return "ok"
    else:
        return f"Error: {response.status_code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
