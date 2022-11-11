#! python3
# instant_messenger_bot.py - Automatically sends a direct message on Discord web-browser. 
# Works as of 10/11/22 on Macbook Pro using Retina display (this display affects some methods, such as .locateOnScreen())
# Usage: python3 instant_messenger_bot.py <discord_handles>
# Note: Separate discord handles using commas
# Example: python3 instant_messenger_bot.py Bob123, Katy567

import pyautogui, time, sys

# Verify correct usage
if len(sys.argv) < 2:
    print("Usage: python3 instant_messenger_bot.py <discord_handles>\nNote: Separate discord handles using commas")
    sys.exit()

try:
    print("\nPress Ctrl-C to exit program.")

    # Hard coded message to send
    MESSAGE = "Hi! I automated the sending of this message :)"

    # Get friend names from command-line and store in a properly formatted list
    friend_names = "".join(sys.argv[1:]).split(",")
    time.sleep(5)
    for friend_name in friend_names:
        # Locate and click button to start conversation
        start_button = pyautogui.locateCenterOnScreen("start_conversation_button.png")
        # Exit application if button is not located
        if start_button == None:
            print("Warning: cannot find button to start message!")
            break  
        start_button = list(start_button)
        pyautogui.moveTo(start_button[0]/2,start_button[1]/2)   # x & y coordinates to click. /2 due to Macbook Retina display
        pyautogui.click()
        time.sleep(5)

        # Find friend and open chat
        pyautogui.typewrite(friend_name, 0.25)
        pyautogui.press("enter")
        time.sleep(5)

        # Type message and send
        pyautogui.typewrite(MESSAGE)
        pyautogui.press("enter")
        time.sleep(5)


    print("All messages sent! :)")

except KeyboardInterrupt:
    print("\nProgram exited.")