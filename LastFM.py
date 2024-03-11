# Evan
# ekirchst@uci.edu
# 59946460
from urllib import request
import json as js
from datetime import datetime
from urllib.parse import quote
from WebAPI import WebAPI


class LastFM(WebAPI):

    def __init__(self) -> None:
        self.url = 'http://ws.audioscrobbler.com/2.0/'

    def load_data(self, artist="Harry Styles"):
        try:
            artist = quote(artist)
            addition = 'artist.getinfo'
            link = f'{self.url}?method={addition}&artist={artist}&api_key={self.apikey}&format=json'
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
        if "@L" in message:
            new = message.replace("@LastFM", self.artist_listeners)
            return new
        if "@l" in message:
            new = message.replace("@lastFM", self.artist_listeners)
            return new
