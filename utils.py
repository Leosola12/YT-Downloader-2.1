# utils.py
import re

def limpiar_urls(texto):
    """Convierte texto multilinea en lista de URLs limpias"""
    return [line.strip() for line in texto.splitlines() if line.strip()]

def validar_url_youtube(url):
    """Valida si una URL parece de YouTube"""
    patron = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+"
    return re.match(patron, url) is not None

def extraer_miniatura(info_dict):
    """Devuelve la URL de la miniatura del video"""
    return info_dict.get("thumbnail", "")

def obtener_titulo(info_dict):
    """Devuelve el título del video"""
    return info_dict.get("title", "Video sin título")
