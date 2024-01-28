from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/messages', methods=['POST'])
def receive_message():
    data = request.json
    # Assuming data contains a 'message' sent by the user
    user_message = data.get('message', '')

    # TODO: Here you can add the logic to process the user message,
    # like sending it to the Azure Bot or QnA service, and get a response.

    # This is a placeholder response
    bot_response = f"You said: {user_message}"

    # Return the response in JSON format
    return jsonify({
        'response': bot_response
    })

if __name__ == '__main__':
    # Note that in production, you might want to set 'debug' to False
    app.run(debug=True, host='0.0.0.0', port=80)
