from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
@app.route('/home', methods=["GET"])
def home_route():
    return jsonify({"message": "Hi there"})


if __name__ == '__main__':
    app.run(debug=True)
