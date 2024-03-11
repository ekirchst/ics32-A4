# Evan
# ekirchst@uci.edu
# 59946460
import urllib
import json
from urllib import request, error
from abc import ABC, abstractmethod


class WebAPI(ABC):
    def _download_url(self, url: str) -> dict:
        try:
            response = None
            lol = None
            response = request.urlopen(url)
            json_results = response.read()
            lol = json.loads(json_results)

        except urllib.error.HTTPError as e:
            print('Failed to download')
            print('Status code: {}'.format(e.code))

        finally:
            if not response:
                response.close()

                return lol

    def set_apikey(self, apikey: str) -> None:
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def transclude(self, message: str) -> str:
        pass
