from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


# alt tab yapmak için süre
time.sleep(2)

# while döngüsü ama g ye basınca duruyo işte
while keyboard.is_pressed('g') == False:

    if pyautogui.locateOnScreen('no_posts.png', region=(0, 0, 1440, 900), grayscale=True, confidence=0.9) is not None:
        # gönderileri yenilemek için
        pyautogui.click(707, 263)
        pyautogui.drag(0, 400, duration=0.5)
        time.sleep(0.2)





    if pyautogui.locateOnScreen('archive.png', region=(0, 0, 1440, 900), grayscale=True,
                                confidence=0.7) is not None:

        # sadece x ve ye koordinatlarını depoluyor
        x, y = pyautogui.locateCenterOnScreen('archive.png', region=(0, 0, 1440, 900), grayscale=True,
                                           confidence=0.9)
        #x ve y koordinatlarına tıkla
        pyautogui.click(x, y)
        # post arşivlenirken beklemek için
        time.sleep(0.55)

    if pyautogui.locateOnScreen('3nokta.png', region=(0, 0, 1440, 900), grayscale=True,
                                confidence=0.8) is not None:


        try:
            x,y= pyautogui.locateCenterOnScreen('3nokta.png', region=(0, 0, 1440, 900), grayscale=True,
                                                 confidence=0.8)
            # x ve y koordinatlarına tıkla
            pyautogui.click(x, y)
            # ig animasyonu için süre
            time.sleep(0.3)
        except:
            pass



    if  pyautogui.locateOnScreen('likes.JPG', region=(0, 0, 1440, 900), grayscale=True,
                                confidence=0.9) is not None or pyautogui.locateOnScreen('likes2.JPG', region=(0, 0, 1440, 900), grayscale=True,
                                confidence=0.9) is not None:
        x, y = pyautogui.locateCenterOnScreen('go_back.png', region=(0, 0, 1440, 900), grayscale=True,
                                 confidence=0.9)
        pyautogui.click(x, y)



