import pyautogui
import webbrowser
from time import sleep

webbrowser.open("https://adsmanager.facebook.com/adsmanager/audiences?act=1016012996344421&business_id=425651638967424&tool=AUDIENCES&nav_entry_point=ads_ecosystem_navigation_menu&nav_source=ads_manager&breakdown_regrouping=0&date=2023-10-16_2023-10-17%2Cyesterday")
sleep(10)
#Clique no Público selecionado
pyautogui.click(550,287)
sleep(6)
#---------------
#Edição do Público Selecionado
pyautogui.click(1283,618)
sleep(5)
#--------------- Escolher Preenchimento de qual videos porcentagem 25%
pyautogui.click(1250,340)
sleep(5)
#--------------- Escolha do Instagram
pyautogui.click(750,210)
sleep(7)
#--------------- Instagram
pyautogui.click(557, 294)
sleep(7)
#cliquei baixar scroll
pyautogui.doubleClick(1550, 968)
sleep(4)
#pyautogui.click(1550, 977)
sleep(5)
#---------------
#pyautogui.click(434, 788)
sleep(1)
#---------------
for b in range(2):
    for i in range(1):
        pyautogui.click(429, 966)
        sleep(2)
        pyautogui.click(428, 848)
        sleep(2)
        pyautogui.click(429, 720)
        sleep(2)
        pyautogui.click(428, 591)
        sleep(2)
        pyautogui.click(428, 465)
        sleep(2)
        pyautogui.click(429, 337)
        sleep(2)
        # Mudar a aba de escolha de videos
        pyautogui.click(1166, 179)
        sleep(4)
#----------------------
#salvar videos
pyautogui.click(1494, 1011)
sleep(4)
breakpoint()
#----------------------
#------------------
# clique fora
#pyautogui.click(1347, 514)
#sleep(3)
#------------------
# Botão  Escolha Dias
#pyautogui.click(697, 577)
#sleep(3)
#----------------
#pyautogui.keyDown('ctrl')
#sleep(2)
#pyautogui.press('a')
#sleep(2)
#pyautogui.keyUp('ctrl')
#-------------------------
#pyautogui.write('14')
#sleep(3)
# Botão nome do público
#pyautogui.click(740, 663)
#sleep(6)
#pyautogui.write('14 DIAS  (25%,50%,75% 95%) - VIEW ALL VIDEO')
#sleep(3)
#---------------------
# Botão Criar público
#pyautogui.click(1267, 741)
sleep(4)
# Botão Criar público
#pyautogui.click(1301, 803)
#sleep(6)
