#! python3
# image_site_downloader.py - Downloads a specified number of images from a specified search term from unsplash.com

import requests
import os
import bs4

category = input("Enter your category to search:\n")
num_files = int(input(
    "How many files do you want to limit the download to? (Note: 0=unlimited)\n"))

os.makedirs(os.path.join("unsplash", category),
            exist_ok=True)  # store files in folder

res = requests.get(f"https://unsplash.com/s/photos/{category}")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")
images = soup.select("div[data-test='search-photos-route'] img")
if images == []:
    print("None")
else:
    for i in range(min(num_files, len(images))):
        img_alt = "_".join(images[i].get("alt").split(" ")) if images[i].get(
            "alt") != None else "unnamed_picture"
        img_name = img_alt + "_" + str(i + 1) + ".png"
        # Download Image
        image_res = requests.get(images[i].get("src"))
        image_res.raise_for_status()
        print(f"    - Downloading image {img_name}...")
        # Save Image
        image_file = open(os.path.join("unsplash", category, img_name), "wb")
        for chunk in image_res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
