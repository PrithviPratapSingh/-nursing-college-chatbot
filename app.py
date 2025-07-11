from flask import Flask, render_template, request, jsonify
from chatbot import NursingCollegeChatbot
import uuid

app = Flask(__name__)
chatbot = NursingCollegeChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    user_id = data.get('user_id', str(uuid.uuid4()))
    
    response = chatbot.get_response(user_id, user_message)
    
    return jsonify({
        'response': response,
        'user_id': user_id
    })

@app.route('/reset', methods=['POST'])
def reset():
    data = request.get_json()
    user_id = data.get('user_id', '')
    
    if user_id in chatbot.sessions:
        del chatbot.sessions[user_id]
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 