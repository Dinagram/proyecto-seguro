import requests

URL = "https://proyecto-seguro-wdnu.onrender.com/api/clave"
PARAMS = {"clave": "clave-desde-render"}

response = requests.get(URL, params=PARAMS)

if response.status_code == 200:
    data = response.json()
    print("🔐 Clave obtenida desde la API:", data["clave_de_acceso"])
else:
    print("❌ Error al obtener la clave:", response.status_code)
