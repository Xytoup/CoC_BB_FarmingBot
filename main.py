from time import sleep
import pyautogui as pg
from pynput.keyboard import Key, Controller

print(pg.size())

keyboard = Controller()

keyboard.press(Key.alt_l)
keyboard.press(Key.tab)
sleep(1)
keyboard.release(Key.alt_l)
keyboard.release(Key.alt_l)

while True:

    # open the game
    pg.click(540, 940, duration=1)
    sleep(10)

    # collect elixir
    pg.click(1650, 0, duration=1)
    pg.click(1850, 1200, duration=1)
    pg.click(2140, 150, duration=1)

    # start battle
    pg.click(150, 1300, duration=1)
    pg.click(1900, 950, duration=1)
    sleep(10)

    # place troops
    pg.click(600, 1300, duration=1)
    pg.click(470, 360, duration=1)
    pg.click(570, 200, duration=1)
    pg.click(900, 60, duration=1)
    pg.click(1600, 40, duration=1)
    pg.click(1800, 220, duration=1)
    pg.click(2050, 400, duration=1)
    pg.click(440, 1300, duration=1)
    pg.click(550, 1000, duration=1)
    sleep(2)

    # close the game
    keyboard.press(Key.alt_l)
    keyboard.press(Key.f4)
    sleep(1)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.f4)
