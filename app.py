from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "EAAMwZBWNnX1wBQw2wDmbGKsJUoj5I8lJYut3Vtv9jtwZBYamIuPl3uUa9IOmHPaCAcEqAC082RdS1GFLhm3A9HAGrvCEQWLGFGPfmZCHNE6SQlLBxnNXKcBUULTZADJvDjcis53KsHeMS5Hup5AtrqIQeYRM3AIuqaOmgUVFHI3WA97B6DMYSx4DC6oCnA4K6gZA6vAnCu6WA2kMGzfzkIAZDZD"

@app.route("/webhook", methods=["GET"])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed"

@app.route("/webhook", methods=["POST"])
def webhook():
    print(request.json)
    return "OK", 200

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=10000)
