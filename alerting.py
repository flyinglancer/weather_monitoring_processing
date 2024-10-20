# def check_alert_conditions(current_temp, threshold):
#     if current_temp > threshold:
#         return f"Alert: Temperature exceeds threshold! Current temperature: {current_temp}°C"
#     return None

def check_alert_conditions(current_temp, threshold):
    if current_temp > threshold:
        return f"Alert: Temperature exceeds threshold! Current temperature: {current_temp:.1f}°C"
    return None
