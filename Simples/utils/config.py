import os

# Obtiene la ruta absoluta del directorio donde se encuentra este archivo config.py
# Esto resultará en algo como '.../PRACTICA-RV/PRV/utils'
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Navega un nivel arriba para llegar a la raíz de tu paquete principal 'practice'
# CURRENT_DIR = '.../PRACTICA-RV/PRV/utils'
# os.path.dirname(CURRENT_DIR) = '.../PRACTICA-RV/PRV'
PROJECT_ROOT = os.path.dirname(CURRENT_DIR) 

# --- Configuración de URLs ---
BASE_URL = "https://demoqa.com"
#FORM_URL = "https://validaciones.rodrigovillanueva.com.mx"

# --- Rutas de Almacenamiento de Evidencias ---

# Directorio base donde se guardarán todas las evidencias.
# Construye la ruta absoluta para que apunte a '.../PRACTICA-RV/PRV/test/reportes'
EVIDENCE_BASE_DIR = os.path.join(PROJECT_ROOT, "test", "reportes")

# Ruta para videos.
# Se creará '.../PRACTICA-RV/PRV/test/reportes/video'
VIDEO_DIR = os.path.join(EVIDENCE_BASE_DIR, "video")

# Ruta para traceview.
# Se creará '.../PRACTICA-RV/PRV/test/reportes/traceview'
TRACEVIEW_DIR = os.path.join(EVIDENCE_BASE_DIR, "traceview")

# Ruta para capturas de pantalla.
# Se creará '.../PRACTICA-RV/PRV/test/reportes/imagen'
SCREENSHOT_DIR = os.path.join(EVIDENCE_BASE_DIR, "imagen")

# Ruta para logger.
# Se creará '.../PRACTICA-RV/PRV/test/reportes/log'
LOGGER_DIR = os.path.join(EVIDENCE_BASE_DIR, "log")

# --- Nueva ruta para archivos fuente ---
# Se creará '.../PRACTICA-RV/PRV/test/archivos_data_escritura'
SOURCE_FILES_DIR_DATA_ESCRITURA = os.path.join(PROJECT_ROOT, "test", "archivos", "archivos_data_fuente")

# Se creará '.../PRACTICA-RV/PRV/test/archivos_data_fuente'
SOURCE_FILES_DIR_DATA_FUENTE = os.path.join(PROJECT_ROOT, "test", "archivos", "archivos_data_fuente")

# Se creará '.../PRACTICA-RV/PRV/test/archivos_upload'
SOURCE_FILES_DIR_UPLOAD = os.path.join(PROJECT_ROOT, "test", "archivos", "archivos_upload")

# Se creará '.../PRACTICA-RV/PRV/test/archivos_download'
SOURCE_FILES_DIR_DOWNLOAD = os.path.join(PROJECT_ROOT, "test", "archivos", "archivos_download")

# Función para asegurar que los directorios existan
def ensure_directories_exist():
    """
    Crea los directorios necesarios si no existen.
    """
    os.makedirs(VIDEO_DIR, exist_ok=True)
    os.makedirs(TRACEVIEW_DIR, exist_ok=True)
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    os.makedirs(SOURCE_FILES_DIR_DATA_ESCRITURA, exist_ok=True)
    os.makedirs(SOURCE_FILES_DIR_DATA_FUENTE, exist_ok=True)
    os.makedirs(SOURCE_FILES_DIR_UPLOAD, exist_ok=True)
    os.makedirs(SOURCE_FILES_DIR_DOWNLOAD, exist_ok=True)
    os.makedirs(LOGGER_DIR, exist_ok=True)
    print(f"Directorios verificados/creados: {EVIDENCE_BASE_DIR}, \
        {SOURCE_FILES_DIR_UPLOAD}, \
            {SOURCE_FILES_DIR_DOWNLOAD}, \
                {LOGGER_DIR}, \
                    {SOURCE_FILES_DIR_DATA_FUENTE}, \
                        {SOURCE_FILES_DIR_DATA_ESCRITURA}")


# Llama a la función para asegurar que los directorios se creen al importar este módulo
ensure_directories_exist()