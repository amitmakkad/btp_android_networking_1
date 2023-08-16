from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_base_url', methods=['GET'])
def get_base_url():
    base_url = "https://b031-103-159-214-223.ngrok-free.app/"  # Replace with your server's base URL
    return jsonify({"baseUrl": base_url})

if __name__ == '__main__':
    app.run(debug=True)
