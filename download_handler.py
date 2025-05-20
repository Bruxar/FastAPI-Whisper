# app/download_handler.py
import yt_dlp as youtube_dl
import os, random, string, uuid

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

def _bright_proxy() -> str | None:
    """Devuelve la URL del proxy Bright Data con session-id aleatorio."""
    base = os.getenv("YT_PROXY")              # NO debe llevar comillas en la env-var
    if not base:
        return None
    rnd = ''.join(random.choices(string.hexdigits.lower(), k=8))
    # Inserta -session-<rnd> justo antes de la contraseña (tras el primer ':')
    return base.replace(":", f"-session-{rnd}:", 1)

def download_audio_from_youtube(youtube_url: str, output_dir: str = "./content") -> str:
    """Descarga audio y devuelve la ruta final del .mp3 generado."""
    os.makedirs(output_dir, exist_ok=True)
    tmp_name = uuid.uuid4().hex                        # nombre base único

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        # SIN extensión fija → %(ext)s la pone yt-dlp; ffmpeg la cambia a .mp3
        "outtmpl": os.path.join(output_dir, f"{tmp_name}.%(ext)s"),
        "user_agent": UA,
        "http_headers": {"Accept-Language": "es-ES,es;q=0.9,en;q=0.8"},
        "sleep_interval": 5,
        "max_sleep_interval": 15,
        "proxy": _bright_proxy(),
        "retries": 3,
        "fragment_retries": 3,
        "quiet": False,
        "verbose": True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        # yt-dlp >=2024.04 expone 'filepath' con la ruta final
        final_path = info.get("filepath") or ydl.prepare_filename(info).rsplit('.', 1)[0] + ".mp3"
        return final_path
