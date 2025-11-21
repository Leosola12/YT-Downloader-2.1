
# 🎬 YT Downloader 2.1 – Streamlit Edition

Una aplicación web simple y poderosa para descargar **videos, audios y subtítulos de YouTube** con estilo.  
Construida con Streamlit y yt-dlp.

---

## ✨ Features

- 📥 Descargar videos en formato **MP4**
- 🎧 Descargar audios en formato **MP3**
- 📜 Descargar subtítulos en múltiples idiomas (formato `.srt`)
- 🎞️ Opción **Todos** → baja video, audio y subtítulos en un solo paso
- 🖼️ Miniaturas y títulos de cada video antes de descargar
- 📊 Barra de progreso por lote de URLs
- 📂 Elegir carpeta de destino (incluye opción de usar la carpeta de descargas del sistema)
- ⚠️ Aviso si el video no tiene subtítulos en el idioma solicitado (o, en su defecto, la herramienta no logra detectarlos)

---

## 📁 Estructura del proyecto

yt_downloader_app/

├── app.py               # Interfaz Streamlit

├── downloader.py        # Lógica de descarga (videos, audios, subtítulos)

├── utils.py             # Validaciones y helpers

├── requirements.txt     # Dependencias

└── README.txt           # Documentación

---

## 🚀 Instalación

1. Cloná el repositorio:

   git clone https://github.com/Leosola12/YT-Downloader-2.1.git
   cd yt_downloader_app

2. Instalá las dependencias:

   pip install -r requirements.txt

3. Ejecutá la aplicación:

   streamlit run app.py

---

## 🧩 Uso

1. Pegá una o varias URLs de YouTube (una por línea).
2. Elegí el formato de descarga: **MP4**, **MP3**, **Subtítulos**, o **Todos**.
3. Seleccioná carpeta de destino (o marcá la opción de usar la carpeta de descargas del sistema).
4. Presioná 🚀 Ejecutar y mirá cómo se descargan tus archivos.

---

## 📦 Dependencias

- Streamlit
- yt-dlp
- FFmpeg (para conversión de audio a MP3)
