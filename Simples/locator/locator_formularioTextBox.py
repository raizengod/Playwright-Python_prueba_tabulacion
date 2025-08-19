from playwright.sync_api import Page

class FormularioTextBoxLocatorPage:
    
    def __init__(self, page: Page):
        self.page = page
        
    #Selector menú formulario
    @property
    def opcionTextBox(self):
        return self.page.get_by_role("listitem").filter(has_text="Text Box") 
    
    #Selector campo Nombre
    @property
    def campoNombre(self):
        return self.page.get_by_role("textbox", name="Full Name")
    
    #Selector campo Email
    @property
    def campoEmail(self):
        return self.page.get_by_placeholder("name@example.com")
    
    #Selector campo Dirección
    @property
    def campoDireccion(self):
        return self.page.get_by_role("textbox", name="Current Address")
    
    #Selector campo Dirección fija
    @property
    def campoDireccionFija(self):
        return self.page.locator("#permanentAddress")
    
    #Selector botón submit
    @property
    def botonSubmit(self):
        return self.page.get_by_role("button", name="Submit")