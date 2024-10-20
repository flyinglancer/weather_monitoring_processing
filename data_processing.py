# import pandas as pd
# from datetime import datetime

# def kelvin_to_celsius(kelvin_temp):
#     return kelvin_temp - 273.15

# def process_weather_data(weather_data):
#     if 'main' not in weather_data or 'weather' not in weather_data:
#         print("Error: Required data not found in the API response.")
#         return None
    
#     temperature_kelvin = weather_data['main']['temp']
#     temperature_celsius = kelvin_to_celsius(temperature_kelvin)
#     return {
#         'temp': temperature_celsius,
#         'main': weather_data['weather'][0]['main']
#     }


# def calculate_daily_summary(weather_records):
#     df = pd.DataFrame(weather_records)
#     dominant_condition = df['main'].mode()[0]
#     condition_counts = df['main'].value_counts()
#     reason = f"Dominant condition is {dominant_condition} (occurred {condition_counts[dominant_condition]} times out of {len(df)} records)"
    
#     daily_summary = {
#         'date': datetime.now().strftime('%Y-%m-%d'),
#         'average_temp': df['temp'].mean(),
#         'max_temp': df['temp'].max(),
#         'min_temp': df['temp'].min(),
#         'dominant_condition': dominant_condition,
#         'dominant_condition_reason': reason
#     }
#     return daily_summary

import pandas as pd
from datetime import datetime

def kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15

def process_weather_data(weather_data):
    if 'main' not in weather_data or 'weather' not in weather_data:
        print("Error: Required data not found in the API response.")
        return None
    
    temperature_kelvin = weather_data['main']['temp']
    temperature_celsius = kelvin_to_celsius(temperature_kelvin)
    return {
        'temp': temperature_celsius,
        'main': weather_data['weather'][0]['main']
    }

def calculate_daily_summary(weather_records):
    df = pd.DataFrame(weather_records)
    dominant_condition = df['main'].mode()[0]
    condition_counts = df['main'].value_counts()
    reason = f"Dominant condition is {dominant_condition} (occurred {condition_counts[dominant_condition]} times out of {len(df)} records)"
    
    daily_summary = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'average_temp': df['temp'].mean(),
        'max_temp': df['temp'].max(),
        'min_temp': df['temp'].min(),
        'dominant_condition': dominant_condition,
        'dominant_condition_reason': reason
    }
    return daily_summary
