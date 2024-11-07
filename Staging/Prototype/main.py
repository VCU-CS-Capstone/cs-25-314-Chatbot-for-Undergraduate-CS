from flask import Flask, render_template, request, jsonify
from chat import Chatbot
app = Flask(__name__)

chatbot = Chatbot()

@app.route('/')
def test_webpage():
    return render_template('test_webpage.html')

@app.route('/chat', methods=['POST'])
def chat():
    # request.json
    user_input= request.json.get('message')
    bot_reply = chatbot.chatbot(user_input)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)