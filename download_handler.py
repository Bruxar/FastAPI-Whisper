# app/download_handler.py
import subprocess
import os

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

        # Verificar si hay errores en la salida
        if result.returncode != 0:
            raise Exception(f"Error al descargar el audio: {result.stderr.strip()}")

        # Comprobar si el mensaje de autenticación está en la salida
        auth_message = None
        if 'To give yt-dlp access to your account' in result.stdout:
            # Captura el mensaje de autenticación
            auth_message = result.stdout.splitlines()[-1]  # Obtiene la última línea que contiene el mensaje

        # Retornar la respuesta
        return {
            "message": "Audio descargado correctamente" if auth_message is None else "Necesitas autorizar el acceso.",
            "auth_message": auth_message,  # Si hay mensaje de autenticación, se incluye
            "output": result.stdout.strip()
        }

    except Exception as e:
        raise Exception(f"Error al descargar el audio: {str(e)}")
