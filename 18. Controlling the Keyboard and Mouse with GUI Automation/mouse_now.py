#! python3
# mouse_now.py = Displays the mouse cursor's current position.

import pyautogui

print("Press Ctrl-C to quit.")

try:
    while True:
        # Get and print the mouse coordinates
        x, y = pyautogui.position()
        position_str = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(position_str, end="")
        print("\b" * len(position_str), end="", flush=True)
except KeyboardInterrupt:
    print("\nDone.")