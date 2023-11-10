import sys
from time import sleep
import pyautogui as pg
from pynput.keyboard import Key, Controller
import random

key = Controller()
position = [-21, -18, -15, -12, -9, -6, -3, 0, 3, 6, 9, 12, 15, 18, 21]


def scaling_finder():
    print("Whats your display resolution?")
    print("1 for 1080p, 2 for 1440p")
    print("--------------------")
    match int(input("> ")):

        case 1:
            return 0.5625

        case 2:
            return 1.0


def tab():
    # change window
    key.press(Key.alt_l)
    key.press(Key.tab)
    sleep(1)
    key.release(Key.alt_l)
    key.release(Key.tab)


def attack_bot(attacks, scaling):

    tab()
    counter = 0
    while counter < attacks:
        # open the game
        pg.click(600, 1000, duration=1)
        sleep(20)
        sleep(random.randint(0, 4))

        # collect elixir
        pg.click(1650 * scaling + position[random.randint(0, 14)], 21 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(1850 * scaling + position[random.randint(0, 14)], 1200 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(2140 * scaling + position[random.randint(0, 14)], 150 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))

        # start battle
        pg.click(150 * scaling + position[random.randint(0, 14)], 1300 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(1900 * scaling + position[random.randint(0, 14)], 950 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        sleep(9)
        sleep(random.randint(0, 4))

        # place units
        pg.click(600 * scaling + position[random.randint(0, 14)], 1300 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(470 * scaling + position[random.randint(0, 14)], 360 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(570 * scaling + position[random.randint(0, 14)], 200 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(900 * scaling + position[random.randint(0, 14)], 60 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(1600 * scaling + position[random.randint(0, 14)], 40 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(1800 * scaling + position[random.randint(0, 14)], 220 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(2050 * scaling + position[random.randint(0, 14)], 400 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(440 * scaling + position[random.randint(0, 14)], 1300 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        pg.click(550 * scaling + position[random.randint(0, 14)], 1000 * scaling + position[random.randint(0, 14)],
                 duration=1 + random.randint(0, 2))
        sleep(1)
        sleep(random.randint(0, 4))

        # close the game
        key.press(Key.alt_l)
        key.press(Key.f4)
        sleep(1)
        key.release(Key.alt_l)
        key.release(Key.f4)

        counter += 1

        print(f'{counter} attacks done')


print("How many attacks will the bot do for you?")
attacks = int(input("> "))
print("--------------------")

# start the bot
attack_bot(attacks, scaling_finder())

# close the game
key.press(Key.alt_l)
key.press(Key.f4)
sleep(1)
key.release(Key.alt_l)
key.release(Key.f4)

sys.exit()
