import os
import yt_dlp


def get_ydl_opts(output_dir, formato="mp4"):
    os.makedirs(output_dir, exist_ok=True)

    if formato == "mp3":
        return {
            "format": "bestaudio/best",

            "outtmpl": f"{output_dir}/%(title)s.%(ext)s",

            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],

            "noplaylist": True,
            "retries": 10,
            "fragment_retries": 10,

            "quiet": True,

            "extractor_args": {
                "youtube": {
                    "player_client": ["android", "web"]
                }
            },

            "http_headers": {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/137.0 Safari/537.36"
                )
            },

            "sleep_interval": 1,
            "max_sleep_interval": 3,
        }

    return {
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/best",

        "merge_output_format": "mp4",

        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",

        "noplaylist": True,

        "retries": 10,
        "fragment_retries": 10,

        "quiet": True,

        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        },

        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/137.0 Safari/537.36"
            )
        },

        "sleep_interval": 1,
        "max_sleep_interval": 3,
    }


def descargar_video(urls, formato="mp4", output_dir="downloads"):
    errores = []

    opts = get_ydl_opts(output_dir, formato)

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(urls)

    except Exception as e:
        errores.append(str(e))

    return errores


def descargar_subtitulos(urls, idiomas=["es"], output_dir="downloads"):
    errores = []

    opts = {
        "writesubtitles": True,
        "subtitleslangs": idiomas,
        "skip_download": True,

        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",

        "quiet": True,

        "extractor_args": {
            "youtube": {
                "player_client": ["android", "web"]
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(urls)

    except Exception as e:
        errores.append(str(e))

    return errores


def descargar_todo(urls, idiomas=["es"], output_dir="downloads"):
    errores = []

    opts = get_ydl_opts(output_dir, "mp4")

    opts.update({
        "writesubtitles": True,
        "subtitleslangs": idiomas,
    })

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download(urls)

    except Exception as e:
        errores.append(str(e))

    return errores


def obtener_info_video(url):
    try:
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            return ydl.extract_info(url, download=False)
    except:
        return {}


def obtener_subtitulos_disponibles(url):
    try:
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)

            subs = info.get("subtitles", {})
            auto = info.get("automatic_captions", {})

            disponibles = set(subs.keys()) | set(auto.keys())

            return list(disponibles)

    except:
        return []
