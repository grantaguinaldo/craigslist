def mongo_store_():
    import pymongo
    import scrape

    listings = scrape.scrape_function()

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.craigslistdb

    db.listing.drop()

    db.listing.insert_one(listings)
    listingData = db.listing.find()

    for each in listingData:
        print(each)

    return listingData


if __name__ == '__main__':
    mongo_store_()
