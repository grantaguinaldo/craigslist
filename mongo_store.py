import pymongo
import scrape


def mongo_store_():

    listings = scrape.scrape_function()

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.craigslistdb

    db.listing.drop()

    db.listing.insert_one(listings)
    listingData = list(db.listing.find())

    # Sending the object to a list is needed.
    # https://stackoverflow.com/questions/28968660/how-to-convert-a-pymongo-cursor-cursor-into-a-dict

    return listingData[0]
