import pyautogui

pyautogui.PAUSE = 2.5
pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.PAUSE = 2.5
pyautogui.keyUp('win')
pyautogui.PAUSE = 2.5
pyautogui.write('notepad')
pyautogui.PAUSE = 2.5
pyautogui.press('enter')
pyautogui.PAUSE = 2.5
pyautogui.write('Escreve essaEscreve essa porrada porrada')
pyautogui.press(['left','left','left'])
pyautogui.PAUSE = 2.5



