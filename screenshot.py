import pyautogui
import time


def screenshot():
    name=int(round(time.))
    time.sleep(5)
    img=pyautogui.screenshot('test.png')
    img.show()

screenshot()