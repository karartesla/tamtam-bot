from flask import Flask, request
import requests

app = Flask(name)

# ضع توكن البوت هنا
TOKEN = "f9LodDOcOJT8LGSn3FiZAdMVLApj7o3 PHGf-ocZutYCZHCV1QGSk4KwPUPzdcHF GsnbqLeplvXEaKRnZVfRow"

def send_message(user_id, text):
    url = f"https://botapi.tamtam.chat/messages?access_token={TOKEN}"
    data = {
        "recipient": {"user_id": user_id},
        "message": {"text": text}
    }
    requests.post(url, json=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    try:
        user_id = data['message']['sender']['user_id']
        text = data['message']['body']['text']
        if "سلام" in text:
            send_message(user_id, "وعليكم السلام 🌟")
        else:
            send_message(user_id, "أهلاً بك! هذا بوت الحماية 👮")
    except:
        pass
    return "ok"

app.run(host="0.0.0.0", port=81)
