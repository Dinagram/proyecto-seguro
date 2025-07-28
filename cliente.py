import requests

URL = "https://proyecto-seguro-wdnu.onrender.com/api/clave"
PARAMS = {"clave": "####"}  # misma clave que guardaste en Render

response = requests.get(URL, params=PARAMS)

if response.status_code == 200:
    data = response.json()
    print("✅ Clave recibida:", data["clave_de_acceso"])
else:
    print("❌ Error:", response.json()["error"])
