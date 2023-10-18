from time import sleep
import pyautogui
import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=0_rod5TcCAU")
sleep(10)
# Scrolling
#pyautogui.mouseDown(1063, 241)
#sleep(5)
#pyautogui.mouseUp()
for i in range(50):
    pyautogui.scroll(-200)
    sleep(2)