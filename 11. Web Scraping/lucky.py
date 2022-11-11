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
link_elems = soup.select("a.package-snippet")
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open("https://pypi.org" + link_elems[i].get("href"))
