from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")  

@app.route("/enrich", methods=["POST"])
def enrich():
    print("Enriching alert")
    data = request.json
    print(f"Alert data: {data}")
    data["extra_info"] = "Agent processed this alert!"
    print("Alert enriched")
    
    msg = {
        "text": f"Enriched Alert:\n*Title:* {data.get('title')}\n*Description:* {data.get('description')}\n*Extra:* {data['extra_info']}"
    }
    print("Sending to slack")
    requests.post(SLACK_WEBHOOK_URL, json=msg)

    print("Done")
    return jsonify({"status": "ok", "forwarded_to_slack": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)