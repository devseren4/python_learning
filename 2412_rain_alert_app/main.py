import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OWM_EndPoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
from_ = os.getenv("FROM")
to = os.getenv("TO")

weather_params = {
    "lat": 41.125912,
    "lon": 16.872110,
    "appid": api_key,
    "cnt": 4,
}

respons = requests.get(OWM_EndPoint, params=weather_params)
respons.raise_for_status()

weather_data = respons.json()
weather_status = int(weather_data["list"][0]["weather"][0]["id"])


condition_codes = [code["weather"][0]["id"] for code in weather_data["list"]]

will_rain = False
for code in condition_codes:
    if code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=from_,
        to=to,
    )
    print(message.status)
