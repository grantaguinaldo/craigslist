# Standard Imports

from flask import Flask, render_template
from flask_pymongo import PyMongo
import pymongo
import scrape
import requests as r
from bs4 import BeautifulSoup as soup


# Define the app.
app = Flask(__name__)

# Instantiate PyMongo.
mongo = PyMongo(app)


# Make a connection to the MongoDB database on localhost.
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Create or connect to Database.
db = client.craigslistdb

# Drop 'listing' table.
db.listing.drop()

# Url to scrape
url = 'https://losangeles.craigslist.org/d/furniture/search/fua'

# Connect to URL.
data = r.get(url)

# Print response code.
print(data)

# Read in text into BS
page_soup = soup(data.text, 'html.parser')

# Scrape information from Craiglist.
first_entry = page_soup.find_all('p', {'class', 'result-info'})[0]
last_description = first_entry.find('a').text
last_price = first_entry.find('span', {'class': 'result-price'}).text

# Create empty dict.
listings = {}

# Populate dict.
listings['description'] = last_description
listings['price'] = last_price

# Insert data (stored in variable named 'listings') into collection named 'listing'
listingData = db.listing.find()
db.listing.insert_one(listings)

# Query collection named 'listing' and print out the entries to terminal.
listingData = db.listing.find()
for each in listingData:
    print(each)

# Print 'Hi' to confirm that the code made it this far.
print('Hi')


@app.route('/')
def index():

    listingData = db.listing.find()
    listings = mongo.db.listing.find_one()

    return render_template('index.html', listing_=listings)


if __name__ == '__main__':
    app.run(debug=True)
