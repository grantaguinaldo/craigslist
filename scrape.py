import requests as r
from bs4 import BeautifulSoup as soup


def scrape_function():

    url = 'https://losangeles.craigslist.org/d/furniture/search/fua'

    data = r.get(url)

    print(data)

    page_soup = soup(data.text, 'html.parser')

    first_entry = page_soup.find_all('p', {'class', 'result-info'})[0]
    last_description = first_entry.find('a').text

    #If the price is not present in the add, then the script will not run properlly.
    last_price = first_entry.find('span', {'class': 'result-price'}).text

    listings = {}

    listings['description'] = last_description
    listings['price'] = last_price

    return listings


if __name__ == '__main__':
    scrape_function()
