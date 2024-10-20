# import sqlite3
# import pandas as pd
# from datetime import datetime

# def store_weather_data(city, data):
#     conn = sqlite3.connect('weather_data.db')
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS WeatherData (
#             date TEXT,
#             city TEXT,
#             temp REAL,
#             main TEXT
#         )
#     ''')
    
#     # Convert the current timestamp to a string
#     current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
#     # Ensure all values are of the correct type
#     city = str(city)
#     temp = float(data['temp'])
#     main = str(data['main'])
    
#     c.execute('''
#         INSERT INTO WeatherData (date, city, temp, main) 
#         VALUES (?, ?, ?, ?)
#     ''', (current_time, city, temp, main))
    
#     conn.commit()
#     conn.close()

# def store_daily_summary(summary):
#     conn = sqlite3.connect('weather_data.db')
#     c = conn.cursor()
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS DailySummary (
#             date TEXT,
#             average_temp REAL,
#             max_temp REAL,
#             min_temp REAL,
#             dominant_condition TEXT
#         )
#     ''')
#     c.execute('''
#         INSERT INTO DailySummary (date, average_temp, max_temp, min_temp, dominant_condition) 
#         VALUES (?, ?, ?, ?, ?)
#     ''', (summary['date'], summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
#     conn.commit()
#     conn.close()

# def get_historical_data(start_date, end_date):
#     conn = sqlite3.connect('weather_data.db')
#     query = f"""
#     SELECT date, average_temp, max_temp, min_temp, dominant_condition
#     FROM DailySummary
#     WHERE date BETWEEN '{start_date}' AND '{end_date}'
#     ORDER BY date
#     """
#     df = pd.read_sql_query(query, conn)
#     conn.close()
#     return df

import sqlite3
import pandas as pd
from datetime import datetime

def create_tables():
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS WeatherData (
            date TEXT,
            city TEXT,
            temp REAL,
            main TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS DailySummary (
            date TEXT,
            average_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_weather_data(city, data):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute('''
        INSERT INTO WeatherData (date, city, temp, main) 
        VALUES (?, ?, ?, ?)
    ''', (current_time, str(city), float(data['temp']), str(data['main'])))
    conn.commit()
    conn.close()

def store_daily_summary(summary):
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO DailySummary (date, average_temp, max_temp, min_temp, dominant_condition) 
        VALUES (?, ?, ?, ?, ?)
    ''', (summary['date'], summary['average_temp'], summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()

def get_historical_data(start_date, end_date):
    conn = sqlite3.connect('weather_data.db')
    query = f"""
    SELECT date, AVG(temp) as average_temp, MAX(temp) as max_temp, MIN(temp) as min_temp
    FROM WeatherData
    WHERE date BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY date
    ORDER BY date
    """
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
