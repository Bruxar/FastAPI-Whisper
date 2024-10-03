# app/download_handler.py
import subprocess
import os
import re

# Función para descargar el video de YouTube como archivo MP3
def download_audio_from_youtube(youtube_url, output_path='./content/audio.mp3'):
    # Crea la carpeta content en la raíz si no existe
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_command = [
        'yt-dlp', 
        '--format', 'bestaudio/best', 
        '--postprocessor-args', 'FFmpegExtractAudio', 
        '--audio-format', 'mp3', 
        '--audio-quality', '192K', 
        '--output', output_path,
        '--username', 'oauth2', 
        '--password', ' ',
        youtube_url
    ]

    try:
        # Ejecutar el comando yt-dlp y capturar la salida
        result = subprocess.run(ydl_command, capture_output=True, text=True)
        
        if result.returncode != 0:
            error_message = result.stderr.strip()
            # Busca el mensaje de autorización
            auth_message = re.search(r'To give yt-dlp access to your account, go to (.+?) and enter code (\w+-\w+-\w+)', error_message)

            if auth_message:
                verification_url = auth_message.group(1)
                code = auth_message.group(2)
                return {
                    "message": "Authorization required",
                    "auth_message": f"Go to {verification_url} and enter code {code}"
                }

            # Si es otro tipo de error, lo manejamos como tal
            raise Exception(f"Error al descargar el audio: {error_message}")

        return {
            "message": "Audio descargado correctamente",
            "output": result.stdout.strip()
        }

    except Exception as e:
        raise Exception(f"Error al descargar el audio: {str(e)}")