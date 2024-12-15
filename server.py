from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        # Termux से डेटा लेना
        data = request.json
        access_token = data.get("access_token")
        target_id = data.get("target_id")
        message = data.get("message")

        # API रिक्वेस्ट सिमुलेशन
        url = f"https://graph.facebook.com/v17.0/t_{target_id}"
        parameters = {
            "access_token": access_token,
            "message": message
        }

        # असली API कॉल (चाहें तो अनकॉमेंट करें)
        # response = requests.post(url, data=parameters)

        # मॉक रिस्पॉन्स
        response = {"status": "success", "message": "Message sent successfully!"}

        return jsonify(response)

    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
