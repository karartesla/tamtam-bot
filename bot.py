from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")
API_URL = f"https://botapi.tamtam.chat/messages?access_token={TOKEN}"

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["recipient"]["chat_id"]
        send_message(chat_id, "هلا! شلونك؟ هذا رد تلقائي.")
    return "ok"

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    requests.post(API_URL, json=payload)

@app.route("/", methods=["GET"])
def home():
    return "TamTam Bot Running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
