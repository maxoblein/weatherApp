#code used to get weather from a given location

#import dependencies
from urllib import response
import requests

def getWeather(cityName, countryCode):
    apiKey = "1237eb6e810cf3862b15a8d7f7582700"
    defaultURL = "http://api.openweathermap.org/data/2.5/weather?"

    #query open wetaher map api
    requestURL = defaultURL+"appid="+apiKey+"&q="+cityName+","+countryCode
    response = requests.get(requestURL)

    #process response
    data = response.json()

    if data["cod"] != "404":
        
        #build temperature variables
        y = data["main"]
        current_temperature = y["temp"]
        maxTemp = y["temp_max"]
        minTemp = y["temp_min"]
        humidity = y["humidity"]
        
        #build weather variables
        z = data["weather"]
        weather_description = z[0]["description"]
        weather_icon = z[0]["icon"]

        #build descriptor variables
        sys = data['sys']
        city_name = sys['name']
        country_code = sys['country']


        info = {'temp':current_temperature, 'maxTemp':maxTemp, 'minTemp':minTemp, 'humidity': humidity, 'description':weather_description, 'name': city_name, 'country':country_code}

    else:
        info = {}

    return info



    