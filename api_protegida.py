import os
from flask import Flask, request, jsonify

app = Flask(__name__)

API_SECRET = os.getenv("API_SECRET", "NO_SECRET_DEFINED")
CLAVE_DEL_SERVICIO = os.getenv("CLAVE_DEL_SERVICIO", "NO_SERVICE_PASSWORD")

@app.route("/api/clave", methods=["GET"])
def obtener_contraseña_segura():
    clave = request.args.get("clave")

    if clave == API_SECRET:
        return jsonify({
            "clave_de_acceso": CLAVE_DEL_SERVICIO
        })
    else:
        return jsonify({"error": "Acceso denegado"}), 401

if __name__ == "__main__":
    app.run(debug=True)
