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
email_from_input = input("Enter your email address:\n")
password_input = getpass.getpass("Enter password:\n")
email_to_input = input("Recipient's email address:\n")
subject_input = input("Enter email's subject:\n")
msg_body_input = input("Enter the body text of the email to send:\n")

# Login - Email Address
sleep(2)
email_elem = browser.find_element(By.CSS_SELECTOR, "input[type='email']")
email_elem.send_keys(email_from_input)
email_elem.send_keys(Keys.ENTER)
# Login - Password
sleep(2)
pwd_elem = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
pwd_elem.send_keys(password_input)
pwd_elem.submit()
# Stay Signed In? No
sleep(2)
no_btn_elem = browser.find_element(By.CSS_SELECTOR, "input[value='No']")
no_btn_elem.click()

# Create New Message
sleep(2)
new_msg_elem = browser.find_element(
    By.CSS_SELECTOR, "[data-icon-name='ComposeRegular']")
new_msg_elem.click()
# Email Field
sleep(2)
to_field_elem = browser.find_element(By.CSS_SELECTOR, "div[aria-label='To']")
to_field_elem.send_keys(email_to_input, Keys.ENTER)
# Subject Field
subject_elem = browser.find_element(
    By.CSS_SELECTOR, "input[aria-label='Add a subject']")
subject_elem.send_keys(subject_input)
# Text Field
sleep(2)
msg_body_elem = browser.find_element(
    By.CSS_SELECTOR, "div[aria-label='Message body, press Alt+F10 to exit']")
msg_body_elem.send_keys(msg_body_input)
# Send Email
sleep(2)
send_btn_elem = browser.find_element(
    By.CSS_SELECTOR, "button[aria-label='Send']")
send_btn_elem.click()
