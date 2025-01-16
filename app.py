from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route("/interactions", methods=["POST"])
def handle_interactions():
    payload = json.loads(request.form.get("payload"))

    if "actions" in payload:
        action_id = payload['actions'][0]['action_id']
        if action_id == "create_ticket":
            return jsonify({"text": "Jira ticket successfully created!"})

    return jsonify({"text": "Unknown interaction!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT, fallback to 5000 for local
    app.run(host="0.0.0.0", port=port)
