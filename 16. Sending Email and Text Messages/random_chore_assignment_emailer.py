#! python3
# random_chore_assignment_emailer.py - Takes a list of email addresses and a list of chores, and randomly assigns chores to people.

import random
import smtplib

# Get credentials for email from command line input.
email_address = input("Enter your email address:\n")
email_password = input("Enter your password:\n")

# Hard-coded emails and chores to allocate
emails = ["abby@email.com", "bob@email.com",
          "cindy@email.com", "darren@email.com"]
chores = ["dishes", "bathroom", "vacuum", "walk dog"]

# Dictionary to store assigned chores
# email : chore
assigned_chores = {}

# Gets a random chore and removes from the list


def get_random_chore():
    random_chore = random.choice(chores)
    chores.remove(random_chore)
    return random_chore


# Assign each email to a random chore
for email in emails:
    assigned_chores[email] = get_random_chore()

for assignee, chore in assigned_chores.items():
    print(assignee, chore)


# Login to email account
smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(email_address, email_password)

# Send out chores to emails
for email, chore in assigned_chores.items():
    body = "Subject: Chore - %s.\nYour assigned chore is: %s. Please complete it!" % (
        email, chore)
    print("Sending email to %s..." % email)
    send_email_status = smtp_obj.sendmail(email_address, email, body)

    if send_email_status != {}:
        print("There was a problem sending email to %s: %s" %
              (email, send_email_status))

smtp_obj.quit()
