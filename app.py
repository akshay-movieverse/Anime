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
    def get(self,name):
        try:
            scraper = cfscrape.create_scraper()
            curl="https://4anime.to/" + name
            data=(scraper.get(curl).content)
            soup = BeautifulSoup(data,'html.parser')
            st=soup.findAll('video' )#.getText()
            for gt in st:
                yu=gt.find('source')
                #print(yu['src'])
            print(yu['src'])
            return {'link': str(yu['src'])}
        except:
            return 'fail'



api.add_resource(Three, "/4Anime/<string:name>")
if __name__ == "__main__":
    app.run(debug=True)