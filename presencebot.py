from pyautogui import move
from time import time, sleep

mins_to_run = int(60) # Change number to number of minutes you need
time_stop = time() + (60 * mins_to_run)

while time() < time_stop:
    move(400, 0)
    move(0, 400)
    move(-400, 0)
    move(0, -400)
    sleep(300)
