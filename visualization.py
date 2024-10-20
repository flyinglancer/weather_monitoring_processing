import matplotlib.pyplot as plt

def plot_temperature_trends(daily_summaries):
    if not daily_summaries:
        print("No data to plot.")
        return
    
    dates = [summary['date'] for summary in daily_summaries]
    temps = [summary['average_temp'] for summary in daily_summaries]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o')
    plt.title('Average Temperature Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (C)')
    plt.grid(True)
    plt.show()  # Ensure this is included to display the plot
