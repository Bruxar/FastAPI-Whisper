# app/download_handler.py
import yt_dlp as youtube_dl
import os, random, string

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

def _bright_proxy() -> str:
    """Devuelve la URL del proxy con un session-id aleatorio para forzar rotación IP."""
    base = os.getenv("YT_PROXY")          # tomado del entorno
    if not base:
        return None                       # sin proxy → descarga directa
    #  Añade un sufijo -session-<rnd> al nombre de usuario
    rnd = ''.join(random.choices(string.hexdigits.lower(), k=8))
    return base.replace(":gsre", f"-session-{rnd}:gsre", 1)

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
        "user_agent": UA,
        "http_headers": {"Accept-Language": "es-ES,es;q=0.9,en;q=0.8",},
        "sleep_interval": 5,
        "max_sleep_interval": 15,
        "proxy": _bright_proxy(),
        "retries": 3,
        "fragment_retries": 3,
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
    except Exception as e:
        raise Exception(f"Error al descargar el audio: {e}")
