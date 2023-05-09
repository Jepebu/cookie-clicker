import pyautogui as pg
import time
import keyboard

#cookie is 250 500
#cursor is 1750 350
#each upgrade is about 50 px, add 50 more every 3 items

i = 0

def cookie():
    pg.click(250,500)



def upgrade():
    x = 1020
    for foo in range(12):
        pg.click(1750,x)
        x -= 60
    return 0


while keyboard.is_pressed("q") == False:
    cookie()
    i += 1
    if i == 1000:
        i = upgrade()