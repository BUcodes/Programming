# The purpose of scraping is to automate 
# the collection of targeted information on the web

# Task
"""Scrape the description of the latest movies released in theaters. 
Go to the Allociné website and try to find the tags that will give 
links to the specific pages of these movies to get their summaries
"""

# import libraries
from bs4 import BeautifulSoup
import requests


# first, recover url of the page of newly released films
url = "https://www.allocine.fr/"
r = requests.get(url)
print(r.status_code)

# create Beautifulsoup oject for web scraping
soup = BeautifulSoup(r.content, "lxml")
print(soup)


# manually inspect the web page and find tags of interest
# extract the value of the class variable of these identical tags.
for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
    print(elem.get("href")) # displays relative path of the pages


# put href values in a list
links = []
for elem in soup.find_all("a", attrs={"class": "meta-title meta-title-link"}):
    links.append(elem.get("href"))
    

# construct the absolute path by appending the url
movie_links = ["http://www.allocine.fr" + elem for elem in links if "film" in elem]


# inspect each movie to determine class of title & synopsis
# for example a link has the title and synopsis as follows:
# title: <div class="titlebar-title titlebar-title-lg">Le Grand Bain</div>
# synopsis: <div class="content-txt " itemprop="description"
# extract the title & synopsis


# Finally, retrieve title & synopsis on each page
for link in movie_links:
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "lxml")

    # Extract the title
    title_elements = soup.find_all("div", attrs={"class": "titlebar-title titlebar-title-lg"})
    if title_elements:
        for elem in title_elements:
            print("Title:", elem.get_text().strip())
    else:
        print(f"No title found for {link}")

    # Extract the synopsis
    synopsis_elements = soup.find_all("div", attrs={"class": "content-txt", "itemprop": "description"})
    if synopsis_elements:
        for elem in synopsis_elements:
            print("Synopsis:", elem.get_text().strip())
    else:
        print(f"No synopsis found for {link}")
    






     
