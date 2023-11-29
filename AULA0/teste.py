import pyautogui
import webbrowser
from time import sleep
webbrowser.open("https://adsmanager.facebook.com/adsmanager/audiences?act=1016012996344421&business_id=425651638967424&tool=AUDIENCES&nav_entry_point=ads_ecosystem_navigation_menu&nav_source=ads_manager&breakdown_regrouping=0&date=2023-10-16_2023-10-17%2Cyesterday")
sleep(10)
#Botão Criar público
pyautogui.click(142, 191)
sleep(10)
# Botão Público personalizado
pyautogui.click(165, 240)
sleep(6)
# Botão Vídeo
pyautogui.click(721, 511)
sleep(6)
# Botão Avançar
pyautogui.click(1249, 760)
sleep(6)
# Botão  Engajamento  Escolha um tipo de contéudo
pyautogui.click(1299, 372)
sleep(3)
# Botão 25%
pyautogui.click(800, 522)
sleep(1)
# Botão 50%
pyautogui.click(718, 618)
sleep(1)
# Botão 75%
pyautogui.click(709, 675)
sleep(1)
# Botão 95%
pyautogui.click(758, 737)
sleep(1)
#------------------
# clique fora
pyautogui.click(1347, 514)
sleep(3)
#------------------
# Botão  Escolha Dias
pyautogui.click(697, 577)
sleep(3)
#----------------
pyautogui.keyDown('ctrl')
sleep(2)
pyautogui.press('a')
sleep(2)
pyautogui.keyUp('ctrl')
#-------------------------
pyautogui.write('14')
sleep(3)
# Botão nome do público
pyautogui.click(740, 663)
sleep(6)
pyautogui.write('14 DIAS  (25%,50%,75% 95%) - VIEW ALL VIDEO')
sleep(3)
