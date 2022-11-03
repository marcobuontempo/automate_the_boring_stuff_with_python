#! python3
# scheduled_comic_downloader.py - Downloads any new web comics that have been added since the program was last run. Uses multi-threading to improve execution time.

import requests, bs4, json, os, threading

# Load existing JSON data for info about last fetched comics
json_read_file = open("./comic_info.json")
comic_info = json.load(json_read_file)
json_read_file.close()

os.makedirs("downloaded_comics", exist_ok=True)  # store comics in ./downloaded_comics

# Downloads any new xkcd comics
def get_xkcd():
    # Get the last saved URL
    prev_comic_url = comic_info["prev_xkcd"]

    # Get the Next comic's url
    print("Checking last XKCD comic...")
    res = requests.get(prev_comic_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    next_link = soup.select("a[rel='next']")[0]
    url = "https://xkcd.com" + next_link.get("href")

    if url.endswith("#"):
        print("Latest xkcd comic already fetched.")
        return
    
    while not url.endswith("#"):
        # Download the web page
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, features="lxml")

        # Find the URL of the comic image
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("Could not find comic image.")
        else:
            comic_url = "http:" + comic_elem[0].get("src")
            # Download the image
            print("Downloading image %s..." % comic_url)
            res = requests.get(comic_url)
            res.raise_for_status()
            # Save the image to ./downloaded_comics
            imageFile = open(os.path.join("downloaded_comics",os.path.basename(comic_url)), "wb")
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
    print("Checking last Left-Handed Toons comic...")
    res = requests.get(prev_comic_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    next_link = soup.select("li.next a")

    if len(next_link) == 0:
        print("No new comics.")
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
            print("Could not find comic image.")
        else:
            comic_url = comic_elem[0].get("src")
            # Download the image
            print("Downloading image %s..." % comic_url)
            res = requests.get(comic_url)
            res.raise_for_status()
            # Save the image to ./downloaded_comics
            imageFile = open(os.path.join("downloaded_comics",os.path.basename(comic_url)), "wb")
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        
        # Update JSON info
        comic_info["prev_left_handed_toons"] = url
        # Update href to next image
        next_link = soup.select("li.next a")



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
print("Done.")

# Save updated JSON info
with open("./comic_info.json", "w") as json_write_file:
    json_obj = json.dumps(comic_info)
    json_write_file.write(json_obj)