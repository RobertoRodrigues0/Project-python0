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
pyautogui.click(166, 237)
sleep(5)
#-----------
# Botão SELEÇÃO DE PUBLICO Conta do Instagram -3
pyautogui.click(971, 512)
sleep(3)
# Botão Avançar -4
pyautogui.click(1252, 763)
sleep(7)
#-----------
#Botão Escolher Opção Instagram -5
pyautogui.click(1207, 345)
sleep(2)
#Botão Seleçao Instagram -6
pyautogui.click(717, 458)
sleep(2)
#------------------
#Botão Eventos -7
pyautogui.click(1207, 419)
sleep(3)
#------------------
#Botão Seleção Eventos (SEGUIR ESSA CONTA PROFISSIONAL) -8
pyautogui.click(716, 500)
sleep(3)
#------------------

#-----Manutenção--------
#pyautogui.moveTo(1488, 1015, 1)
#sleep(10)
#breakpoint()


# Botão  ESCOLHER NOME -9
pyautogui.click(700, 613)
sleep(4)
#-------------------------

#NOME DO PÚBLICO -10
pyautogui.write('[SEGUIDORES]')
#ENGAJAMENTO
#VISITAS
#SEGUIDORES
#MENSAGENS
sleep(2)
#------------------
#salvar videos
#Botão Criar Público
pyautogui.click(1180, 786)
sleep(1)
#------------------
breakpoint()