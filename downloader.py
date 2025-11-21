# downloader.py
import os
from yt_dlp import YoutubeDL

def obtener_info_video(url):
    """Devuelve metadatos del video (título, miniatura, etc.)"""
    opciones = {"skip_download": True}
    with YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=False)
    return info

def descargar_video(urls, formato="mp4", output_dir="."):
    """Descarga uno o varios videos en MP4 o MP3"""
    os.makedirs(output_dir, exist_ok=True)

    if formato == "mp4":
        opciones = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        }
    elif formato == "mp3":
        opciones = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    else:
        raise ValueError("Formato no soportado")

    errores = []
    with YoutubeDL(opciones) as ydl:
        for url in urls:
            try:
                ydl.download([url])
            except Exception as e:
                errores.append((url, str(e)))
    return errores

def obtener_subtitulos_disponibles(url):
    """Devuelve los idiomas de subtítulos disponibles para un video"""
    opciones = {"skip_download": True}
    with YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url, download=False)
    return list(info.get("subtitles", {}).keys())

def descargar_subtitulos(urls, idiomas=["es"], output_dir="."):
    os.makedirs(output_dir, exist_ok=True)

    opciones = {
        "skip_download": True,
        "writesubtitles": True,
        "subtitleslangs": idiomas,
        "subtitlesformat": "srt",   # ✅ fuerza formato .srt
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    }

    errores = []
    with YoutubeDL(opciones) as ydl:
        for url in urls:
            try:
                ydl.download([url])
            except Exception as e:
                errores.append((url, str(e)))
    return errores

    errores = []
    with YoutubeDL(opciones) as ydl:
        for url in urls:
            try:
                ydl.download([url])
            except Exception as e:
                errores.append((url, str(e)))
    return errores

def descargar_todo(urls, idiomas=["es"], output_dir="."):
    """Descarga MP4, MP3 y subtítulos en un solo paso"""
    errores = []
    for url in urls:
        try:
            err1 = descargar_video([url], formato="mp4", output_dir=output_dir)
            err2 = descargar_video([url], formato="mp3", output_dir=output_dir)
            err3 = descargar_subtitulos([url], idiomas=idiomas, output_dir=output_dir)
            errores.extend(err1 + err2 + err3)
        except Exception as e:
            errores.append((url, str(e)))
    return errores
