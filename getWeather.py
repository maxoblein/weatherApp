#code used to get weather from a given location

#import dependencies
from urllib import response
import requests

if __name__ == "__main__":
    apiKey = "1237eb6e810cf3862b15a8d7f7582700"
    defaultURL = "http://api.openweathermap.org/data/2.5/weather?"

    #get city from commandline
    #cityName = input("Enter city name: ")
    cityName = "Hemel Hempstead"

    #query open wetaher map api
    requestURL = defaultURL+"appid="+apiKey+"&q="+cityName
    response = requests.get(requestURL)

    #process response
    data = response.json()

    if data["cod"] != "404":
        y = data["main"]

        current_temperature = y["temp"]
        z = data["weather"]

        weather_description = z[0]["description"]

        print(" Temperature (in celcius) = " +
                        str(current_temperature-273) +
            "\n description = " +
                        str(weather_description))

    else:
        print(" City Not Found ")
    