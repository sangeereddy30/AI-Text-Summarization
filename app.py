from flask import Flask, request, jsonify
from flask_cors import CORS
# CORS(app)
import openai
app = Flask(__name__)
CORS(app)
openai.api_key = "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"
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    )
    summary = response['choices'][0]['message']['content']
    return jsonify({"summary": summary})
if __name__ == '__main__':
    app.run(debug=True)
