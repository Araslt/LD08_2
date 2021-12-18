from time import sleep
import requests, urllib.request
import json
import random

# viskas is thingspeak.com
write_api_key = 'IRMPN4OE1F447726'
read_api_key = 'B56BF9I7H9M9BCH7'
baseURL_temp = 'http://api.thingspeak.com/update?api_key=' + write_api_key + '&field1='
baseURL_hum = 'http://api.thingspeak.com/update?api_key=' + write_api_key + '&field2='

# viskas is openweathermap.org
weather_api_key = "757d1bc7fac0c64cc7dc0897d2bdc41b"
city_name = "vilnius"
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + weather_api_key
response = requests.get(weather_url)
weather_data = response.json()

# print(baseURL)

count = 0
while count < 10:
    if weather_data['cod'] == 200:
        kelvin = 273.15  # Temperature shown here is in Kelvin and I will show in Celsius
        temp = int(weather_data['main']['temp'] - kelvin)
        humidity = weather_data['main']['humidity']
        print(f"Temperatura: {temp} C")
        print(f"Dregme: {humidity}")
    else:
        print(f"City Name: {city_name} was not found!")
    f1 = urllib.request.urlopen(baseURL_temp + str(temp))
    f2 = urllib.request.urlopen(baseURL_hum + str(humidity))
    f1.read()
    f2.read()
    f1.close()
    f2.close()
    sleep(16)
    count = count +1

print("Program has ended")
