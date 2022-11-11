#! python3
# 2048.py - Plays the game 2048 by automatically inputting a constant sequence of up/right/down/left keystrokes
#         - It will retry until the game has been won

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Opens 2048 in Chrome
browser = webdriver.Chrome()
browser.get("https://play2048.co/")

# Get HTML tag (i.e. entire page) to send keystrokes to
html_elem = browser.find_element(By.TAG_NAME, "html")

# Algorithm to loop up/right/down/left keystrokes
while (True):
    game_message = browser.find_element(
        By.CSS_SELECTOR, ".game-message p").text
    if (game_message == "Game over!"):
        # Retry if didn't win
        browser.find_element(By.CSS_SELECTOR, ".retry-button").click()
    elif (game_message == "You win!"):
        # End if game has been completed
        break
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)
