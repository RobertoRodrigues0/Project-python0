from playwright.sync_api import sync_playwright#TODO CHAMA BIBLIOTECAS E IMPORTAR 
import pyautogui#TODO IMPORTAR BIBLIOTECA
import datetime
import time
for a in range(2):  #TODO LOOPE PARA INCIAR PROGRAMA E CONTAGEM DE X  A SER FEITA
        with sync_playwright() as p:
            pyautogui.PAUSE = 0.5
            navegador = p.chromium.launch(headless=False)#TODO ABRIR NO CHROMIUM ANONIMO
            page = navegador.new_page()#TODO ABRI NOVO NAVEGADOR
            page.goto("https://www.youtube.com/watch?v=0_rod5TcCAU")#TODO COLOCAR NA URL LINK E IR A CAMINHO DO DESTINO
            page.keyboard.press(' ')#TODO TOCAR O VIDEO NO YOUTUBE
            time.sleep(3)#TODO ESPERAR
            for c in range(3):#TODO LOOPE PARA FECHAR E ABRIR OUTROS BROWSER ISOLADAS, ANONIMAS E CONTAGEM DE X  A SER FEITA
                time.sleep(5)
                page.keyboard.press('Shift+.')#TODO AUMENTAR O VOLUME DE X TEMPO ATÉ O FIM
                time.sleep(6)
time.sleep(90)
