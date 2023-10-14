from time import sleep
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    #iphone = p.devices['iPhone 6']#todo Escolher qual dispositivos quer ver
    sleep(3)
    context = browser.new_context(
        color_scheme='light',
        #**iphone#todo ativa a tela escolhida
        #record_video_dir='.',todo gravar a tela
        #viewport={'width': 100, 'height': 100},todo tamanho do browser


    )
    sleep(3)
    page = context.new_page()
    sleep(3)
    page.goto("https://dgg.gg")
    #sleep(3)
    #page.go_back()#todo voltar a página
    #sleep(3)
    #page.go_forward()#todo ir para a frente da página
    #sleep(3)
    #page.screenshot(path="screenshot.png", full_page=True)todo tirar print da tela
    print(page.title())
    sleep(3)
    #breakpoint()
    browser.close()
