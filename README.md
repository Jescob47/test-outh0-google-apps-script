Ejecutar Google Apps Script desde Python

Este repositorio muestra cómo llamar funciones de Google Apps Script desde Python usando OAuth2 para la autenticación.
Lo hice porque no encontré un ejemplo práctico y claro, así que aquí queda documentado paso a paso.

Video en Youtube:
https://youtu.be/dynAsXrTKLU

🚀 Requisitos

Python 3.9+

Una cuenta de Google

Proyecto creado en Google Cloud Console con las APIs necesarias habilitadas

Archivos credentials.json y token.json (este último se genera automáticamente la primera vez que corres el script)

📦 Instalación

Se recomienda usar un entorno virtual (venv).
Instala solo las dependencias necesarias con:

pip install requests google-auth google-auth-oauthlib

▶️ Uso

Coloca tu credentials.json en la carpeta raíz del proyecto.

Modifica en el script:

API_URL → la URL de tu Apps Script desplegado como API

"myFunction" → el nombre de la función que quieres ejecutar

Corre el script:

python appscript_from_python.py


La primera vez te pedirá iniciar sesión con tu cuenta de Google para generar el archivo token.json.
Después ya podrás correrlo sin volver a autenticarte (a menos que el token caduque).

📌 Nota

Este ejemplo está pensado para personas que ya saben lo básico de Python, manejar entornos virtuales y tienen una cuenta de Google configurada.
No es un tutorial “profesional”, simplemente lo comparto porque a mí me costó bastante encontrar la forma y espero que le sirva a alguien más.
