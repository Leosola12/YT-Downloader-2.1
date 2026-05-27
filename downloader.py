import os
import yt_dlp


def _base_opts(output_dir):
    os.makedirs(output_dir, exist_ok=True)

    return {
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),

        # estabilidad
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,

        # retries
        "retries": 3,
        "fragment_retries": 3,

        # MUY IMPORTANTE
        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        },
    }


def descargar_video(urls, formato="mp4", output_dir="downloads"):
    errores = []

    opts = _base_opts(output_dir)

    # ===== VIDEO =====
    if formato == "mp4":

        # IMPORTANTE:
        # usamos streams progresivos primero
        # MUCHÍSIMO más estables en cloud
        opts.update({
            "format": (
                "best[ext=mp4]/"
                "best/"
                "bv*+ba/b"
            ),

            "merge_output_format": "mp4",
        })

    # ===== AUDIO =====
    elif formato == "mp3":

        opts.update({
            "format": "bestaudio/best",

            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        })

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(urls)

    except Exception as e:
        errores.append(str(e))

    return errores


def descargar_subtitulos(urls, idiomas=["es"], output_dir="downloads"):
    errores = []

    opts = _base_opts(output_dir)

    opts.update({
        "skip_download": True,

        "writesubtitles": True,
        "writeautomaticsub": True,

        "subtitleslangs": idiomas,

        "subtitlesformat": "srt",
    })

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(urls)

    except Exception as e:
        errores.append(str(e))

    return errores


def descargar_todo(urls, idiomas=["es"], output_dir="downloads"):
    errores = []

    opts = _base_opts(output_dir)

    opts.update({
        # streams progresivos primero
        "format": (
            "best[ext=mp4]/"
            "best/"
            "bv*+ba/b"
        ),

        "merge_output_format": "mp4",

        # subtítulos
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitleslangs": idiomas,
        "subtitlesformat": "srt",
    })

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(urls)

    except Exception as e:
        errores.append(str(e))

    return errores


def obtener_info_video(url):

    opts = {
        "quiet": True,
        "skip_download": True,

        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        },
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            return ydl.extract_info(url, download=False)

    except:
        return {}


def obtener_subtitulos_disponibles(url):

    opts = {
        "quiet": True,
        "skip_download": True,
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:

            info = ydl.extract_info(url, download=False)

            subs = info.get("subtitles", {})
            auto = info.get("automatic_captions", {})

            return list(set(subs.keys()) | set(auto.keys()))

    except:
        return []
