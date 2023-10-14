from playwright.sync_api import sync_playwright
from time import sleep
for a in range(2): #todo for python abrir páginas do navegador
        with sync_playwright() as p:
            sleep(5)
            navegador = p.chromium.launch(headless=False)
            page = navegador.new_page()
            page.goto("https://www.youtube.com/watch?v=0_rod5TcCAU")
            page.keyboard.press(' ')
            sleep(189)
            #for c in range(4):#todo for python aumentar o volume
                #sleep(5)
                #page.keyboard.press('Shift+.')
                #sleep(6)
            #breakpoint()
            page.close()