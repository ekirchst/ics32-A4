# Evan
# ekirchst@uci.edu
# 59946460
from urllib import request
import json as js
from datetime import datetime
from urllib.parse import quote
from WebAPI import WebAPI


class LastFM(WebAPI):
    '''
    Weather API Class Created to Interact with LastFM api
    '''

    def __init__(self) -> None:
        self.url = 'http://ws.audioscrobbler.com/2.0/'

    def load_data(self, artist="Harry Styles"):
        '''
        Function to Retrieve Certain Data from the LastFM API
        '''
        try:
            artist = quote(artist)
            addition = 'artist.getinfo'
            temp1 = f'{self.url}?method={addition}&artist={artist}'
            temp2 = f'&api_key={self.apikey}&format=json'
            link = f"{temp1}{temp2}"
            response = request.urlopen(link)
            re = js.loads(response.read())
            with open("lastfm.json", "w") as file:
                js.dump(re, file)
            artist_info = re['artist']
            self.artist_listeners = re['artist']['stats']['listeners']
            self.artist_playcount = re['artist']['stats']['playcount']
            return artist_info
        except request.URLError as e:
            print(f"Error: {e}")

    def transclude(self, message: str) -> str:
        '''
        Function to Replace Keyword "@lastfm" with Data from LastFM API
        '''
        temp = message.lower()
        if "@lastfm" in temp:
            new = temp.replace("@lastfm", self.artist_listeners)
            return new
