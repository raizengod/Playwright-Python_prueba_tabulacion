# Proyecto de Automatización de Pruebas UI simples con Playwright y Python 🧪

## 🚀 Descripción General
Este proyecto es un framework de automatización de pruebas de interfaz de usuario (UI) desarrollado con [Playwright](https://playwright.dev/python/) y Python, utilizando Pytest como gestor de pruebas. Su objetivo principal es verificar el comportamiento de un formulario de texto con simulación de interacción con el teclado y la funcionalidad de descarga de archivos. El framework está diseñado para ser modular y escalable, con una estructura de código clara que facilita la reusabilidad y el mantenimiento.

## ✨ Características Principales
El framework incluye una serie de funcionalidades diseñadas para optimizar y enriquecer el proceso de automatización:

* **Tecnología Moderna:** Implementado con Playwright, un framework rápido y confiable para la automatización de navegadores.
* **Lenguaje de Programación:** Desarrollado en Python 3.13.5 (versión recomendada, aunque puede ser compatible con otras versiones de Python 3).
* **Gestión de Pruebas:** Organización y ejecución de casos de prueba con Pytest, aprovechando su sistema de fixtures.
* **Cross-Browser & Responsive Testing:** Soporte para pruebas en Chromium, Firefox y WebKit, incluyendo emulación de dispositivos móviles como iPhone 12 y Pixel 5 para asegurar la compatibilidad y el comportamiento responsivo.
* **Manejo de Elementos y Interacciones:** Funciones globales para:
    * Verificar el orden de tabulación en un formulario (tecla Tab).
    * Verificar la tabulación inversa (teclas Shift + Tab).
    * Hacer clic en elementos.
    * Validar la URL y el título de la página.
    * Gestionar la descarga de archivos y verificar que la operación se complete exitosamente.
* **Generación de Evidencias:** 
    * Capturas de pantalla automáticas en puntos críticos, con rutas configurables para almacenamiento.
    * Grabaciones de video de las ejecuciones de las pruebas.
    * Archivos de traza de Playwright (traceview) para un análisis detallado de la ejecución.
* **Organización del Código:** Estructura de proyecto modular que separa localizadores (locator), lógica de página (pages) y utilidades (utils), promoviendo la reusabilidad y mantenibilidad.
* **Logging Configurable:** Sistema de logging detallado con niveles de salida separados para consola y archivo, facilitando la depuración y el seguimiento de la ejecución.
* **Fixtures Reutilizables:** Utilización de conftest.py para definir fixtures que configuran la página de Playwright y navegan a la URL de prueba, reduciendo la duplicación de código en los tests.

## 🛠️ Tecnologías Utilizadas
* **Playwright:** Framework de automatización de navegadores.
* **Python:** Lenguaje de programación.
* **Pytest:** Framework para la gestión y ejecución de pruebas.
* **os:** Módulo estándar de Python para interactuar con el sistema operativo (e.g., renombrar archivos).
* **datetime:** Módulo para manejar fechas y horas, usado para generar nombres de archivos únicos.

## 📂 Estructura del Proyecto
La estructura del proyecto está diseñada para ser clara, modular y fácil de mantener:
```
.
├── Simples/
│   ├── pages/                   # Clases con las funciones de las páginas (lógica)
│   │   ├── base_page.py
│   ├── locator/                 # Clases con los selectores de los elementos
│   │   ├── locator_barraNavegacion.py
│   │   ├── locator_formularioDescarga.py
│   │   └── locator_formularioTextBox.py
│   ├── utils/                   # Módulos de utilidad
│   │   ├── config.py
│   │   └── logger.py
├── test/
│   ├── conftest.py                 # Fixtures de Pytest para configuraciones globales
│   ├── test_descarga.py            # Pruebas para la funcionalidad de descarga de archivos
│   ├── test_textBox.py             # Pruebas para la funcionalidad de tabulación en el formulario
│   └── reportes/               # Directorio para almacenar evidencias de las pruebas
│       ├── html/               # Informes HTML
│       ├── video/              # Grabaciones de video de las ejecuciones
│       ├── traceview/          # Archivos traceview de Playwright
│       └── imagen/             # Capturas de pantalla
├── requirements.txt             # Dependencias del proyecto
└── README.md
```

## ⚙️ Configuración e Instalación
**Clonar el repositorio:**

```bash
git clone https://github.com/raizengod/Playwright-Python_prueba_tabulacion.git
cd EjemplosSimples
```

**Crear y activar un entorno virtual (recomendado):**

```bash
python -m venv mv_EjSimples
.\venv\Scripts\activate
# En Windows
```

```bash
python -m venv mv_EjSimples
source venv/bin/activate
# En macOS/Linux
```

**Instalar las dependencias:**

```bash
pip install -r requirements.txt
playwright install  # Instala los navegadores necesarios (Chromium, Firefox, WebKit)
# (Asegúrate de que pytest-reporter-html1 esté incluido en requirements.txt)
```

Asegurar Directorios de Evidencias: El archivo config.py define una función ensure_directories_exist() que crea automáticamente las carpetas necesarias para reportes y archivos de datos. Asegúrate de que esta función se ejecute, o créalas manualmente según la Estructura del Proyecto.

## 🚀 Uso
Para ejecutar las pruebas, asegúrate de estar en el entorno virtual activado y en la raíz del proyecto.

**Ejecución de Pruebas**

1.  **Ejecuta las pruebas y genera los resultados de reporte:**
    ```bash
    pytest Simples\test\test_descarga.py -s -v --template=html1/index.html --report=reportes/html1/playwright_reporte.html
    ```

2.  **Ejecutar todas las pruebas con Pytest:**
    ```bash
    pytest Simples\test\
    ```

3.  **Ejecutar pruebas específicas (ejemplo):**
    ```bash
    pytest Simple\test\test_textBox.py
    ```

4.  **Ejecutar todas las pruebas con reporte detallado y genera los resultados en reporte HTML:**:**
    ```bash
    pytest Simples\test\ -s -v --template=html1/index.html --report=reportes/html1/playwright_reporte.html
    ```

5.  **Ejecuta las pruebas en paralelo y genera los resultados de reporte:**
    ```bash
    pytest Simples\test\ -s -v -n 3 --template=html1/index.html --report=reportes/html1/playwright_reporte.html
    ```

## 📊 Integración de Pruebas de Rendimiento
El framework ha sido mejorado para incluir la medición del rendimiento en operaciones críticas. En la clase Funciones_Globales (en base_page.py), se han añadido puntos de medición que registran el tiempo de ejecución de acciones complejas como "Drag and Drop manual" y los escriben en el log.

**Ejemplo de Salida de Log**
```bash
# Ejemplo para la operación de rellenado de texto
INFO - Rellenando campo con selector '#username' con el texto: 'usuario_demo'.
...
INFO - PERFORMANCE: Tiempo que tardó en rellenar el campo '#username': 0.0567 segundos.
...
INFO - ✔ ÉXITO: Campo '#username' rellenado con éxito con el texto: 'usuario_demo'.
```
Estas mediciones permiten a los QA y desarrolladores identificar cuellos de botella y regresiones de rendimiento a medida que el proyecto evoluciona.

## 📈 Reportes y Evidencias

Todas las evidencias generadas durante la ejecución de las pruebas se almacenarán en el directorio test/reportes/:
* test/reportes/html/: Contiene los informes HTML de Pytest.
* test/reportes/video/: Videos de la ejecución de las pruebas (si están configurados en conftest.py).
* test/reportes/traceview/: Archivos de traza de Playwright para análisis detallado.
* test/reportes/imagen/: Capturas de pantalla tomadas durante la ejecución.

## 📈 Integración Continua (CI)

El proyecto está configurado con **GitHub Actions** para ejecutar las pruebas automáticamente en cada push a la rama principal y en cada pull request. El archivo de configuración se encuentra en `.github/workflows/playwright.yml`. Esto garantiza que cualquier cambio en el código se valide rápidamente, detectando regresiones de manera temprana.

## ✅ Habilidades Demostradas

A través de este proyecto, demuestro las siguientes habilidades clave en QA Automation:

* **Diseño de Frameworks de Automatización:** Implementación de una estructura de proyecto modular y escalable utilizando el patrón Page Object Model (POM).
* **Automatización de Pruebas End-to-End:** Creación de escenarios de prueba realistas que cubren flujos de usuario completos.
* **Uso Avanzado de Playwright:** Experiencia profunda en la interacción con elementos web, manejo de aserciones robustas, gestión de contextos de navegador, emulación de dispositivos y configuración de pruebas con Playwright.
* **Programación en Python:** Habilidad para escribir código limpio, legible y eficiente para la automatización, aplicando principios de diseño de software.
* **Integración Continua (CI):** Configuración y mantenimiento de pipelines de CI con GitHub Actions para una ejecución de pruebas automatizada y recurrente, esencial en el ciclo de vida del desarrollo de software.
* **Identificación y Reporte de Bugs:** Capacidad para diseñar pruebas que revelen defectos y, en un entorno de trabajo real, reportarlos adecuadamente con evidencia relevante.
* **Mantenibilidad de Código:** Organización del código para facilitar futuras actualizaciones y extensiones de las pruebas, promoviendo la colaboración y escalabilidad a largo plazo.
* **Pruebas de Funcionalidad Específica:** Enfoque en la verificación de funcionalidades clave como el orden de los elementos al usar la tecla Tab, lo cual es crucial para la accesibilidad y la experiencia del usuario.

# 🔮 Mejoras Futuras / Roadmap

Este proyecto es una base sólida, y siempre hay espacio para la mejora continua. Algunas ideas para futuras extensiones incluyen:

* Configurar variables de entorno para la URL base y credenciales, mejorando la seguridad y flexibilidad del framework.
* Extender la cobertura con pruebas de APIs para una validación completa del backend (si aplica).

## Licencia

Este proyecto no tiene una licencia específica declarada. Consulta con el autor para su uso en producción.

## Autor

[Carlos N](https://github.com/raizengod)