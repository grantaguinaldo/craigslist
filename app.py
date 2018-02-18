from flask import Flask, render_template
import mongo_store


app = Flask(__name__)


@app.route('/')
def index():

    listings = mongo_store.mongo_store_()  #This needs to be in the form a list.

    return render_template('index.html', page_data=listings)


if __name__ == '__main__':
    app.run(debug=True)
