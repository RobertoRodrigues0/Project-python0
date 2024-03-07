import pyautogui
from time import sleep
pyautogui.click(379, 553 )
#-----------------------
pyautogui.press('home')
sleep(2)
pyautogui.press('del')
sleep(1)
#-----------------
pyautogui.keyDown('shift')
sleep(1)
pyautogui.press('"')
sleep(1)
pyautogui.keyUp('shift')
sleep(1)
#----------------------
pyautogui.press('end')
sleep(1)
#----------------------
pyautogui.press('backspace')
sleep(1)
#---------------------
pyautogui.keyDown('shift')
sleep(1)
pyautogui.press('"')
sleep(1)
pyautogui.keyUp('shift')
sleep(1)
#----------------------------
pyautogui.press('tab')
sleep(3)
#------------------------
#2
#-----------------------
for b in range(1):
    for i in range(16):
        pyautogui.press('home')
        pyautogui.press('del')
        #-----------------

        pyautogui.keyDown('shift')
        pyautogui.press('"')
        pyautogui.keyUp('shift')
        #----------------------
        pyautogui.press('end')
        #----------------------
        pyautogui.press('backspace')
        #---------------------
        pyautogui.keyDown('shift')
        pyautogui.press('"')
        pyautogui.keyUp('shift')
        #----------------------------
        pyautogui.press('tab')
        sleep(1)
#------------------------
#-----Manutenção--------
#pyautogui.moveTo(1488, 1015, 1)
#pyautogui.click(, )
#sleep(10)
#breakpoint()
#----------------------------
#pyautogui.keyDown('ctrl')
#pyautogui.press('-')
#pyautogui.keyUp('ctrl')