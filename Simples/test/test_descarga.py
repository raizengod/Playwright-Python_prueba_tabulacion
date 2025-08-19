import random
import pytest
import re
import os
import time
from playwright.sync_api import expect
from Simples.pages.base_page import Funciones_Globales
from Simples.locator.locator_formularioDescarga import FormularioDescaraLocatorPage
from Simples.utils import config

def test_DecargarArchivo(set_up_Descarga):
    """
    Prueba de extremo a extremo para la funcionalidad de descarga de un archivo.

    Esta prueba sigue los siguientes pasos:
    1. Navega a la página de 'Upload and Download' (gestionado por el fixture 'set_up_Descarga').
    2. Localiza el botón de descarga en la página.
    3. Llama a la función genérica para hacer clic en el botón y gestionar la descarga del archivo.
    4. El archivo descargado se guarda en el directorio especificado.
    5. Se valida que la operación de descarga se complete exitosamente.

    Args:
        set_up_Descarga (Page): Objeto de página de Playwright, proporcionado por el fixture
                                'set_up_Descarga', que ya ha navegado a la URL inicial del
                                formulario de carga y descarga.
    """
    
    # Inicializa el objeto 'page' de Playwright a partir del fixture.
    page = set_up_Descarga

    # Instancia de la clase Funciones_Globales para acceder a métodos genéricos de
    # interacción con la interfaz de usuario (validaciones, clics, descargas, etc.).
    fg = Funciones_Globales(page)
    
    # Instancia de la clase FormularioDescaraLocatorPage para acceder a los localizadores
    # específicos de los elementos de la página de descarga.
    fdl = FormularioDescaraLocatorPage(page)
    
    # Llama a la función para descargar un archivo.
    # Se le pasa el localizador del botón de descarga, el nombre base para capturas,
    # el directorio de capturas y el directorio de destino para el archivo.
    fg.descargar_archivo(fdl.botonDescargar, "descargar_archivo", config.SCREENSHOT_DIR, config.SOURCE_FILES_DIR_DOWNLOAD)