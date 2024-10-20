# import dash
# from dash import dcc, html, Input, Output
# import plotly.express as px
# import pandas as pd
# from storage import get_historical_data

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     html.H1('Weather Monitoring Dashboard'),
    
#     dcc.DatePickerRange(
#         id='date-range',
#         start_date_placeholder_text="Start Date",
#         end_date_placeholder_text="End Date",
#         calendar_orientation='horizontal',
#     ),
    
#     dcc.Graph(id='temperature-trend'),
    
#     dcc.Graph(id='weather-conditions-pie'),
    
#     html.Div(id='alerts')
# ])

# @app.callback(
#     [Output('temperature-trend', 'figure'),
#      Output('weather-conditions-pie', 'figure'),
#      Output('alerts', 'children')],
#     [Input('date-range', 'start_date'),
#      Input('date-range', 'end_date')]
# )
# def update_graphs(start_date, end_date):
#     df = get_historical_data(start_date, end_date)
    
#     temp_fig = px.line(df, x='date', y=['average_temp', 'max_temp', 'min_temp'],
#                        labels={'value': 'Temperature (°C)', 'variable': 'Temperature Type'},
#                        title='Temperature Trends')
    
#     condition_counts = df['dominant_condition'].value_counts()
#     pie_fig = px.pie(values=condition_counts.values, names=condition_counts.index,
#                      title='Dominant Weather Conditions')
    
#     alerts = []
#     for _, row in df.iterrows():
#         if row['max_temp'] > 35:
#             alerts.append(html.P(f"Alert: High temperature of {row['max_temp']}°C on {row['date']}"))
    
#     return temp_fig, pie_fig, alerts

# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from storage import get_historical_data
from datetime import datetime, timedelta

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Weather Monitoring Dashboard'),
    
    dcc.DatePickerRange(
        id='date-range',
        start_date=datetime.now().date() - timedelta(days=7),
        end_date=datetime.now().date(),
        display_format='YYYY-MM-DD'
    ),
    
    dcc.Graph(id='temperature-trend'),
    
    dcc.Graph(id='weather-conditions-pie'),
    
    html.Div(id='alerts')
])

@app.callback(
    [Output('temperature-trend', 'figure'),
     Output('weather-conditions-pie', 'figure'),
     Output('alerts', 'children')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_graphs(start_date, end_date):
    df = get_historical_data(start_date, end_date)
    
    temp_fig = px.line(df, x='date', y=['average_temp', 'max_temp', 'min_temp'],
                       labels={'value': 'Temperature (°C)', 'variable': 'Temperature Type'},
                       title='Temperature Trends')
    
    condition_counts = df['dominant_condition'].value_counts()
    pie_fig = px.pie(values=condition_counts.values, names=condition_counts.index,
                     title='Dominant Weather Conditions')
    
    alerts = []
    for _, row in df.iterrows():
        if row['max_temp'] > 35:
            alerts.append(html.P(f"Alert: High temperature of {row['max_temp']}°C on {row['date']}"))
    
    return temp_fig, pie_fig, alerts

if __name__ == '__main__':
    app.run_server(debug=True)
