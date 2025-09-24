import os
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import traceback
import requests

# --- Configuración --
SCOPES = [
    "https://www.googleapis.com/auth/script.projects",
    "https://www.googleapis.com/auth/script.scriptapp",
"https://www.googleapis.com/auth/script.external_request"
  # <- este es el importante
]


TOKEN_PATH = "token.json"
CREDENTIALS_PATH = "credentials.json"

creds = None

# --- Autenticación OAuth2 ---
try:
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_PATH, "w") as token_file:
            token_file.write(creds.to_json())

except Exception as e:
    print("Error autenticando:", traceback.format_exc())
    raise e

# --- Llamada a Apps Script API ---
try:
    url = f"API_URL"
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json"
    }

    payload = {
        "function": "myFunction",      # Función que definimos en Apps Script
        "parameters": []      # Parámetros de la función
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Status:", response.status_code)

    if response.status_code == 200:
        result = response.json()
        if "response" in result and "result" in result["response"]:
            print("Resultado:", result["response"]["result"])
        else:
            print("Respuesta completa:", result)
    else:
        print("Error:", response.text)

except Exception as e:
    print("Error ejecutando script:", traceback.format_exc())
