# Evan
# ekirchst@uci.edu
# 59946460
from urllib import request
import json as js
from datetime import datetime
from urllib.parse import quote


class LastFM:

    def __init__(self) -> None:
        self.url = 'http://ws.audioscrobbler.com/2.0/'

        
    def set_apikey(self, apikey:str) -> None:
        self.apikey = apikey
    
    def get_artist_info(self, artist):
        try:
            artist = quote(artist)
            addition = 'artist.getinfo'
            link = f'{self.url}?method={addition}&artist={artist}&api_key={self.apikey}&format=json'
            response = request.urlopen(link)
            re = js.loads(response.read())
            with open("lastfm.json", "w") as file:
                js.dump(re, file)
            artist_info = re['artist']
            self.artist_listeners = re['artist']['stats']['listeners'].strip()
            self.artist_playcount = re['artist']['stats']['playcount'].strip()
            return artist_info
        except request.URLError as e:
            print(f"Error: {e}") 
