import pyautogui
import time

out_img = pyautogui.locateCenterOnScreen('./no.png')
stock_img = pyautogui.locateCenterOnScreen('./yesnike.PNG')

while True:
    time.sleep(3)
    if stock_img == None:
        print('Out of Stock')
        pyautogui.moveTo(500,136,3)
        pyautogui.click()
        pyautogui.typewrite(['F5'])
    else:
        print('Find')
