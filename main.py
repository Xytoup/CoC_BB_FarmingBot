from time import sleep
import pyautogui as pg
from pynput.keyboard import Key, Controller
import random

counter = 0
position = [-21, -18, -15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 20]

keyboard = Controller()

keyboard.press(Key.alt_l)
keyboard.press(Key.tab)
sleep(1)
keyboard.release(Key.alt_l)
keyboard.release(Key.alt_l)

while counter < 100:

    # open the game
    pg.click(540+position[random.randint(0, 14)], 940+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    sleep(10)
    sleep(random.randint(0, 4))

    # collect elixir
    pg.click(1650+position[random.randint(0, 14)], 21+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(1850+position[random.randint(0, 14)], 1200+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(2140+position[random.randint(0, 14)], 150+position[random.randint(0, 14)], duration=1+random.randint(0, 2))

    # start battle
    pg.click(150+position[random.randint(0, 14)], 1300+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(1900+position[random.randint(0, 14)], 950+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    sleep(9)
    sleep(random.randint(0, 4))

    # place troops
    pg.click(600+position[random.randint(0, 14)], 1300+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(470+position[random.randint(0, 14)], 360+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(570+position[random.randint(0, 14)], 200+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(900+position[random.randint(0, 14)], 60+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(1600+position[random.randint(0, 14)], 40+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(1800+position[random.randint(0, 14)], 220+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(2050+position[random.randint(0, 14)], 400+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(440+position[random.randint(0, 14)], 1300+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    pg.click(550+position[random.randint(0, 14)], 1000+position[random.randint(0, 14)], duration=1+random.randint(0, 2))
    sleep(1)
    sleep(random.randint(0, 4))

    # close the game
    keyboard.press(Key.alt_l)
    keyboard.press(Key.f4)
    sleep(1)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.f4)

    counter += 1
