# import datetime as dt
import requests

#API_KEY = open('Sam_api', 'r).read()
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "0cd9590c5606f92e59d74999a6fa2ec7"
CITY = input("Enter the name of the city: ")

def kelvin_to_celsius(kelvin):
    celsius = kelvin-273.15
    return celsius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

x = response
if x['cod']!='404':
    y = x['main']

temp_kelvin = y['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)

# print(response)
# output = "The temperature in",CITY,"is: ",format(temp_celsius,".2f"),"℃"
print("The temperature in",CITY,"is: ",format(temp_celsius,".2f"),"℃")

# found = False
# if response.status_code == 404:
#     print("Invalid city: {}, Please check your city name".format(CITY))
# else:
#     print("output")