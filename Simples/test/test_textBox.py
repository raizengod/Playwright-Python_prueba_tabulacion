import random
import pytest
import re
import os
import time
from playwright.sync_api import expect
from Simples.pages.base_page import Funciones_Globales
from Simples.locator.locator_formularioTextBox import FormularioTextBoxLocatorPage
from Simples.utils import config

def test_verificar_orden_tabulacion(set_up_Tabulacion):
    """
    Objetivo: Verificar que la tabulación (tecla Tab) en el formulario de texto
    sigue el orden correcto de los elementos.

    Pasos de la prueba:
    1. Obtener la instancia de la página de Playwright desde el fixture.
    2. Inicializar los objetos de las clases de acciones y localizadores.
    3. Enfocar el primer elemento del formulario (campo de nombre).
    4. Presionar la tecla 'Tab' y verificar que el foco se mueva correctamente
       al siguiente campo, repitiendo el proceso para cada elemento en el
       orden esperado.
    """
    # 1. Inicializa el objeto 'page' de Playwright a partir del fixture.
    page = set_up_Tabulacion

    # 2. Instancia la clase de funciones globales para las acciones y
    # la clase de localizadores para acceder a los selectores.
    fg = Funciones_Globales(page)
    ftb = FormularioTextBoxLocatorPage(page)
    
    # 3. Enfocar el primer elemento de la secuencia de tabulación.
    #    Esto establece el punto de partida para la prueba.
    fg.hacer_focus_en_elemento(ftb.campoNombre, "hacer_focus_en_elemento_campo_nombre", config.SCREENSHOT_DIR)
    
    # 4. Presionar 'Tab' y verificar el foco para cada elemento.
    #    - Se espera que el foco se mueva del campoNombre al campoEmail.
    fg.presionar_Tab_y_verificar_foco(ftb.campoEmail, "presionar_Tab_y_verificar_foco_campo_email", config.SCREENSHOT_DIR)
    
    #    - Se espera que el foco se mueva del campoEmail al campoDireccion.
    fg.presionar_Tab_y_verificar_foco(ftb.campoDireccion, "presionar_Tab_y_verificar_foco_campo_direccion", config.SCREENSHOT_DIR)
    
    #    - Se espera que el foco se mueva del campoDireccion al campoDireccionFija.
    fg.presionar_Tab_y_verificar_foco(ftb.campoDireccionFija, "presionar_Tab_y_verificar_foco_campo_direccion_fija", config.SCREENSHOT_DIR)
    
    #    - Finalmente, se espera que el foco se mueva del campoDireccionFija al botonSubmit.
    fg.presionar_Tab_y_verificar_foco(ftb.botonSubmit, "presionar_Tab_y_verificar_foco_boton_submit", config.SCREENSHOT_DIR)

def test_verificar_orden_inverso_tabulacion(set_up_Tabulacion):
    """
    Objetivo: Verificar que la tabulación inversa (teclas Shift + Tab) en el formulario
    de texto funciona correctamente y el foco se mueve al elemento anterior.

    Pasos de la prueba:
    1. Obtener la instancia de la página de Playwright desde el fixture.
    2. Inicializar los objetos de las clases de acciones y localizadores.
    3. Enfocar el último elemento de la secuencia (el botón de envío).
    4. Presionar la combinación de teclas 'Shift + Tab' y verificar que el foco
       se mueva al elemento anterior, repitiendo el proceso en el orden inverso
       al esperado para la tabulación normal.
    """
    # 1. Inicializa el objeto 'page' de Playwright a partir del fixture.
    page = set_up_Tabulacion

    # 2. Instancia la clase de funciones globales para las acciones y
    # la clase de localizadores para acceder a los selectores.
    fg = Funciones_Globales(page)
    ftb = FormularioTextBoxLocatorPage(page)
    
    # 3. Enfocar el último elemento de la secuencia para comenzar la prueba de tabulación inversa.
    fg.hacer_focus_en_elemento(ftb.botonSubmit, "hacer_focus_en_elemento_boton_submit", config.SCREENSHOT_DIR)
    
    # 4. Presionar 'Shift + Tab' y verificar el foco para cada elemento en orden inverso.
    #    - Se espera que el foco se mueva del botonSubmit al campoDireccionFija.
    fg.presionar_Shift_Tab_y_verificar_foco(ftb.campoDireccionFija, "presionar_Shift_Tab_y_verificar_foco_campo_direccion_fija", config.SCREENSHOT_DIR)
    
    #    - Se espera que el foco se mueva del campoDireccionFija al campoDireccion.
    fg.presionar_Shift_Tab_y_verificar_foco(ftb.campoDireccion, "presionar_Shift_Tab_y_verificar_foco_campo_direccion", config.SCREENSHOT_DIR)
    
    #    - Se espera que el foco se mueva del campoDireccion al campoEmail.
    fg.presionar_Shift_Tab_y_verificar_foco(ftb.campoEmail, "presionar_Shift_Tab_y_verificar_foco_campo_email", config.SCREENSHOT_DIR)
    
    #    - Finalmente, se espera que el foco se mueva del campoEmail al campoNombre.
    fg.presionar_Shift_Tab_y_verificar_foco(ftb.campoNombre, "presionar_Shift_Tab_y_verificar_foco_campo_nombre", config.SCREENSHOT_DIR)