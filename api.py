from flask import Flask, request

import baidu.api_ai_baidu

app = Flask(__name__)

@app.route('/ai', methods=['POST'])
def ai():
    data = request.get_json()
    text = data.get('text', '')
    return baidu.api_ai_baidu.getOneData(text)

if __name__ == '__main__':
    app.run(debug=True)