import requests
import smtplib
import time

# 1. Location Coordinates (Nigeria)
MY_LAT = 9.081999
MY_LONG = 8.675277

# Your email configuration (Using your working Port 465 SSL network settings)
MY_EMAIL = "arthurreynolds2121@gmail.com"
PASSWORD = "fgvp bpmr wfvk vwlt"

def check_rain_forecast():
    # Base endpoint and parameters configured cleanly
    url = "https://api.open-meteo.com/v1/forecast"
    parameters = {
        "latitude": MY_LAT,
        "longitude": MY_LONG,
        "current": "is_day",          # 0 means night, 1 means day
        "hourly": "weather_code",     # Gets the upcoming hourly weather codes
        "timezone": "auto"            # Syncs with your local timezone automatically
    }

    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    data = response.json()

    # A. Check if it's currently dark out (is_day == 0 means it is nighttime)
    is_nighttime = data["current"]["is_day"] == 0

    # B. Get the upcoming weather codes and slice down to the next 12 hours
    all_hourly_codes = data["hourly"]["weather_code"]
    next_12_hours = all_hourly_codes[0:12]

    # C. Scan the 12-hour slice for rain codes
    # WMO Codes 51-67 and 80-86 represent drizzle or rain showers
    will_rain = False
    for code in next_12_hours:
        if 51 <= code <= 67 or 80 <= code <= 86 or 95 <= code <= 99:
            will_rain = True
            break

    # Return True ONLY if it's dark AND it's going to rain
    return will_rain and is_nighttime


print("Day 35 Weather Checker Active...")

try:
    if check_rain_forecast():
        print("Conditions met! It's dark and rain is coming. Sending email...")
        with smtplib.SMTP_SSL("://gmail.com", 465) as connection:
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="sylphie91@gmail.com",
                msg="Subject: Rain Alert! ☔\n\nIt is nighttime and the forecast predicts rain within the next 12 hours. Remember your umbrella!"
            )
        print("🎉 Success! Alert delivered to your inbox.")
    else:
        print("Check complete: Conditions not met. Either it's daylight, or no rain is forecasted.")

except Exception as error:
    print(f"An unexpected error occurred: {error}")
