from flask import Flask, render_template, request, jsonify
from test import chatbot_response
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input= request.json.get('message')
    bot_reply = chatbot_response(user_input)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)