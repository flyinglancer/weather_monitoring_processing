# Weather Monitoring Dashboard

## Overview

This project is a real-time weather monitoring dashboard that fetches data from the OpenWeatherMap API and displays it using a Dash web application. The dashboard provides insights into current weather conditions across major cities in India.

## Project Structure
weather_monitoring/
│

├── main.py # Backend script to fetch and process weather data

├── dash_app.py # Dash application for visualization

├── weather_api.py # Module for API interaction

├── data_processing.py # Module for processing weather data

├── alerting.py # Module for alert conditions

├── storage.py # Module for data storage

├── requirements.txt # Project dependencies

└── README.md # Project documentation


## Prerequisites

- Python 3.x: Ensure Python is installed on your system.
- OpenWeatherMap API Key: Sign up at OpenWeatherMap to obtain a free API key.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/weather_monitoring.git
   cd weather_monitoring
2. **Install Dependencies**:
    Use the requirements.txt file to install all necessary libraries:
    ```bash
    pip install -r requirements.txt
## Configuration
  API Key Setup:
    Open weather_api.py and replace 'your_actual_api_key_here' with your OpenWeatherMap API key.
# Usage
   Run the Backend Script:
    First, run the backend script to collect and process weather data:
  ```bash
    python main.py
```
This script will fetch and store weather data for specified cities. It uses modules like schedule to periodically update the data.
# Launch the Dash Application:
  Once the data is collected, launch the Dash app to visualize it:
  ```
python dash_app.py
```
Open your web browser and navigate to http://localhost:8050 to view the dashboard.

# Dependencies
* Dash: For building the interactive web application.
* Requests: To handle HTTP requests to the OpenWeatherMap API.
* Pandas: For data manipulation and analysis.
* Plotly: To create interactive plots within Dash.
* Schedule: For scheduling periodic tasks.

# Features
* Real-Time Data Fetching: Continuously fetches weather data for multiple cities.
* Interactive Dashboard: Visualizes temperature trends using Plotly graphs.
* Alert System: Notifies when certain weather conditions are met.
* Modular Design: Separates data fetching, processing, alerting, and visualization for maintainability.

# Troubleshooting
* Ensure your API key is valid and has not exceeded its usage limits.
* If the Dash app does not display, check that all dependencies are installed correctly and that no errors occur when running dash_app.py.
