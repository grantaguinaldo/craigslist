def scrape_function():
    import requests as r
    from bs4 import BeautifulSoup as soup
    import pymongo

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.craigslistdb

    db.listing.drop()

    url = 'https://losangeles.craigslist.org/d/furniture/search/fua'

    data = r.get(url)

    print(data)

    page_soup = soup(data.text, 'html.parser')

    first_entry = page_soup.find_all('p', {'class', 'result-info'})[0]
    last_description = first_entry.find('a').text
    last_price = first_entry.find('span', {'class': 'result-price'}).text

    listings = {}

    listings['description'] = last_description
    listings['price'] = last_price

    listingData = db.listing.find()
    db.listing.insert_one(listings)

    listingData = db.listing.find()
    for each in listingData:
        print(each)

    print('Hi')

    return listings


# if __name__ == '__main__':
#     scrape_function()
