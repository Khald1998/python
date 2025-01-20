from flask import Flask, request, jsonify
from app import generate_response

app = Flask(__name__)

@app.route('/gpt', methods=['GET'])
def generate():
    prompt = request.args.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400
    response, error = generate_response(prompt)
    if error:
        return jsonify({'error': error}), 500
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
