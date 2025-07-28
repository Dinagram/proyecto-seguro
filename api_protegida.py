import os
from flask import Flask, request, jsonify

app = Flask(__name__)

API_SECRET = os.getenv("API_SECRET", "NO_SECRET_DEFINED")

@app.route("/api/datos", methods=["GET"])
def datos_protegidos():
    clave = request.args.get("clave")

    if clave == API_SECRET:
        # Datos protegidos: podrían venir de una base de datos, por ejemplo
        datos = {
            "usuario": "hugo",
            "rol": "admin",
            "secreto": "la contraseña es el entorno, no el código"
        }
        return jsonify(datos)
    else:
        return jsonify({"error": "Acceso denegado"}), 401

if __name__ == "__main__":
    app.run(debug=True)
