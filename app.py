from flask import Flask,jsonify, request 
from flask_restful import Api, Resource

import cloudscraper as cfscrape
from bs4 import BeautifulSoup

from flask_cors import CORS, cross_origin
import json
from json import JSONEncoder
import pafy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/api3": {"origins": "*"}})

api = Api(app)

class Three(Resource):
    @cross_origin(origin='*')
    def get(self):
        try:
            scraper = cfscrape.create_scraper()
            curl="https://4anime.to/one-piece-episode-1?id=1051"
            data=(scraper.get(curl).content)
            soup = BeautifulSoup(data,'html.parser')
            st=soup.findAll('script' )#.getText()
            #print(soup)
            for gt in st:
                if "href" in str(gt):
                    vt=gt
                    break
            print(vt)
            return {'id': str(vt)}

        except:
            return "Fail"

api.add_resource(Three, "/test/360/")
if __name__ == "__main__":
    app.run(debug=True)