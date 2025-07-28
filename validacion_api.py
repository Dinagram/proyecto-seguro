import os
from flask import Flask, request, jsonify

app = Flask(__name__)

API_SECRET = os.getenv("API_SECRET", "NO_SECRET_DEFINED")

@app.route("/")
def home():
    return jsonify({"message": "API funcionando correctamente"})

@app.route("/validar", methods=["POST"])
def validar_clave():
    data = request.get_json()
    clave_ingresada = data.get("clave")

    if clave_ingresada == API_SECRET:
        return jsonify({"acceso": "autorizado"}), 200
    else:
        return jsonify({"acceso": "denegado"}), 401

if __name__ == "__main__":
    app.run(debug=True)
