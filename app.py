from flask import Flask,jsonify, request 
from flask_restful import Api, Resource
from selenium import webdriver
import cloudscraper as cfscrape
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api3": {"origins": "*"}})
api = Api(app)

class One(Resource):
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

class Two(Resource):
    @cross_origin(origin='*')
    def get(self,name):
        try:
            browser = webdriver.Chrome(options=options)
            wait = ui.WebDriverWait(browser, 5)
            url="https://animixplay.to/v1/"+name
            browser.get(url)
            iframe = wait.until(lambda browser: browser.find_element_by_id("iframeplayer"))
            tv=browser.switch_to.frame(iframe)
            try:
                wait.until(lambda browser: browser.find_element_by_css_selector("#videocontainer > div > div.plyr__video-wrapper > video > source"))
                html = browser.page_source
                soup = BeautifulSoup(html,'html.parser')
                st=soup.findAll('video' )#.getText()
                yu=st[0].find("source")['src']

            except:
                wait.until(lambda browser: browser.find_element_by_id("player_html5_api"))
                html = browser.page_source
                soup = BeautifulSoup(html,'html.parser')
                st=soup.findAll('video' )#.getText()
                yu=st[0]['src']

            return {'link': str(yu)}
        except:
            return 'fail'


api.add_resource(One, "/4Anime/<string:name>")
api.add_resource(Two, "/Animix/<string:name>")
if __name__ == "__main__":
    app.run(debug=True)



