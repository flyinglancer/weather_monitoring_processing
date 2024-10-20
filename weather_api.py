# import requests

# def get_weather_data(city, api_key):
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
#     response = requests.get(url)
#     data = response.json()
#     print(data)  # Print the response for debugging
#     return data

import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    print(f"Weather data for {city}:", data)  # For debugging
    return data
