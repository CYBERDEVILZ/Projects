import pyautogui as pi
import time
while True:
    time.sleep(3)
    pi.moveTo(280, 230, 0.1)
    pi.click()
    time.sleep(1)
    try:
        x, y = pi.locateCenterOnScreen("!!!!!!!!!!!!!!!!PATH TO THE MAIL.PNG FILE!!!!!!!!!!!!!!")
    except:
        print("Mail has been cleaned!!")
        break
    pi.click(x, y)
    pi.moveTo(280, 230, 0.1)
    pi.click()
    pi.moveTo(341, 232, 0.1)
    pi.click()
    time.sleep(1)
