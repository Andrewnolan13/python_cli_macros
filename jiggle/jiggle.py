import pyautogui as pag 
import random
import sys

def jiggler():
    pag.FAILSAFE = False

    try:
        while True:
            a = random.randint(1, 10)
            b = 1

            while b <= a:
                pag.PAUSE = random.randint(1, 3)
                pag.moveRel(random.randint(-500, 500), random.randint(-500, 500), duration=0.5)
                b += 1

            pag.press('capslock')
            pag.PAUSE = 1
            pag.press('capslock')
    
    except KeyboardInterrupt:
        sys.exit(0)