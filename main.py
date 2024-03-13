import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode


TOGGLE_KEY = KeyCode.from_char("t")
FREQUENCY = 10 # how many times per second you want an event to occur

clicking = False
interval = 1
mouse = Controller()


def calculate_interval():
    if FREQUENCY <= 0:
        raise ValueError("Frequency must be greater than zero")
    return 1 / FREQUENCY


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(interval)


def toggle_event(key):
    if key == TOGGLE_KEY:
        print('Pressed')
        global clicking
        clicking = not clicking
        global interval
        interval = calculate_interval()


click_thread = threading.Thread(target=clicker)
click_thread.start()


# Collect events until released
with Listener(on_press=toggle_event) as listener:
    print('Listening...')
    try:
        listener.join()
    except Exception as e:
        print('{0} was pressed'.format(e.args[0]))
