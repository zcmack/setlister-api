#!flask/bin/python
from flask import Flask, jsonify
import requests, json

app = Flask(__name__)

@app.route('/')
def index():
    return "setlist.fm proxy api"

@app.route('/api/search/artist/<string:artist>')
def artistSearch(artist):
    #artist = 'M83'
    url = 'http://api.setlist.fm/rest/0.1/search/artists.json?artistName='+artist
    response = requests.get(url)
    if(response.ok):
        parsedResponse = json.loads(response.content)
        return(jsonify(parsedResponse["artists"]["artist"]))

@app.route('/api/search/setlists/<string:mbid>')
def setlistSearch(mbid):
    url = 'http://api.setlist.fm/rest/0.1/search/setlists.json?artistMbid='+mbid
    response = requests.get(url)
    if(response.ok):
        parsedResponse = json.loads(response.content)
        return(jsonify(parsedResponse))



if __name__ == '__main__':
    app.run(debug=True)
