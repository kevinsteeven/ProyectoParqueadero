import requests
from config import AZURE_ENDPOINT, PREDICTION_KEY

def classify_image(image_bytes):
    """
    Envía una imagen a Azure para clasificación.
    """
    headers = {
        "Prediction-Key": PREDICTION_KEY,
        "Content-Type": "application/octet-stream",
    }

    # Realizar la petición a la API de Azure
    response = requests.post(AZURE_ENDPOINT, headers=headers, data=image_bytes)
    response.raise_for_status()

    # Parsear la respuesta JSON
    prediction = response.json()

    # Obtener la etiqueta y convertirla a minúsculas
    result = prediction["predictions"][0]["tagName"].lower()  # Normaliza a minúsculas

    return result