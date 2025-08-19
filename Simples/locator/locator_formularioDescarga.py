from playwright.sync_api import Page

class FormularioDescaraLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector menú hamburguesa en formulario
    @property
    def opcionDescarga(self):
        return self.page.get_by_role("listitem").filter(has_text="Upload and Download")
    
    #Selector menú hamburguesa en formulario
    @property
    def botonDescargar(self):
        return self.page.get_by_role("link", name= "Download")