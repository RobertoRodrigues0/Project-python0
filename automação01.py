import pyautogui
pyautogui.PAUSE = 2.5
pyautogui.keyDown('alt')
pyautogui.PAUSE = 2.5
pyautogui.press('tab')
pyautogui.PAUSE = 2.5
pyautogui.keyUp('alt')
pyautogui.PAUSE = 2.5
pyautogui.click('imagem-teste-mouse.PNG')
pyautogui.PAUSE = 2.5
pyautogui.move(0,100)
pyautogui.PAUSE = 2.5
pyautogui.drag(200, 200,5)
pyautogui.PAUSE = 2.5


screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()