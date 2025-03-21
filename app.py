import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload_csi', methods=['POST'])
def receive_csi():
    try:
        data = request.get_json()

        timestamp = data.get("timestamp")
        csi = data.get("csi")

        if not timestamp or not isinstance(csi, list):
            return jsonify({"error": "Invalid CSI data"}), 400

        print(f"📡 CSI received | Timestamp: {timestamp} | Length: {len(csi)}")
        # Optionally: Save to file or DB
        # with open("csi_log.json", "a") as f:
        #     f.write(json.dumps(data) + "\n")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        print("❌ Error processing CSI:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
