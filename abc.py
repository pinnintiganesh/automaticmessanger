import pyautogui 
import time 


time.sleep(3)
print(pyautogui.position())

pyautogui.leftClick(837, 1053,1)
time.sleep(1)
pyautogui.typewrite("https://web.telegram.org/?legacy=1")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("enter")
pyautogui.leftClick(475, 249,1)
time.sleep(1)

for i in range(10):
    pyautogui.typewrite("hi afzal")
    pyautogui.press("enter")
    time.sleep(1)
# 475 259