import os

from flask import Flask, jsonify
#de normal aqui cragarias el env

app = Flask(__name__)

@app.route("/")
def index():
    secret = os.getenv("API_SECRET", "NO_SECRET_DEFINED")
    return jsonify({"message": "La app funciona", "api_secret": secret})

if __name__ == "__main__":
    app.run(debug=True)

