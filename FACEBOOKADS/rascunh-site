
from playwright.sync_api import sync_playwright#TODO CHAMA BIBLIOTECAS E IMPORTAR
from time import sleep
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)#TODO ABRIR NO CHROMIUM ANONIMO
    context = browser.new_context(
        color_scheme='light'
    )
    sleep(3)
    page = context.new_page()#TODO ABRI NOVO NAVEGADOR
    page.goto("https://google.com")#TODO COLOCAR NA URL LINK E IR A CAMINHO DO DESTINO
    sleep(3)#TODO ESPERAR
    #breakpoint()
    browser.close()