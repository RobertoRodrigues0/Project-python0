import pyautogui
import webbrowser
from time import sleep
webbrowser.open("https://adsmanager.facebook.com/adsmanager/audiences?act=1280056725926362&business_id=1016433562658262&tool=AUDIENCES&nav_entry_point=ads_ecosystem_navigation_menu&nav_source=ads_manager&breakdown_regrouping=1&date=2023-05-08_2024-02-14%2Cmaximum")
sleep(15)
#Botão Criar público -1
pyautogui.click(142, 191)
sleep(3)
#-----------
# Botão Público personalizado -2
pyautogui.click(159, 285)
sleep(5)
#-----------
# Botão SELEÇÃO DE PUBLICO Conta do Instagram  (total seguindo)-3
pyautogui.click(759, 308)
sleep(3)
#--------------------
pyautogui.click('887, 354')
sleep(5)
breakpoint()
#----------------------
#ESCREVER NOME DO PUBLICO LAL
pyautogui.write('TODOS SEGUIDORES')
sleep(10)
#----------------------

pyautogui.click('724, 388')
#----------------------

pyautogui.click('706, 440')
sleep(3)
pyautogui.write('Brasil')
sleep(3)
pyautogui.click('746, 485')
sleep(3)
pyautogui.click('938, 333')
sleep(3)
#----------------------
# Selecionar porcentagem
pyautogui.click('676, 557')
#----------------------
pyautogui.click('661, 776')
#----------------------

pyautogui.click('1224, 940')
#----------------------

#-----Manutenção--------
#pyautogui.moveTo(1488, 1015, 1)
#sleep(10)
#breakpoint()




