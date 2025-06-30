from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
API_URL = f"https://botapi.tamtam.chat/messages?access_token={TOKEN}"

@app.route("/", methods=["GET"])
def home():
    return "TamTam Bot is running!"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["recipient"]["chat_id"]
        msg = data["message"]["body"]["text"].lower()
        
        if "سلام" in msg:
            send_message(chat_id, "وعليكم السلام 🌟")
        elif "اسمك" in msg:
            send_message(chat_id, "اسمي بوت تمتم 🤖")
        else:
            send_message(chat_id, "ما فهمت قصدك، جرب شي ثاني 🧐")
    return "ok"

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(API_URL, json=payload)

app.run(host="0.0.0.0", port=8080)
