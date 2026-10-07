import requests
from datetime import datetime
import smtplib
import time

# 1. Your actual Location Coordinates (Nigeria)
MY_LAT = 9.081999
MY_LONG = 8.675277

# Your credentials
MY_EMAIL = "arthurreynolds2121@gmail.com"
PASSWORD = "fgvp bpmr wfvk vwlt"


def is_iss_overhead():
    # Headers prevent the server from blocking your connection when looping
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    # Using the highly stable alternative ISS API tracker
    response = requests.get(url="https://wheretheiss.at", headers=headers)
    response.raise_for_status()
    data = response.json()

    # Extract coordinates directly from top-level lowercase keys
    iss_latitude = float(data["latitude"])
    iss_longitude = float(data["longitude"])

    # Check if the ISS position is within +5 or -5 degrees of your position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://sunrise-sunset.org", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Correct slicing logic to isolate the hour digit cleanly
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Using utcnow() hour to perfectly match the Sunrise/Sunset API's UTC data format
    time_now = datetime.utcnow().hour

    # Check if it is currently dark out
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


# Main execution loop
print("ISS Tracking Script Started... Checking position every 60 seconds.")

while True:
    try:
        if is_iss_overhead() and is_night():
            # Using your sturdier, network-validated SMTP configurations
            with smtplib.SMTP_SSL("://gmail.com", 465) as connection:
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="sylphie91@gmail.com",
                    msg="Subject:Look Up! 🛰️\n\nThe ISS is passing over your position right now!"
                )
            print("Email alert successfully sent!")
        else:
            print(f"Checked at {datetime.now().strftime('%H:%M:%S')}: ISS is not overhead or it is still daylight.")

    except requests.exceptions.RequestException as error:
        # Prevents the entire program from crashing if your network fluctuates temporarily
        print(f"Network glitch occurred: {error}. Trying again on the next loop.")

    # Pause execution for 60 seconds before looping again
    time.sleep(60)
