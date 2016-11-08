#!flask/bin/python
from flask import Flask
import requests, json

app = Flask(__name__)

@app.route('/')
def index():
    return "setlist.fm proxy api"

@app.route('/api/search/<string:artist>')
def search(artist):
    #artist = 'M83'
    url = 'http://api.setlist.fm/rest/0.1/search/artists.json?artistName='+artist
    response = requests.get(url)
    if(response.ok):
        parsedResponse = json.loads(response.content)
        return(parsedResponse["artists"]["artist"][0]["@name"])


if __name__ == '__main__':
    app.run(debug=True)
