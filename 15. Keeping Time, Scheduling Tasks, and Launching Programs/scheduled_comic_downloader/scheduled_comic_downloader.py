#! python3
# scheduled_comic_downloader.py - Downloads any new web comics that have been added since the program was last run
# Uses multi-threading to improve execution time.
# When running the program, it will fetch and download new comics one time.
# If the program is left to run, it will continue to periodically fetch and download at 12pm every day.

import requests
import bs4
import json
import os
import threading
import time
import datetime

# Load existing JSON data for info about last fetched comics
json_read_file = open("./comic_info.json")
comic_info = json.load(json_read_file)
json_read_file.close()

# Get datetime objects for last, current and next
last_fetch = datetime.datetime.strptime(
    comic_info["last_fetch"], "%Y-%m-%d %H:%M:%S")
current_datetime = datetime.datetime.now()
next_fetch = (last_fetch + datetime.timedelta(days=1)
              ).replace(hour=12, minute=0, second=0)

# store comics in ./downloaded_comics
os.makedirs("downloaded_comics", exist_ok=True)

# Downloads any new xkcd comics


def get_xkcd():
    # Get the last saved URL
    prev_comic_url = comic_info["prev_xkcd"]

    # Get the Next comic's url
    print("Checking for new xkcd comics...")
    res = requests.get(prev_comic_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    next_link = soup.select("a[rel='next']")[0]
    url = "https://xkcd.com" + next_link.get("href")

    if url.endswith("#"):
        print(" - Latest xkcd comic already fetched.")
        return

    while not url.endswith("#"):
        # Download the web page
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="lxml")

        # Find the URL of the comic image
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print(" - Could not find comic image.")
        else:
            comic_url = "http:" + comic_elem[0].get("src")
            # Download the image
            print(" - Downloading image %s..." % comic_url)
            res = requests.get(comic_url)
            res.raise_for_status()
            # Save the image to ./downloaded_comics
            imageFile = open(os.path.join("downloaded_comics",
                             os.path.basename(comic_url)), "wb")
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # Update JSON info
        comic_info["prev_xkcd"] = url
        # Update URL to next image
        next_link = soup.select("a[rel='next']")[0]
        url = "https://xkcd.com" + next_link.get("href")


# Downloads any new XKCD comics
def get_left_handed_toons():
    # Get the last saved URL
    prev_comic_url = comic_info["prev_left_handed_toons"]

    # Get the Next comic's url
    print("Checking for new Left-Handed Toons comic...")
    res = requests.get(prev_comic_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    next_link = soup.select("li.next a")

    if len(next_link) == 0:
        print(" - Latest Left-Handed Toons comic already fetched.")
        return

    while len(next_link) != 0:
        # Download the web page
        url = "http://www.lefthandedtoons.com" + next_link[0].get("href")
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="lxml")

        # Find the URL of the comic image
        comic_elem = soup.select(".comicimage")
        if comic_elem == []:
            print(" - Could not find comic image.")
        else:
            comic_url = comic_elem[0].get("src")
            # Download the image
            print(" - Downloading image %s..." % comic_url)
            res = requests.get(comic_url)
            res.raise_for_status()
            # Save the image to ./downloaded_comics
            imageFile = open(os.path.join("downloaded_comics",
                             os.path.basename(comic_url)), "wb")
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # Update JSON info
        comic_info["prev_left_handed_toons"] = url
        # Update href to next image
        next_link = soup.select("li.next a")


def get_all():
    # Multi-thread each comic download
    # Create and start the Thread objects.
    threads = []   # a list of all the Thread objects

    xkcd_thread = threading.Thread(target=get_xkcd)
    threads.append(xkcd_thread)
    left_handed_toons_thread = threading.Thread(target=get_left_handed_toons)
    threads.append(left_handed_toons_thread)

    for thread in threads:
        thread.start()

    # Wait for all the threads to end.
    for thread in threads:
        thread.join()
    print("Fetch & Download Completed.\n")

    # Save updated JSON info
    with open("./comic_info.json", "w") as json_write_file:
        comic_info["last_fetch"] = current_datetime.strftime(
            "%Y-%m-%d %H:%M:%S")   # Update the last_fetch to current datetime
        json_obj = json.dumps(comic_info)
        json_write_file.write(json_obj)


# Fetch and download once
get_all()


# Wait for 12pm each day to re-fetch and download
print("Waiting for next fetch call at %s...\n" % next_fetch)
while True:
    current_datetime = datetime.datetime.now()  # Update current datetime
    if current_datetime >= next_fetch:
        get_all()
        next_fetch = (current_datetime + datetime.timedelta(days=1)).replace(
            hour=12, minute=0, second=0)  # Set next fetch to 12pm next day
        print("Waiting for next fetch call at %s...\n" %
              next_fetch.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        time.sleep(1)   # Wait if no fetch is required
