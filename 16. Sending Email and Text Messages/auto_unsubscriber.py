#! python3
# auto_unsubscriber.py - scans email account for 'Unsubscribe' links, and automatically opens them in browser

import imaplib
import imapclient
import pyzmail
import webbrowser
import bs4

imaplib._MAXLINE = 10000000

# Get email and password details
email = input("Enter your email username:\n")
password = input("Enter your email password:\n")

# Get all emails in inbox
imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
imap_obj.login(email, password)
imap_obj.select_folder("INBOX", readonly=True)
UIDs = imap_obj.search(["ALL"])

# Create list of "unsubscribe" links
unsubscribe_links = []
for UID in UIDs:
    raw_message = imap_obj.fetch([UID], ["BODY[]", "FLAGS"])
    message = pyzmail.PyzMessage.factory(raw_message[UID]["BODY[]"])
    html = message.html_part.get_payload().decode(message.html_part.charset)
    soup = bs4.BeautifulSoup(html, "lxml")
    link_elems = soup.select("a")
    for selected in link_elems:
        if "unsubscribe" in str(selected):
            unsubscribe_links.append(selected.get("href"))
imap_obj.logout()

# Open each link in browser
for link in unsubscribe_links:
    webbrowser.open(link)

print("Operation complete.")
