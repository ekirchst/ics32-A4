# Evan
# ekirchst@uci.edu
# 59946460

from pathlib import Path
import ui as ui
import admin as admin
import user as user
import OpenWeather as opw
# port = 168.235.86.101


if __name__ == "__main__":
    zipcode = "92697"
    ccode = "US"
    apikey = 'a3049970138b25f903d606cc94d57614'

    open_weather = opw.OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    open_weather.load_data()

    print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
    print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
    print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
    print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
    print(f"The current weather for {zipcode} is {open_weather.description}")
    print(f"The current humidity for {zipcode} is {open_weather.humidity}")
    print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")

    '''
    if ui.user() == 1:
        admin.start()
    else:
        user.comm_list()
        user.start()
    '''