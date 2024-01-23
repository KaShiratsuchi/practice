from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json['data']
    print(data)
    return jsonify({
        "status": "success",
        "data": data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
