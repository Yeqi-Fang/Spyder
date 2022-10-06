import pyautogui
import time
import xlrd
import pyperclip

img2 = r"pic/Screenshot 2022-09-06 183945.png"
img1 = r"pic/Screenshot 2022-09-06 183537.png"
clickTimes = 1
lOrR = 'left'
location = pyautogui.locateCenterOnScreen(img2, confidence=0.9)
pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
while True:
    location = pyautogui.locateCenterOnScreen(img1, confidence=0.8)
    if location is not None:
        pyautogui.click(location.x, location.y, clicks=clickTimes, interval=0.2, duration=0.2, button=lOrR)
    else:
        pyautogui.moveTo(1000, 1000)
        pyautogui.scroll(-500)
