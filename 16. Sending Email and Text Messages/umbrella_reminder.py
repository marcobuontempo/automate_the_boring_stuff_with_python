#! python3
# umbrella_reminder.py - checks the weather in the morning at 6am and sends a text message reminder if an umbrella is required.
# Usage: umbrella_reminder.py <Twilio SID> <Twilio Auth Token> <Twilio Number> <Cell Number> <OpenWeather API Key> <location>

import json
import requests
import sys
import datetime
import time
from twilio.rest import TwilioRestClient

# Get command line args
if len(sys.argv) < 7:
    print("Usage: umbrella_reminder.py <Twilio SID> <Twilio Auth Token> <Twilio Number> <Cell Number> <OpenWeather API Key> <location>")
    sys.exit()
account_SID = sys.argv[1]
auth_token = sys.argv[2]
twilio_number = sys.argv[3]
cell_phone = sys.argv[4]
API_KEY = sys.argv[5]
location = " ".join(sys.argv[6:])


def check_if_raining():
    # Download the JSON data from the OpenWeatherMap.org's API
    url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=%s" % (
        location, API_KEY)
    response = requests.get(url)
    response.raise_for_status
    # Load JSON data into a python variable
    weather_data = json.loads(response.text)
    # Check if raining
    is_raining = "rain" in weather_data["list"][0]["weather"][0]["main"].lower(
    )
    return is_raining

# Send text reminder


def send_reminder():
    message_body = "REMINDER! It's raining today!"
    twilio_cli = TwilioRestClient(account_SID, auth_token)
    twilio_cli.messages.create(
        body=message_body, from_=twilio_number, to=cell_phone)


# Schedule at 6am
while True:
    current_datetime = datetime.datetime.now()  # Update current datetime
    if current_datetime.hour == 6 and current_datetime.minute == 0 and current_datetime.second == 0:
        if check_if_raining():
            send_reminder()  # Send reminder if raining
    else:
        time.sleep(1)   # Wait until 6am
