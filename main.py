# app/main.py
from fastapi import FastAPI, HTTPException, Query
from download_handler import download_audio_from_youtube
from whisper_handler import transcribe_audio_with_whisper
import os

app = FastAPI()

@app.post("/download_audio/")
async def download_audio(url: str = Query(...)):
    try:
        # Define la ruta donde se guardará el archivo descargado
        audio_output_path = os.path.abspath('./content/audio.mp3') 

        # Descargar el audio con yt-dlp
        result = download_audio_from_youtube(url, audio_output_path)

        if result.get("auth_message"):
            return {"message": result["message"], "auth_message": result["auth_message"]}

        # Verificar si el archivo fue creado
        if not os.path.exists(audio_output_path):
            print(f"Archivo no encontrado en {audio_output_path}")
            raise HTTPException(status_code=404, detail="No se encontró el archivo de audio descargado")

        # Transcribir el audio con Whisper
        transcription = transcribe_audio_with_whisper(audio_output_path)

        # (Opcional) Eliminar el archivo de audio después de la transcripción
        os.remove(audio_output_path)
        
        return {"message": "Transcripcion completada", "transcription": transcription}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
