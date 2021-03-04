from flask import Flask,jsonify, request 
from flask_restful import Api, Resource
from selenium import webdriver
import cloudscraper as cfscrape
from bs4 import BeautifulSoup

from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api3": {"origins": "*"}})
api = Api(app)

class Three(Resource):
    @cross_origin(origin='*')
    def get(self,name):
        try:
            browser = webdriver.PhantomJS()
            url="https://4anime.to/"+name
            browser.get(url)
            html = browser.page_source
            soup = BeautifulSoup(html,'html.parser')
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



