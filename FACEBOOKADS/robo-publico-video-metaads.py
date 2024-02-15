import pyautogui
import webbrowser
from time import sleep
webbrowser.open("https://adsmanager.facebook.com/adsmanager/audiences?act=1280056725926362&business_id=1016433562658262&tool=AUDIENCES&nav_entry_point=ads_ecosystem_navigation_menu&nav_source=ads_manager&breakdown_regrouping=1&date=2023-05-08_2024-02-14%2Cmaximum")
sleep(12)
#Botão Criar público
pyautogui.click(154, 200)
sleep(3)
#-----------
# Botão Público personalizado
pyautogui.click(144, 246)
sleep(3)
#-----------
# Botão Vídeo
pyautogui.click(748, 514)
sleep(3)
#-----------
# Botão Avançar
pyautogui.click(1252, 761)
sleep(3)
#-----------
# Botão  Escolha de Porcentagem de Visualização de Videos
pyautogui.click(1299, 372)
sleep(5)
#-----------
# Botão 25%
pyautogui.click(614, 524)
sleep(1)
#-----------
# Botão 50%
pyautogui.click(614, 615)
sleep(1)
#-----------
# Botão 75%
pyautogui.click(617, 677)
sleep(1)
#-----------
# Botão 95%
pyautogui.click(613, 740)
sleep(3)
#fim da seleção de porcentagem do video
#-----------

#--------------- Escolher Preenchimento de qual videos porcentagem 25%
pyautogui.click(1222, 311)
sleep(5)
#-----------
#--------------- Escolha do Instagram ou Pagina Facebook
pyautogui.click(750,210)
sleep(4)
#-----------
#--------------- Escolha do Opção Instagram
pyautogui.click(517,307)
sleep(4)
#-----------

#--------------- Seleção de Qual é o Instagram
pyautogui.click(1164, 220)
sleep(2)
#-----------
#Selecionar o Instagram Escolhido
pyautogui.click(931, 310)
sleep(3)
#-----------

#Diminuir tamanha de tela
pyautogui.keyDown('ctrl')
pyautogui.press('-')
pyautogui.keyUp('ctrl')
sleep(3)
#-----------
#cliquei baixar scroll baixo
pyautogui.click(1492, 980)
sleep(3)
#---------------
for b in range(6):
    for i in range(1):
        pyautogui.click(483, 931)
        sleep(2)
        pyautogui.click(480, 810)
        sleep(2)
        pyautogui.click(482, 698)
        sleep(2)
        pyautogui.click(482, 580)
        sleep(2)
        pyautogui.click(484, 468)
        sleep(2)
        pyautogui.click(483, 350)
        sleep(2)
        # Mudar a aba de escolha de videos
        pyautogui.click(1144, 211)
        sleep(4)
#----------------------
#Voltar 100% tamanho da pagina
pyautogui.keyDown('ctrl')
pyautogui.press('+')
pyautogui.keyUp('ctrl')
sleep(3)
#----------------------
#Ultima seleção de videos
pyautogui.click(430, 427)
sleep(4)
#----------------------
#salvar videos
pyautogui.click(1488, 1015)
sleep(4)
#---------------------
#----------------Salvo o primeira ABA
#---------------------


#-----Manutenção--------
#pyautogui.moveTo(1488, 1015, 1)
#sleep(10)
#breakpoint()




#--------------- Escolher Preenchimento de qual videos porcentagem 50%
pyautogui.click(1221, 402)
sleep(4)
#---------
#--------------- Escolha do Instagram ou Pagina Facebook
pyautogui.click(750,210)
sleep(4)
#-----------
#--------------- Escolha do Instagram
pyautogui.click(517,307)
sleep(4)
#-----------
#Diminuir tamanha de tela
pyautogui.keyDown('ctrl')
pyautogui.press('-')
pyautogui.keyUp('ctrl')
sleep(3)
#-----------
#cliquei baixar scroll baixo
pyautogui.click(1492, 980)
sleep(4)
#---------------
for b in range(6):
    for i in range(1):
        pyautogui.click(483, 931)
        sleep(2)
        pyautogui.click(480, 810)
        sleep(2)
        pyautogui.click(482, 698)
        sleep(2)
        pyautogui.click(482, 580)
        sleep(2)
        pyautogui.click(484, 468)
        sleep(2)
        pyautogui.click(483, 350)
        sleep(2)
        # Mudar a aba de escolha de videos
        pyautogui.click(1144, 211)
        sleep(4)
#----------------------
#Voltar 100% tamanho da pagina
pyautogui.keyDown('ctrl')
pyautogui.press('+')
pyautogui.keyUp('ctrl')
sleep(3)
#----------------------
#Ultima seleção de videos
pyautogui.click(430, 427)
sleep(4)
#----------------------
#salvar videos
pyautogui.click(1488, 1015)
sleep(4)
#----------------Salvo o Seguda ABA
#------------------



#--------------- Escolher Preenchimento de qual videos porcentagem 75%
pyautogui.click(1218, 482)
sleep(4)
#-----------
#--------------- Escolha do Instagram ou Pagina Facebook
pyautogui.click(750,210)
sleep(4)
#-----------
#--------------- Escolha do Instagram
pyautogui.click(517,307)
sleep(4)
#-----------
#Diminuir tamanha de tela
pyautogui.keyDown('ctrl')
pyautogui.press('-')
pyautogui.keyUp('ctrl')
sleep(3)
#-----------
#cliquei baixar scroll baixo
pyautogui.click(1492, 980)
sleep(4)
#---------------
for b in range(6):
    for i in range(1):
        pyautogui.click(483, 931)
        sleep(2)
        pyautogui.click(480, 810)
        sleep(2)
        pyautogui.click(482, 698)
        sleep(2)
        pyautogui.click(482, 580)
        sleep(2)
        pyautogui.click(484, 468)
        sleep(2)
        pyautogui.click(483, 350)
        sleep(2)
        # Mudar a aba de escolha de videos
        pyautogui.click(1144, 211)
        sleep(4)
#----------------------
#Voltar 100% tamanho da pagina
pyautogui.keyDown('ctrl')
pyautogui.press('+')
pyautogui.keyUp('ctrl')
sleep(3)
#----------------------
#Ultima seleção de videos
pyautogui.click(430, 427)
sleep(4)
#----------------------
#salvar videos
pyautogui.click(1488, 1015)
sleep(4)
#---------------------
#----------------Salvo o primeira ABA
#----------------Salvo o Seguda ABA
#------------------


#--------------- Escolher Preenchimento de qual videos porcentagem 95%
pyautogui.click(1221, 574)
sleep(4)
#-----------
#--------------- Escolha do Instagram ou Pagina Facebook
pyautogui.click(750,210)
sleep(4)
#-----------
#--------------- Escolha do Instagram
pyautogui.click(517,307)
sleep(4)
#-----------
#Diminuir tamanha de tela
pyautogui.keyDown('ctrl')
pyautogui.press('-')
pyautogui.keyUp('ctrl')
sleep(3)
#-----------
#cliquei baixar scroll baixo
pyautogui.click(1492, 980)
sleep(4)
#---------------
for b in range(6):
    for i in range(1):
        pyautogui.click(483, 931)
        sleep(2)
        pyautogui.click(480, 810)
        sleep(2)
        pyautogui.click(482, 698)
        sleep(2)
        pyautogui.click(482, 580)
        sleep(2)
        pyautogui.click(484, 468)
        sleep(2)
        pyautogui.click(483, 350)
        sleep(2)
        # Mudar a aba de escolha de videos
        pyautogui.click(1144, 211)
        sleep(4)
#----------------------
#Voltar 100% tamanho da pagina
pyautogui.keyDown('ctrl')
pyautogui.press('+')
pyautogui.keyUp('ctrl')
sleep(3)
#----------------------
#Ultima seleção de videos
pyautogui.click(430, 427)
sleep(4)
#----------------------
#salvar videos
pyautogui.click(1488, 1015)
sleep(4)
#---------------------
#----------------Salvo o primeira ABA
#----------------Salvo o Seguda ABA



#------------------
# Botão  Escolha Dias
pyautogui.click(663, 723)
sleep(4)
#----------------
#-------------------------
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.keyUp('ctrl')
pyautogui.write('90')
sleep(4)
# Botão nome do público
pyautogui.click(669, 805)
sleep(4)
pyautogui.write('90 DIAS  (25%,50%,75%, 95%) - VIEW ALL VIDEO')
sleep(4)
#------------------
#salvar videos
pyautogui.click(1288, 952)
sleep(5)
#------------------


#-------
#----
#------------------

