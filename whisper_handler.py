from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(OPENAI_API_KEY)

# Función para transcribir el audio usando la API de Whisper
def transcribe_audio_with_whisper(audio_path):
    # Cargar la clave de la API desde las variables de entorno
    client = OpenAI(api_key=OPENAI_API_KEY)
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        # Devolver el texto de la transcripción
        return transcription.text

