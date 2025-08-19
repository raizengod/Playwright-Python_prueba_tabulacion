# Proyecto de Automatización de Pruebas UI y rendimiento básico con Playwright y Python 🧪

## 🚀 Descripción General
Este proyecto es un framework de automatización de pruebas de interfaz de usuario (UI) robusto y escalable, desarrollado con Playwright y Python, utilizando Pytest como gestor de pruebas. 
Este repositorio contiene un proyecto básico en Python que utiliza la herramienta [Playwright](https://playwright.dev/python/) para realizar pruebas automatizadas de rendimiento en aplicaciones web.

## ✨ Características Principales
El framework incluye una serie de funcionalidades diseñadas para optimizar y enriquecer el proceso de automatización:

* **Tecnología Moderna:** Implementado con Playwright, un framework rápido y confiable para la automatización de navegadores.
* **Lenguaje de Programación:** Desarrollado en Python 3.13.5 (versión recomendada, aunque puede ser compatible con otras versiones de Python 3).
* **Gestión de Pruebas:** Organización y ejecución de casos de prueba con Pytest, aprovechando su sistema de fixtures.
* **Cross-Browser & Responsive Testing:** Soporte para pruebas en Chromium, Firefox y WebKit, incluyendo emulación de dispositivos móviles como iPhone 12 y Pixel 5 para asegurar la compatibilidad y el comportamiento responsivo.
* **Manejo de Elementos y Interacciones:** Funciones globales para:
    * Verificación contenido de una tabla
    * Relleno de campos de texto y numéricos.
    * Interacción con iframes y nuevas ventanas/pestañas.
    * Validación de títulos de página.
* **Gestión de Archivos:** Capacidades para lectura de diversos formatos de datos:
    * Excel (.xlsx)
    * CSV (.csv)
    * JSON (.json)
    * XML
* **Generación de Evidencias:** Capturas de pantalla automáticas en puntos críticos y rutas configurables para almacenamiento de videos y trazas de ejecución.
* **Logging Configurable:** Sistema de logging detallado con niveles de salida separados para consola y archivo, facilitando la depuración y el seguimiento de la ejecución.
* **Organización del Código:** Estructura de proyecto modular que separa locators, páginas y utilidades, promoviendo la reusabilidad y mantenibilidad.
* **Pruebas de Rendimiento Básicas:**
    * **Medición de Tiempos de Carga:** Se han integrado mediciones de tiempo de principio a fin para acciones específicas como Drag and Drop.
    * **Logging de Rendimiento:** Los tiempos de ejecución de operaciones críticas se registran en los logs para su posterior análisis.

## 🛠️ Tecnologías Utilizadas
* **Playwright:** Framework de automatización de navegadores.
* **Python:** Lenguaje de programación.
* **Pytest:** Framework para la gestión y ejecución de pruebas.
* **pytest-html:** Para la generación de informes HTML autocontenidos.
* **Openpyxl:** Librería para manejar archivos .xlsx.
* **CSV:** Módulo para trabajar con archivos .csv.
* **JSON:** Módulo para manejar archivos JSON.
* **xml.etree.ElementTree:** Módulo para trabajar con archivos XML.
* **Logging:** Módulo estándar de Python para el registro de eventos.

## 📂 Estructura del Proyecto
La estructura del proyecto está diseñada para ser clara, modular y fácil de mantener:
```
.
├── Perform/
│   ├── pages/                   # Clases con las funciones de las páginas (lógica)
│   │   ├── base_page.py
│   ├── locator/                 # Clases con los selectores de los elementos
│   │   ├── locator_barraNavegacion.py
│   │   └── locator_ModalDataTable.py
│   ├── utils/                   # Módulos de utilidad
│   │   ├── config.py
│   │   └── logger.py
├── test/
│   ├── archivos/               # Archivos de prueba (ej. para upload/download)
│   │   └── archivos_data_fuente/
│   ├── reportes/               # Directorio para almacenar evidencias de las pruebas
│   │   ├── html/               # Informes HTML
│   │   ├── video/              # Grabaciones de video de las ejecuciones
│   │   ├── traceview/          # Archivos traceview de Playwright
│   │   └── imagen/             # Capturas de pantalla
│   ├── conftest.py              # Fixtures de Pytest para configuraciones globales
│   └── test_ModalDataTable.py   # Archivos de pruebas
├── requirements.txt             # Dependencias del proyecto
└── README.md
```

## ⚙️ Configuración e Instalación
**Clonar el repositorio:**

```bash
git clone https://github.com/raizengod/Playwright-Python_prueba_rendiemiento_basico.git
cd Rendimiento
```

**Crear y activar un entorno virtual (recomendado):**

```bash
python -m venv mv_Rendimiento
.\venv\Scripts\activate
# En Windows
```

```bash
python -m venv mv_Rendimiento
source venv/bin/activate
# En macOS/Linux
```

**Instalar las dependencias:**

```bash
pip install -r requirements.txt
playwright install  # Instala los navegadores necesarios (Chromium, Firefox, WebKit)
# (Asegúrate de que pytest-reporter-html1 esté incluido en requirements.txt)
```

```bash
pip install playwright pytest pytest-html openpyxl
playwright install
```

Asegurar Directorios de Evidencias: El archivo config.py define una función ensure_directories_exist() que crea automáticamente las carpetas necesarias para reportes y archivos de datos. Asegúrate de que esta función se ejecute, o créalas manualmente según la Estructura del Proyecto.

## 🚀 Uso
Para ejecutar las pruebas, asegúrate de estar en el entorno virtual activado y en la raíz del proyecto.

**Ejecución de Pruebas**

1.  **Ejecuta las pruebas y genera los resultados de reporte:**
    ```bash
    pytest Perform\test\test_ModalDataTable.py -s -v --template=html1/index.html --report=reportes/html1/playwright_reporte.html
    ```

2.  **Ejecutar todas las pruebas con Pytest:**
    ```bash
    pytest Perform\test\
    ```

3.  **Ejecutar pruebas específicas (ejemplo):**
    ```bash
    pytest Perform\test\test_ModalDataTable.py
    ```

4.  **Ejecutar todas las pruebas con reporte detallado y genera los resultados en reporte HTML:**:**
    ```bash
    pytest Perform\test\ -s -v --template=html1/index.html --report=reportes/html1/playwright_reporte.html
    ```

5.  **Ejecuta las pruebas en paralelo y genera los resultados de reporte:**
    ```bash
    pytest Perform\test\ -s -v -n 5 --template=html1/index.html --report=reportes/html1/playwright_reporte.html
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
* **Manejo de Datos en Pruebas:** Experiencia en la lectura y escritura de datos de prueba desde/hacia archivos Excel, CSV, JSON y XML.

# 🔮 Mejoras Futuras / Roadmap

Este proyecto es una base sólida, y siempre hay espacio para la mejora continua. Algunas ideas para futuras extensiones incluyen:

* Configurar variables de entorno para la URL base y credenciales, mejorando la seguridad y flexibilidad del framework.
* Extender la cobertura con pruebas de APIs para una validación completa del backend (si aplica).

## Licencia

Este proyecto no tiene una licencia específica declarada. Consulta con el autor para su uso en producción.

## Autor

[Carlos N](https://github.com/raizengod)