#! python3
# looking_busy.py - Moves the cursor every 10 seconds, to prevent applications from entering idle mode

import pyautogui
import time

DELAY = 10  # Number of seconds to wait (i.e. 10 seconds)

countdown = DELAY   # Initialise countdown to the delay

try:
    print("\nPress Ctrl-C in terminal to exit program at any time.")
    while True:
        if countdown > 0:
            # Reduce countdown while it is above 0 seconds
            time.sleep(1)
            countdown -= 1
            continue

        # When countdown is 0 (i.e. total delay time has elapsed), jiggle the cursor up and down 1px
        pyautogui.moveRel(0, -1, 0.1)
        pyautogui.moveRel(0, 1, 0.1)
        countdown = DELAY   # Reset the countdown after the mouse has been jiggled

except KeyboardInterrupt:
    print("\nProgram exited.")
