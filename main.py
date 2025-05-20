from fastapi import FastAPI, HTTPException, Query
from download_handler import download_audio_from_youtube
from whisper_handler import transcribe_audio_with_whisper
import os

app = FastAPI()

@app.get("/", tags=["health"])
def health():
    return {"status": "ok"}

@app.post("/download_audio")
async def download_audio(url: str = Query(...)):
    try:
        audio_path = download_audio_from_youtube(url)   # ← devuelve ruta final mp3
        if not os.path.exists(audio_path):
            raise HTTPException(404, "Archivo no encontrado")

        transcription = transcribe_audio_with_whisper(audio_path)
        os.remove(audio_path)                           # limpia disco efímero

        return {"message": "Transcripción completada", "transcription": transcription}
    except Exception as e:
        # imprime la traza en los logs para depurar
        import traceback, sys
        traceback.print_exc(file=sys.stderr)
        raise HTTPException(500, str(e))
