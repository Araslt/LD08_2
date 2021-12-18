import requests
import json

api_key = "757d1bc7fac0c64cc7dc0897d2bdc41b"
# city_name = input("Enter city name: ")
city_name = "vilnius"
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key

# Get the response from weather url
response = requests.get(weather_url)

# response will be in json format and we need to change it to pythonic format
weather_data = response.json()

if weather_data['cod'] == 200:
    kelvin = 273.15 # Temperature shown here is in Kelvin and I will show in Celsius
    temp = int(weather_data['main']['temp'] - kelvin)
    # humidity = weather_data['main']['humidity']

    # print(f"Weather Information for City: {city_name}")
    print(f"Temperatura: {temp} C")
    # print(f"Dregme: {humidity}")

else:
    print(f"City Name: {city_name} was not found!")