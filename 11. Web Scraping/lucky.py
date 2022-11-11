#! python3
# lucky.py - Opens the top PyPI search results
# Usage - python lucky.py [search query...]

import requests
import sys
import webbrowser
import bs4

print("Searching...")    # display text while downloading the Google page
res = requests.get("https://pypi.org/search?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# Open a browser tab for each result
linkElems = soup.select("a.package-snippet")
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open("https://pypi.org" + linkElems[i].get("href"))
