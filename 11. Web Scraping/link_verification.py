#! python3
# link_verification.py - given a URL of a webpage, this will download every linked page within that page
#                      - any broken links with 404 Error will print to console

import bs4, requests

url = input("Enter URL:\n")

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

for link in soup.select("a[href]"):
    try:
        link_url = link.get("href")
        if(link_url.startswith("/")):
            link_url = url + link_url
        if(link_url.startswith("http://") or link_url.startswith("https://")):
            link_res = requests.get(link_url)
            if(link_res.status_code == 404):
                print(f"404 Error: {link_url}")
    except:
        continue