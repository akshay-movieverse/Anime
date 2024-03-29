from flask import Flask,jsonify, request 
from flask_restful import Api, Resource
from selenium import webdriver
import cloudscraper as cfscrape
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/api3": {"origins": "*"}})
api = Api(app)

def load_chrome_driver():

      options = Options()

      options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')

      options.add_argument('--headless')
      options.add_argument('--disable-gpu')
      options.add_argument('--no-sandbox')
      #options.add_argument('--remote-debugging-port=9222')
      #options.add_argument('--proxy-server='+proxy)

      return webdriver.Chrome(executable_path=str(os.environ.get('CHROMEDRIVER_PATH')), chrome_options=options)

class One(Resource):
    @cross_origin(origin='*')
    def get(self,name):
        try:
            browser = webdriver.PhantomJS()
            url="https://4anime.gg/"+name
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
    
    def get(self,ver,name,ep):
        try:
            browser = load_chrome_driver()
            wait = ui.WebDriverWait(browser, 5)
            url="https://animixplay.to/"+ver+"/"+name+"/"+ep
            browser.get(url)
            iframe = wait.until(lambda browser: browser.find_element_by_id("iframeplayer"))
            tv=browser.switch_to.frame(iframe)
            try:
                wait.until(lambda browser: browser.find_element_by_css_selector("#videocontainer > div > div.plyr__video-wrapper > video > source"))
                html = browser.page_source
                soup = BeautifulSoup(html,'html.parser')
                st=soup.findAll('video' )#.getText()
                yu=st[0].find("source")['src']
                browser.close()

            except:
                wait.until(lambda browser: browser.find_element_by_id("player_html5_api"))
                html = browser.page_source
                soup = BeautifulSoup(html,'html.parser')
                st=soup.findAll('video' )#.getText()
                yu=st[0]['src']
                browser.close()

            return {'link': str(yu)}
        except:
            return 'fail'


api.add_resource(One, "/4Anime/<string:name>")
api.add_resource(Two, "/Animix/<string:ver>/<string:name>/<string:ep>")
if __name__ == "__main__":
    app.run(debug=True)



