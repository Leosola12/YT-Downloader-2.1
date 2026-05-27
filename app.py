# app.py
import os
import streamlit as st
from downloader import (
    descargar_video,
    descargar_subtitulos,
    descargar_todo,
    obtener_info_video,
    obtener_subtitulos_disponibles
)
from utils import limpiar_urls, validar_url_youtube, extraer_miniatura, obtener_titulo

st.set_page_config(page_title="YT Downloader 2.1", page_icon="🎬", layout="centered")

st.title("🎬 YouTube Downloader 2.1")
st.markdown("Descargá videos, audios y subtítulos de YouTube con estilo.")

# Selección de formato
modo = st.selectbox(
    "Elegí formato de descarga",
    ["MP4 (video)", "MP3 (audio)", "Subtítulos (SRT)", "Todos"]
)

# URLs
urls_input = st.text_area("Pegá una o varias URLs (una por línea)")
urls = limpiar_urls(urls_input)

# Carpeta de destino
usar_descargas = st.checkbox("📂 Usar carpeta de descargas del sistema")
if usar_descargas:
    output_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    st.info(f"Los archivos se guardarán en: {output_dir}")
else:
    output_dir = st.text_input("📂 Carpeta de destino", value="downloads")

# Idiomas de subtítulos
idiomas = []
if modo in ["Subtítulos (SRT)", "Todos"]:
    idiomas = st.multiselect(
        "Elegí idioma(s) de subtítulo",
        ["es", "en", "fr", "pt", "de"],
        default=["es"]
    )

# Botón de ejecución
if st.button("🚀 Ejecutar"):
    if not urls:
        st.warning("Por favor, ingresá al menos una URL.")
    else:
        progreso = st.progress(0)
        total = len(urls)

        for i, url in enumerate(urls):
            if not validar_url_youtube(url):
                st.error(f"❌ URL inválida: {url}")
                continue

            info = obtener_info_video(url)
            st.subheader(obtener_titulo(info))
            miniatura = extraer_miniatura(info)
            if miniatura:
                st.image(miniatura, width=320)

            # ✅ siempre pasamos [url] como lista
            if modo == "MP4 (video)":
                errores = descargar_video([url], formato="mp4", output_dir=output_dir)
            elif modo == "MP3 (audio)":
                errores = descargar_video([url], formato="mp3", output_dir=output_dir)
            elif modo == "Subtítulos (SRT)":
                disponibles = obtener_subtitulos_disponibles(url)
                if not any(lang in disponibles for lang in idiomas):
                    st.warning(f"⚠️ No hay subtítulos en {idiomas} para {url}. Disponibles: {disponibles}")
                    errores = []
                else:
                    errores = descargar_subtitulos([url], idiomas=idiomas, output_dir=output_dir)
            else:  # Todos
                disponibles = obtener_subtitulos_disponibles(url)
                if not any(lang in disponibles for lang in idiomas):
                    st.warning(f"⚠️ No hay subtítulos en {idiomas} para {url}. Disponibles: {disponibles}")
                errores = descargar_todo([url], idiomas=idiomas, output_dir=output_dir)

            if errores:
                st.error(f"❌ Error en {url}: {errores}")
            else:
                st.success(f"✅ Descarga completada: {url}")

            progreso.progress((i + 1) / total)

        st.success("🎉 ¡Todas las descargas finalizadas!")
        # --- Footer ---
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center">
        <p>Creado con ❤️ por <b>Leonardo Sola</b></p>
        <a href="https://github.com/LeoSola12" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" 
                 width="40" style="margin:10px; background-color:white; border-radius:8px; padding:5px">
        </a>
        <a href="https://www.instagram.com/leeeeeeeo_/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" 
                 width="40" style="margin:10px; background-color:white; border-radius:8px; padding:5px">
        </a>
        <a href="https://x.com/LeoSola7" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/5968/5968830.png" 
                 width="40" style="margin:10px; background-color:white; border-radius:8px; padding:5px">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

