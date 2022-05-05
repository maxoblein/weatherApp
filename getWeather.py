#code used to get weather from a given location

#import dependencies
from urllib import response
import requests
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def getWeather(cityName, countryCode):
    with open('key.txt') as f:
        key = f.readline()
    apiKey = key
    defaultURL = "http://api.openweathermap.org/data/2.5/weather?"

    #query open wetaher map api
    requestURL = defaultURL+"appid="+apiKey+"&q="+cityName+","+countryCode
    response = requests.get(requestURL)

    #process response
    data = response.json()

    if data["cod"] != "404":
        
        #build temperature variables
        y = data["main"]
        current_temperature = np.round(y["temp"] -273,2)
        maxTemp = np.round(y["temp_max"]-273,2)
        minTemp = np.round(y["temp_min"]-273,2)
        humidity = y["humidity"]
        
        #build weather variables
        z = data["weather"]
        weather_description = z[0]["description"]
        weather_icon = z[0]["icon"]

        #build descriptor variables
        sys = data['sys']
        city_name = data['name']
        country_code = sys['country']


        info = {'temp':current_temperature, 'maxTemp':maxTemp, 'minTemp':minTemp, 'humidity': humidity, 'description':weather_description, 'name': city_name, 'country':country_code, 'icon':weather_icon}

    else:
        info = {}

    return info



if __name__ == "__main__":
    print('hi')
    info = getWeather('Hemel Hempstead','GB')
    icon = info.get('icon')
    icon_url =  'http://openweathermap.org/img/wn/'+ icon + '@2x.png'
    im = Image.open(requests.get(icon_url,stream=True).raw)
    plt.imshow(im)
    plt.show()
