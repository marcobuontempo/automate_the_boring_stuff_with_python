#! python3
# text_myself.py - Defines the textmyself() function that texts a message passed to it as a string.

from twilio.rest import TwilioRestClient

# Preset values:
account_SID = input("Enter Account SID: (e.g. ACxxxxxxxxxxxxxxxxxxx)\n")
auth_token = input("Enter Auth Token:\n")
twilio_number = input("Enter Twilio Number: (e.g. +xxxxxxxxxxx)\n")
cell_phone = input("Enter Cell Phone Number: (e.g +xxxxxxxxxxx)\n")
message_body = input("Enter message body:\n")


def textmyself(message):
    twilio_cli = TwilioRestClient(account_SID, auth_token)
    twilio_cli.messages.create(
        body=message_body, from_=twilio_number, to=cell_phone)
