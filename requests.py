from playwright.sync_api import sync_playwright#TODO CHAMA BIBLIOTECAS E IMPORTAR
from time import sleep
def event_handler(request_event):
    response = request_event.response()

    print(response.status,' - ', request_event.url)
    print(response.status)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)#TODO ABRIR NO CHROMIUM ANONIMO
    context = browser.new_context(
        color_scheme='light'
    )
    sleep(3)
    page = context.new_page()#TODO ABRI NOVO NAVEGADOR
    page.on('request', event_handler) #todo Quando um request acontecer
    #page.on('open', event_handler)

    page.goto("https:ddg.gg")#TODO COLOCAR NA URL LINK E IR A CAMINHO DO DESTINO
    sleep(3)#TODO ESPERAR

    #breakpoint()
    browser.close()