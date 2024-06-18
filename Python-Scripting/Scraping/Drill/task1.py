# Task :
"""Scrape the description of the latest movies released in theaters from Allociné 
website extract the summaries of these movies. Automate the script for the entire 
list of movies. Put the information in three lists (film_links, title, synopsis). 
Create a DataFrame object from the pandas library. This dataframe will have to include 
these three informations in three columns. Finally, Save this dataframe in a CSV file.
PS: slow down the frequency of requests to avoid been identified and banned from the website.
"""

import time
import random
import requests

from bs4 import BeautifulSoup
import pandas as pd

# Define the base URL for Allociné's latest movies page
url = "https://www.allocine.fr"

# Initialize lists to store the extracted information
movie_links = []
titles = []
synopses = []

# Function to get the content of a webpage
def get_page_content(url):
    r = requests.get(url)
    time.sleep(random.uniform(1.0, 2.0))  # Sleep to avoid being banned
    return r.content

# Function to extract movie details from a given movie page URL
def extract_movie_details(movie_url):
    content = get_page_content(movie_url)
    soup = BeautifulSoup(content, 'lxml')

    # Extract the title
    title_tag = soup.find('h1', class_='titlebar-title')
    title = title_tag.text.strip() if title_tag else "No title found"

    # Extract the synopsis
    synopsis_tag = soup.find('div', class_='content-txt')
    synopsis = synopsis_tag.text.strip() if synopsis_tag else "No synopsis found"

    return title, synopsis

# Get the main page content
main_page_content = get_page_content(url)
main_soup = BeautifulSoup(main_page_content, 'lxml')

# Find all movie links
movie_containers = main_soup.find_all('div', class_='card entity-card entity-card-list cf')
for container in movie_containers:
    link_tag = container.find('a', class_='meta-title-link')
    if link_tag:
        movie_link = "https://www.allocine.fr" + link_tag['href']
        movie_links.append(movie_link)

# Loop through each movie link and extract details
for link in movie_links:
    title, synopsis = extract_movie_details(link)
    titles.append(title)
    synopses.append(synopsis)

    # check length
    len(movie_links)
    len(titles)
    len(synopses)

# Create a DataFrame from the lists
df = pd.DataFrame({
    'Title': titles,
    'Movie Link': movie_links,
    'Synopsis': synopses
})

# Save the DataFrame to a CSV file
df.to_csv('latest_movies.csv', index=False, encoding='utf-8')
print("CSV file has been created successfully!")
