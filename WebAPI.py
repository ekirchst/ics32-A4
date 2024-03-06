# Evan
# ekirchst@uci.edu
# 59946460

class OpenWeather:
    '''
    Weather API Class Created to Interact with OpenWeather api
    '''
    def __init__(self, zipcode, ccode):
        '''
        Initializes OpenWeather Object
        Takes in zipcode and ccode
        '''
        self.zip_code = zipcode
        self.c_code = ccode
        