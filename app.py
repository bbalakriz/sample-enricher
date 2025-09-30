from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")  

@app.route("/enrich", methods=["POST"])
def enrich():
    data = request.json
    data["extra_info"] = "Agent processed this alert!"
    
    msg = {
        "text": f"Enriched Alert:\n*Title:* {data.get('title')}\n*Description:* {data.get('description')}\n*Extra:* {data['extra_info']}"
    }
    requests.post(SLACK_WEBHOOK_URL, json=msg)

    return jsonify({"status": "ok", "forwarded_to_slack": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
