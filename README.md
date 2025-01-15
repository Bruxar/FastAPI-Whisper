# Análisis de Videos con Whisper, yt-dlp y FastAPI

Este repositorio contiene una prueba de concepto para analizar videos a través del procesamiento de audio extraído de URLs. Utiliza las siguientes bibliotecas:

- **Whisper** de OpenAI: Para la transcripción del audio en texto.
- **yt-dlp**: Para la descarga de audio desde URLs de videos (e.g., YouTube).
- **FastAPI**: Para exponer una API que gestiona el proceso de descarga y transcripción.

## Características

1. **Descarga de audio**: Utilizando `yt-dlp`, el proyecto descarga el audio del video especificado en formato MP3.
2. **Transcripción**: Con la API de Whisper de OpenAI, convierte el audio descargado en texto.
3. **Exposición como API**: Una API basada en FastAPI recibe las URLs de los videos y retorna la transcripción.
