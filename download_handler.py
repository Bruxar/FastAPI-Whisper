# app/download_handler.py
import yt_dlp as youtube_dl
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("YOUTUBE_USERNAME")
password = os.getenv("YOUTUBE_PASSWORD")

# Función para descargar el video de YouTube como archivo MP3
def download_audio_from_youtube(youtube_url, output_path='./content/audio.mp3'):
    # Crea la carpeta content en la raíz si no existe
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,  # Guarda el archivo directamente como audio.mp3
        'username': username,  # Usar la variable de entorno para el nombre de usuario
        'password': password,  # Usar la variable de entorno para la contraseña
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except Exception as e:
        raise Exception(f"Error al descargar el audio: {e}")
