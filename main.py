# import schedule
# import time
# from weather_api import get_weather_data
# from data_processing import process_weather_data, calculate_daily_summary
# from alerting import check_alert_conditions
# from storage import store_weather_data, store_daily_summary, get_historical_data

# API_KEY = 'feec9f4e44103a6e0728e2ec2deb6a7c'
# CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
# THRESHOLD_TEMP = 35

# def job():
#     all_weather_records = []

#     for city in CITIES:
#         weather_data = get_weather_data(city, API_KEY)
#         processed_data = process_weather_data(weather_data)

#         if processed_data is not None:
#             all_weather_records.append(processed_data)
#             store_weather_data(city, processed_data)
#             alert = check_alert_conditions(processed_data['temp'], THRESHOLD_TEMP)
#             if alert:
#                 print(alert)  # Print the alert message

#     if all_weather_records:
#         daily_summary = calculate_daily_summary(all_weather_records)
#         if daily_summary:
#             store_daily_summary(daily_summary)
    
#     print("Job completed at:", time.strftime("%Y-%m-%d %H:%M:%S"))  # Add this line to confirm job execution

# def main():
#     print("Weather monitoring system started. Press Ctrl+C to exit.")
#     schedule.every(1).minutes.do(job)  # Changed from every hour to every minute
    
#     # Run the job immediately when the script starts
#     job()
    
#     while True:
#         try:
#             schedule.run_pending()
#             time.sleep(1)
#         except KeyboardInterrupt:
#             print("\nExiting the program...")
#             break

# if __name__ == "__main__":
#     main()


import schedule
import time
from weather_api import get_weather_data
from data_processing import process_weather_data, calculate_daily_summary
from alerting import check_alert_conditions
from storage import create_tables, store_weather_data, store_daily_summary

API_KEY = 'feec9f4e44103a6e0728e2ec2deb6a7c'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
THRESHOLD_TEMP = 35

def job():
    all_weather_records = []

    for city in CITIES:
        weather_data = get_weather_data(city, API_KEY)
        processed_data = process_weather_data(weather_data)

        if processed_data is not None:
            all_weather_records.append(processed_data)
            store_weather_data(city, processed_data)
            alert = check_alert_conditions(processed_data['temp'], THRESHOLD_TEMP)
            if alert:
                print(alert)

    if all_weather_records:
        daily_summary = calculate_daily_summary(all_weather_records)
        if daily_summary:
            store_daily_summary(daily_summary)
    
    print("Job completed at:", time.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    create_tables()
    print("Weather monitoring system started. Press Ctrl+C to exit.")
    schedule.every(1).minutes.do(job)
    
    job()  # Run immediately on start
    
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nExiting the program...")
            break

if __name__ == "__main__":
    main()

