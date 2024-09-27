# app/download_handler.py
import os
from pytube import YouTube
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

    try:
        # Descargar el video con pytube
        yt = YouTube(youtube_url)
        print(yt.title)
        print(yt.fmt_streams)
        # Filtrar para obtener solo la transmisión de audio
        streams = yt.streams.all()
        for stream in streams:
            print(stream)

    except Exception as e:
        raise Exception(f"Error al descargar el audio: {e}")
