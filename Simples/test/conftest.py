# nombra el archivo: Ve a la ubicación de tu archivo y colcoar el nombre a conftest.py
# La convención de conftest.py le indica a Pytest que este archivo contiene fixtures que deben estar disponibles 
# para los tests en ese directorio y sus subdirectorios.
import pytest
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from datetime import datetime
import os
from typing import Generator
from Simples.utils import config
from Simples.pages.base_page import Funciones_Globales
from Simples.locator.locator_barraNavegacion import BarraNavLocatorPage
from Simples.locator.locator_formularioDescarga import FormularioDescaraLocatorPage
from Simples.locator.locator_formularioTextBox import FormularioTextBoxLocatorPage

# Función para generar IDs legibles
def generar_ids_browser(param):
    """
    Genera un ID descriptivo para cada combinación de navegador y dispositivo.
    """
    browser = param['browser']
    device = param['device']
    resolution = param['resolution']

    if device:
        return f"{browser}-{device}"
    else:
        return f"{browser}-{resolution['width']}x{resolution['height']}"

@pytest.fixture(
    scope="function",
    params=[
            # Resoluciones de escritorio
            {"browser": "chromium", "resolution": {"width": 1920, "height": 1080}, "device": None},
            {"browser": "firefox", "resolution": {"width": 1920, "height": 1080}, "device": None},
            {"browser": "webkit", "resolution": {"width": 1920, "height": 1080}, "device": None},
            # Emulación de dispositivos móviles
            {"browser": "chromium", "device": "iPhone 12", "resolution": None},
            {"browser": "webkit", "device": "Pixel 5", "resolution": None}
    ],
    ids=generar_ids_browser # <--- Usar la función para generar IDs
)
def playwright_page(playwright: Playwright, request) -> Generator[Page, None, None]:
    """
    Fixture base para configurar el navegador, contexto y página de Playwright con configuraciones comunes.
    Maneja el lanzamiento del navegador, la creación del contexto (con grabación de video y emulación de dispositivos),
    el rastreo (tracing) y la navegación de la página a una URL específica. También renombra el archivo de video al finalizar.
    """
    param = request.param
    browser_type = param["browser"]
    resolution = param["resolution"]
    device_name = param["device"]

    browser_instance = None
    context = None
    page = None

    try:
        if browser_type == "chromium":
            browser_instance = playwright.chromium.launch(headless=True, slow_mo=500)
        elif browser_type == "firefox":
            browser_instance = playwright.firefox.launch(headless=True, slow_mo=500)
        elif browser_type == "webkit":
            browser_instance = playwright.webkit.launch(headless=True, slow_mo=500)
        else:
            raise ValueError(f"\nEl tipo de navegador '{browser_type}' no es compatible.")

        context_options = {
            "record_video_dir": config.VIDEO_DIR,
            "record_video_size": {"width": 1920, "height": 1080}
        }

        if device_name:
            device = playwright.devices[device_name]
            context = browser_instance.new_context(**device, **context_options)
        elif resolution:
            context = browser_instance.new_context(viewport=resolution, **context_options)
        else:
            context = browser_instance.new_context(**context_options)

        page = context.new_page()

        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        trace_name_suffix = ""
        if device_name:
            trace_name_suffix = device_name.replace(" ", "_").replace("(", "").replace(")", "")
        elif resolution:
            trace_name_suffix = f"{resolution['width']}x{resolution['height']}"

        trace_file_name = f"traceview_{current_time}_{browser_type}_{trace_name_suffix}.zip"
        trace_path = os.path.join(config.TRACEVIEW_DIR, trace_file_name)

        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield page

    finally:
        if context:
            context.tracing.stop(path=trace_path)
            context.close()
            
        if browser_instance:
            browser_instance.close()
            
        if page and page.video:
            video_path = page.video.path()
            new_video_name = datetime.now().strftime("%Y%m%d-%H%M%S") + ".webm"
            new_video_path = os.path.join(config.VIDEO_DIR, new_video_name)
            try:
                os.rename(video_path, new_video_path)
                print(f"\nVideo guardado como: {new_video_path}")
            except Exception as e:
                print(f"\nError al renombrar el video: {e}")

@pytest.fixture(scope="function")
def set_up_Descarga(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "Descargar archivo"
    """
    # Espera a que el DOM de la página se cargue antes de continuar
    playwright_page.goto(config.BASE_URL, wait_until="domcontentloaded")
    playwright_page.set_default_timeout(10000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)
    fdl = FormularioDescaraLocatorPage(playwright_page)
    
    # Espera a que el selector del menú de formulario sea visible usando .wait_for()
    bnl.opcionFormulario.wait_for()
    
    fg.hacer_click_en_elemento(bnl.opcionFormulario, "clic_menu_formulario", config.SCREENSHOT_DIR, None, 1)
    
    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.scroll_pagina(0, 20)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")
        
    # Espera a que el elemento del Text Box sea visible antes de hacer clic
    fdl.opcionDescarga.wait_for()
    fg.hacer_click_en_elemento(fdl.opcionDescarga, "hacer_click_en_elemento_menú_formulario_descarga", config.SCREENSHOT_DIR, None, 1)
    
    fg.validar_url_actual(".*/upload-download")
    fg.validar_titulo_de_web("DEMOQA", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    
    yield playwright_page
    
@pytest.fixture(scope="function")
def set_up_Tabulacion(playwright_page: Page) -> Generator[Page, None, None]:
    """
    Fixture para pruebas que interactúan con la funcionalidad "Text Box"
    """
    # Espera a que el DOM de la página se cargue antes de continuar
    playwright_page.goto(config.BASE_URL, wait_until="domcontentloaded")
    playwright_page.set_default_timeout(10000)
    
    fg = Funciones_Globales(playwright_page)
    bnl = BarraNavLocatorPage(playwright_page)
    tbl = FormularioTextBoxLocatorPage(playwright_page)
    
    # Espera a que el selector del menú de formulario sea visible usando .wait_for()
    bnl.opcionFormulario.wait_for()
    
    fg.hacer_click_en_elemento(bnl.opcionFormulario, "clic_menu_formulario", config.SCREENSHOT_DIR, None, 1)
    
    ancho_viewport = playwright_page.viewport_size['width']
    if ancho_viewport <= 768:
        fg.scroll_pagina(0, 20)
    else:
        fg.logger.info(f"Detectada resolución de escritorio ({ancho_viewport}px). No se hace clic en el menú hamburguesa.")
    
    # Espera a que el elemento del Text Box sea visible antes de hacer clic
    tbl.opcionTextBox.wait_for()
    fg.hacer_click_en_elemento(tbl.opcionTextBox, "hacer_click_en_elemento_menú_formulario_texBox", config.SCREENSHOT_DIR, None, 1)
    
    fg.validar_url_actual(".*/text-box")
    fg.validar_titulo_de_web("DEMOQA", "validar_titulo_de_web", config.SCREENSHOT_DIR)
    
    yield playwright_page