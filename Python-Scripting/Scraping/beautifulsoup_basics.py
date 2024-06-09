# Web scraping w/ BeautifulSoup

# BeautifulSoup is a Python library for parsing HTML documents
# download the BeautifulSoup4 package with 'pip install beautifulsoup4'

from bs4 import BeautifulSoup

# read file
becode_filename = "files/becode.html"
with open(becode_filename, "r") as file:
  html_doc = file.read()

soup = BeautifulSoup(html_doc, "lxml")
for tag in soup.find_all("h1"):
    # We only retrieve the content ==> .text
    print(tag.text)

# retrieve "h2" tags
for tag in soup.find_all("h2"):
    # We only retrieve the content ==> .text
    print(tag.text)

# retrieve "p" tags
for tag in soup.find_all("p"):
    # We only retrieve the content ==> .text
    print(tag.text)

# SCRAPING VIA HTTP REQUESTS

# the syntax of the requests: command >> URL >> protocol version
# commonly used requests: GET, POST, PUT, DELETE

import requests
# Url of website
url = "https://www.becode.org/about/"
# "GET" request to the site server
r = requests.get(url)
# display the requested url and the return of the server
print(url, r.status_code)
# store the HTML content parsed with lxml in the `soup` variable
soup = BeautifulSoup(r.content, "lxml")
