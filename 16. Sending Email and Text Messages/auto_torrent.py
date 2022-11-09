#! python3
# auto_torrent.py - Automatically launches qBittorrent and begins download, when selected email account receives a torrent magnet link with Subject: "Torrent Link".

import imapclient, pyzmail, subprocess, time

QBITTORRENT_PATH = "/Applications/qbittorrent.app" # Path to qBittorrent application

# Get email settings from user
email_receiver_address = input("Enter the email address to receive emails from:\n")
email_receiver_password = input("Enter the password for the email address:\n")
email_sender_address = input("Enter the email address that will send the torrent links through email (i.e. only emails sent from this selected address will be able to launch qBittorrent):\n")

# Searches for any new magnet links in inbox
def get_magnet_links():
    # Fetch raw messages for all unread emails from the specified email sender address
    imap_obj = imapclient.IMAPClient("imap.gmail.com", ssl=True)
    imap_obj.login(email_receiver_address, email_receiver_password)
    imap_obj.select_folder("INBOX", readonly=False)
    UIDs = imap_obj.search(["FROM %s" % email_sender_address, "UNSEEN"])
    raw_messages = imap_obj.fetch(UIDs, ["BODY[]"])

    magnet_links = []   # List to store all new magnet links found
    if raw_messages:
        for UID in raw_messages:
            message = pyzmail.PyzMessage.factory(raw_messages[UID]["BODY[]"])   # Get message
            if message.get_subject().lower() != "torrent link": continue    # Skip if subject is not "Torrent Link"
            link = message.html_part.get_payload().decode(message.html_part.charset)    # Get link
            magnet_links.append(link)   # Store link in list
        
    imap_obj.logout()   # Exit email

    return magnet_links



time_elapsed = 0
while True:
    if time_elapsed % (60*30) == 0: # Run every 30 minutes from the time of starting program
        time_elapsed = 0    # Reset time elapsed every 30 minutes
        magnet_links = get_magnet_links()
        for link in magnet_links:
            subprocess.Popen(QBITTORRENT_PATH + " " + link) # Open qBittorrent with each magnet link found
    # Sleep and update time elapsed after every check
    time.sleep(1)
    time_elapsed += 1