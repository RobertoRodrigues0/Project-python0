import pyautogui
import webbrowser
from time import sleep
webbrowser.open("https://adsmanager.facebook.com/adsmanager/audiences?act=1739738786499164&business_id=220249320645011&global_scope_id=220249320645011&breakdown_regrouping=1")
sleep(25)
#Botão Criar público
pyautogui.click(142, 191)
sleep(3)
#-----------
# Botão Público personalizado
pyautogui.click(166, 237)
sleep(5)
#-----------
#-----------
# Botão Conta do Instagram
pyautogui.click(971, 512)
sleep(1)

# Botão Avançar
pyautogui.click(1249, 760)
sleep(1)
#-----------


#Botão escolha de Público Instagram
pyautogui.click(1207, 411)
sleep(3)
#Botão Seleçao de Público
pyautogui.click(873, 656)
sleep(1)

#------------------




# Botão  Escolha Dias
pyautogui.click(758, 485)
sleep(4)
#----------------
pyautogui.keyDown('ctrl')
sleep(1)
pyautogui.press('a')
sleep(1)
pyautogui.keyUp('ctrl')
#-------------------------
pyautogui.write('100')
sleep(3)
# Botão nome do público
pyautogui.click(787, 659)
sleep(4)
pyautogui.keyDown('casplock')
pyautogui.write('100 DIAS(TODOS) VISITAS')
#ENGAJAMENTO
#VISITAS
sleep(2)
pyautogui.keyUp('casplock')
#------------------

#salvar videos
pyautogui.click(1177, 794)
sleep(2)
#------------------
pyautogui.keyDown('ctrl')
sleep(3)
pyautogui.press('w')
sleep(3)
pyautogui.keyUp('ctrl')
