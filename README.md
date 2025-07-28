## ☁️ Despliegue en Render (producción)

Este proyecto está desplegado en [Render](https://render.com), un servicio en la nube que permite ejecutar aplicaciones web con código desde GitHub y variables de entorno seguras.

---

### 🛠️ Pasos para desplegar en Render

1. Subí tu proyecto a un repositorio en GitHub (sin incluir `.env` ni claves en el código).
2. Entrá en [https://render.com](https://render.com) y creá una cuenta (podés usar tu cuenta de GitHub).
3. Hacé clic en **"New" → "Web Service"**.
4. Elegí tu repositorio.
5. Completá los campos de configuración así:

| Campo              | Valor                              |
|--------------------|-------------------------------------|
| **Name**           | proyecto-seguro                     |
| **Environment**    | Python                              |
| **Build Command**  | pip install -r requirements.txt     |
| **Start Command**  | gunicorn api_protegida:app          |
| **Root Directory** | (dejalo vacío si todo está en raíz) |

---

### 🔐 Variables de entorno en Render

Agregá la variable de entorno directamente desde el panel:

- **Key:** `API_SECRET`  
- **Value:** `clave-desde-render` (o la clave que quieras usar en producción)

> Esta clave **no se sube a GitHub** ni se guarda en ningún archivo. Render la mantiene en un entorno seguro.

---

### ✅ Resultado

Una vez desplegado, Render te dará una URL pública como:

```
https://proyecto-seguro-wdnu.onrender.com
```

Podés probar tu API así:

```
https://proyecto-seguro-wdnu.onrender.com/api/datos?clave=clave-desde-render
```

Si la clave es válida, obtendrás:

```json
{
  "usuario": "hugo",
  "rol": "admin",
  "secreto": "la contraseña es el entorno, no el código"
}
```

---

### 🎯 ¿Qué aporta Render?

- Tu aplicación está **en línea, siempre disponible**
- Las claves se almacenan **fuera del código**
- Es una forma real de aplicar buenas prácticas de seguridad en Python


