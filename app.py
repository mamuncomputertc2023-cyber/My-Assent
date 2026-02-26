from flask import Flask, request
import requests

app = Flask(__name__)

# 🔹 Put your verify token here (the one you used in Meta webhook)
VERIFY_TOKEN = "myverify123"

# 🔹 Put your NEW Page Access Token here
PAGE_ACCESS_TOKEN = "EAAMwZBWNnX1wBQw2wDmbGKsJUoj5I8lJYut3Vtv9jtwZBYamIuPl3uUa9IOmHPaCAcEqAC082RdS1GFLhm3A9HAGrvCEQWLGFGPfmZCHNE6SQlLBxnNXKcBUULTZADJvDjcis53KsHeMS5Hup5AtrqIQeYRM3AIuqaOmgUVFHI3WA97B6DMYSx4DC6oCnA4K6gZA6vAnCu6WA2kMGzfzkIAZDZD
"


def send_message(recipient_id, message_text):
    url = f"https://graph.facebook.com/v18.0/me/messages?access_token={PAGE_ACCESS_TOKEN}"

    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message_text}
    }

    r = requests.post(url, json=payload)
    print("Send message status:", r.status_code)
    print(r.text)


@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Incoming data:", data)

    if "entry" in data:
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                sender_id = messaging_event["sender"]["id"]

                if "message" in messaging_event:
                    user_message = messaging_event["message"].get("text")

                    if user_message:
                        reply = f"You said: {user_message}"
                        send_message(sender_id, reply)

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
