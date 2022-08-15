#! python3
# command_line_emailer.py - Logs in to Outlook and sends an email using CLI only

import getpass
from time import sleep
from xml.etree.ElementTree import SubElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Opens Outlook in Chrome
browser = webdriver.Chrome()
browser.get("https://outlook.office365.com/mail/inbox")

# Get Email Info from User
emailFromInput = input("Enter your email address:\n")
passwordInput = getpass.getpass("Enter password:\n")
emailToInput = input("Recipient's email address:\n")
subjectInput = input("Enter email's subject:\n")
msgBodyInput = input("Enter the body text of the email to send:\n")

# Login - Email Address
sleep(2)
emailElem = browser.find_element(By.CSS_SELECTOR, "input[type='email']")
emailElem.send_keys(emailFromInput)
emailElem.send_keys(Keys.ENTER)
# Login - Password
sleep(2)
pwdElem = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
pwdElem.send_keys(passwordInput)
pwdElem.submit()
# Stay Signed In? No
sleep(2)
noBtnElem = browser.find_element(By.CSS_SELECTOR, "input[value='No']")
noBtnElem.click()

# Create New Message
sleep(2)
newMsgElem = browser.find_element(By.CSS_SELECTOR, "[data-icon-name='ComposeRegular']")
newMsgElem.click()
# Email Field
sleep(2)
toFieldElem = browser.find_element(By.CSS_SELECTOR, "div[aria-label='To']")
toFieldElem.send_keys(emailToInput, Keys.ENTER)
# Subject Field
subjectElem = browser.find_element(By.CSS_SELECTOR, "input[aria-label='Add a subject']")
subjectElem.send_keys(subjectInput)
# Text Field
sleep(2)
msgBodyElem = browser.find_element(By.CSS_SELECTOR, "div[aria-label='Message body, press Alt+F10 to exit']")
msgBodyElem.send_keys(msgBodyInput)
# Send Email
sleep(2)
sendBtnElem = browser.find_element(By.CSS_SELECTOR, "button[aria-label='Send']")
sendBtnElem.click()