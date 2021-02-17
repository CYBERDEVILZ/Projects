import pyautogui as pi
import time
while True:
    time.sleep(3)
    a, b = pi.locateCenterOnScreen("./checkbox.png")
    c, d = pi.locateCenterOnScreen("./reload.png")
    pi.moveTo(a, b, 0.1)
    pi.click()
    time.sleep(1)
    try:
        x, y = pi.locateCenterOnScreen("./mail.png")
    except:
        pi.click(a, b)
        break
    pi.click(x, y)
    pi.moveTo(a, b, 0.1)
    pi.click()
    pi.moveTo(c, d, 0.1)
    pi.click()
    time.sleep(1)
