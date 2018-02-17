from flask import Flask, render_template
from flask_pymongo import PyMongo
import pymongo
import scrape

app = Flask(__name__)
mongo = PyMongo(app)


@app.route('/')
def index():

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.craigslistdb

    listings = mongo.db.listing.find_one()

    return render_template('index.html', listing=listings)


if __name__ == '__main__':
    app.run(debug=True)
