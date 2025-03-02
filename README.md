# 📌 **Documentación del Script: Conversión de Video a Texto con Whisper**

## 📖 **Descripción**
Este script permite convertir archivos de video en texto utilizando **Whisper**, un modelo de reconocimiento de voz de OpenAI. Primero, extrae el audio de los videos, luego lo transcribe a texto y lo guarda en una carpeta específica.

## 📂 **Estructura de Directorios**
El script trabaja dentro de la carpeta:

```
C:\Users\jonat\Desktop\videollamadas
```

Los archivos se organizan en las siguientes carpetas:
- 📁 `video/` → Carpeta donde deben colocarse los archivos de video a procesar.
- 🎧 `audio/` → Carpeta donde se guardan los archivos de audio temporalmente.
- 📄 `resumen/` → Carpeta donde se guardan los archivos de texto generados con la transcripción.

### ⚠ **Nota Importante**
🔴 **Este script está configurado para ejecutarse en una ruta específica (`C:\Users\jonat\Desktop\videollamadas`).**  
Si otro usuario intenta ejecutar el script sin modificar la ruta, puede obtener errores de directorio.  
Para evitar esto, **modifique la variable `BASE_DIR` en el código**, estableciendo su propia ruta.

```python
# Cambiar esta ruta según el usuario y ubicación deseada
BASE_DIR = r"C:\Users\SU_USUARIO\Desktop\videollamadas"
```

---

## 🛠 **Requisitos Previos**
### 🔹 **Instalación de Dependencias**
Antes de ejecutar el script, asegúrate de instalar los siguientes paquetes:

```bash
pip install openai-whisper tqdm ffmpeg-python
```

También necesitas **FFmpeg**, que puedes instalar en Windows con:

```bash
choco install ffmpeg
```
(O descarga e instala manualmente desde [ffmpeg.org](https://ffmpeg.org))

---

## ⚙️ **Funcionamiento del Script**
### **1️⃣ Conversión de Video a Audio**
- **Si el archivo de audio ya existe**, el script omite la conversión para evitar duplicados.
- **Si no existe**, usa `ffmpeg` para extraer el audio del video.

### **2️⃣ Transcripción del Audio**
- **Si el archivo de texto ya existe**, el script lo omite.
- **Si no existe**, el script transcribe el audio usando **Whisper** (`medium` por defecto) y lo guarda en la carpeta `resumen/`.

### **3️⃣ Formateo del Texto**
- La transcripción se divide en líneas de **50 palabras** para mejorar la legibilidad.

### **4️⃣ Eliminación del Archivo de Audio**
- Una vez transcrito el audio, se elimina automáticamente para ahorrar espacio.

---

## ▶️ **Cómo Ejecutar el Script**
1. **Ubica los videos** en la carpeta `video/`.
2. **Ejecuta el script en Python:**
   ```bash
   python script.py
   ```
3. **Los archivos de texto se guardarán en `resumen/`** con el mismo nombre del video original.

---

## 🔧 **Configuraciones Adicionales**
### **Modificar el Modelo de Whisper**
Puedes cambiar la línea donde se carga el modelo:
```python
model = whisper.load_model("medium")  # Cambia a "small" o "large" si lo deseas
```

### **Cambiar la Ubicación de los Archivos**
Si deseas cambiar dónde se guardan los archivos, edita las rutas en `BASE_DIR` y `RESUMEN_DIR`.

---

## 📌 **Ejemplo de Uso**
Si el usuario coloca un video llamado `entrevista.mp4` en `video/`, el proceso será:
1. `entrevista.mp4` → Se convierte a `entrevista.mp3` (guardado temporalmente en `audio/`).
2. `entrevista.mp3` → Se transcribe a `entrevista.txt` (guardado en `resumen/`).
3. `entrevista.mp3` se elimina automáticamente.

Resultado final:
```
📁 videollamadas/
 ├── 📁 video/
 │   ├── entrevista.mp4
 ├── 📁 resumen/
 │   ├── entrevista.txt
```

---

### 📌 **Conclusión**
✅ **Este script es útil para transcribir videos automáticamente** y organiza los archivos en carpetas específicas.  
✅ **Incluye una verificación para evitar procesar archivos duplicados**.  
✅ **Elimina los archivos de audio automáticamente** para optimizar el almacenamiento.  
⚠ **Es necesario cambiar la ruta `BASE_DIR` si otro usuario lo ejecuta en su PC.**  

🚀 **¡Listo! Ahora puedes convertir videos en texto automáticamente.**
