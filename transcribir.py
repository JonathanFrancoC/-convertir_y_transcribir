import os
import subprocess
import whisper
import time
from tqdm import tqdm  # Para la barra de progreso

# 🔹 Directorios principales
BASE_DIR = r"C:\Users\jonat\Desktop\videollamadas"  # Ruta base donde se almacenan los archivos
VIDEO_DIR = os.path.join(BASE_DIR, "video")  # Carpeta que contiene los videos
AUDIO_DIR = os.path.join(BASE_DIR, "audio")  # Carpeta donde se guardarán los audios extraídos
RESUMEN_DIR = os.path.join(BASE_DIR, "resumen")  # Carpeta donde se guardarán las transcripciones en texto

# 🔹 Crear las carpetas si no existen
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(RESUMEN_DIR, exist_ok=True)

# 🔹 Cargar modelo Whisper para la transcripción
model = whisper.load_model("medium")  # Modelos disponibles: "small", "medium", "large"

def convertir_video_a_audio(video_path, audio_path):
    """
    Convierte un archivo de video en audio usando FFmpeg.
    Solo se ejecuta si el archivo de audio no existe previamente.
    """
    if not os.path.exists(audio_path):
        print(f"🎥 Convirtiendo {os.path.basename(video_path)} a audio...")
        comando = [
            "ffmpeg", "-i", video_path, "-q:a", "0", "-map", "a", audio_path, "-y"
        ]
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)  # Ejecuta FFmpeg sin mostrar salida
    else:
        print(f"⚠️ Audio ya existe: {os.path.basename(audio_path)}, omitiendo conversión.")

def formatear_texto(texto, palabras_por_linea=50):
    """
    Divide el texto en líneas de un número determinado de palabras.
    Esto facilita la lectura en los archivos de texto resultantes.
    """
    palabras = texto.split()
    lineas = [" ".join(palabras[i:i + palabras_por_linea]) for i in range(0, len(palabras), palabras_por_linea)]
    return "\n".join(lineas)  # Une las líneas con saltos de línea

def transcribir_audio_a_texto(audio_path, texto_path):
    """
    Transcribe el audio a texto usando Whisper.
    Muestra una barra de progreso durante el proceso.
    """
    if not os.path.exists(texto_path):
        print(f"🎙️ Transcribiendo {os.path.basename(audio_path)} en tiempo real...")

        # Transcribe el audio
        result = model.transcribe(audio_path)

        # Barra de progreso con delay para visualización
        for _ in tqdm(range(100), desc="📖 Progreso de Transcripción", ascii=" █", ncols=75):
            time.sleep(0.02)

        # Formatear texto con saltos de línea cada 50 palabras
        texto_final = formatear_texto(result["text"]) 
        
        # Guardar el texto transcrito en un archivo en la carpeta "resumen"
        with open(texto_path, "w", encoding="utf-8") as f:
            f.write(texto_final)

        print(f"✅ Transcripción guardada en {texto_path}")

        # Eliminar el archivo de audio después de la transcripción
        os.remove(audio_path)
        print(f"🗑️ Archivo de audio {audio_path} eliminado.")
    else:
        print(f"⚠️ Transcripción ya existe: {os.path.basename(texto_path)}, omitiendo transcripción.")

# 🔹 Procesar todos los videos en la carpeta "video"
for archivo in os.listdir(VIDEO_DIR):
    if archivo.endswith((".mp4", ".mkv", ".avi", ".mov")):  # Verifica formatos de video compatibles
        video_path = os.path.join(VIDEO_DIR, archivo)
        audio_path = os.path.join(AUDIO_DIR, archivo.rsplit(".", 1)[0] + ".mp3")  # Nombre del archivo de audio
        texto_path = os.path.join(RESUMEN_DIR, archivo.rsplit(".", 1)[0] + ".txt")  # Nombre del archivo de texto

        # Convertir video a audio
        convertir_video_a_audio(video_path, audio_path)

        # Transcribir audio a texto
        transcribir_audio_a_texto(audio_path, texto_path)

print("🚀 ¡Proceso completado! Revisa la carpeta 'resumen'.")