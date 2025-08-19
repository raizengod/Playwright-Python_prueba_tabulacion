from playwright.sync_api import Page
import re # Importa el módulo de expresiones regulares

class BarraNavLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector menú hamburguesa en formulario
    @property
    def opcionFormulario(self):
        return self.page.locator("div").filter(has_text=re.compile(r"^Elements$")).nth(1)