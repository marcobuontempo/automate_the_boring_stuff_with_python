#! python3
#! quick_weather.py - Prints the weather for a lcoation from the command line

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print("Usage: quick_weather.py API_KEY location")
    sys.exit()
API_KEY = sys.argv[1]
location = " ".join(sys.argv[2:])

# Download the JSON data from the OpenWeatherMap.org's API
url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=%s" % (location, API_KEY)
response = requests.get(url)
response.raise_for_status

# Load JSON data into a python variable
weather_data = json.loads(response.text)

# Print weather descriptions
w = weather_data["list"]
print("Current weather in %s:" % (location))
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])
print()
print("Tomorrow:")
print(w[1]["weather"][0]["main"], "-", w[1]["weather"][0]["description"])
print()
print("Day after tomorrow:")
print(w[2]["weather"][0]["main"], "-", w[2]["weather"][0]["description"])