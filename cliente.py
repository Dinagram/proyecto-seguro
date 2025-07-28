import requests
import getpass

# Oculta la entrada para mayor seguridad
clave_ingresada = getpass.getpass("🔑 Ingresá la clave de acceso: ")

URL = "https://proyecto-seguro-wdnu.onrender.com/api/clave"
PARAMS = {"clave": clave_ingresada}

response = requests.get(URL, params=PARAMS)

if response.status_code == 200:
    data = response.json()
    print("✅ Clave obtenida:", data["clave_de_acceso"])
else:
    print("❌ Error:", response.json()["mensaje"])

