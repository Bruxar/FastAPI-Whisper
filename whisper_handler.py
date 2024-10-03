from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Función para transcribir el audio usando la API de Whisper
# def transcribe_audio_with_whisper(audio_path):
#     # Cargar la clave de la API desde las variables de entorno
#     client = OpenAI(api_key=OPENAI_API_KEY)
#     with open(audio_path, "rb") as audio_file:
#         transcription = client.audio.transcriptions.create(
#             model="whisper-1",
#             file=audio_file
#         )
#         # Devolver el texto de la transcripción
#         return transcription.text

def transcribe_audio_with_whisper(audio_path):
    print(audio_path)
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras et ipsum vitae leo consequat dictum. Nulla ullamcorper maximus aliquet. Integer placerat quis augue vel vehicula. Nullam tincidunt diam dignissim, dictum velit nec, tempus massa. Suspendisse at velit nec justo egestas blandit. Curabitur vehicula tortor accumsan lacus auctor tempor. Integer feugiat pellentesque massa ut egestas."