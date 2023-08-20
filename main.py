import requests
from twilio.rest import Client
import os

account_sid = 'AC09c30700ea699e92c03658dc4aba3894'
auth_token = os.environ.get("AUTH_TOKEN")
to_number = os.environ.get("TO_NUMBER")
from_number = os.environ.get("FROM_NUMBER")

api_key = os.environ.get("OWM_API_KEY") 
api_call = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
        "lat": 28.54,
        "lon": -81.38,  # lat/lon for Orlando, FL
        "appid": api_key,
        "cnt": 5
    }

response = requests.get(url=api_call, params=parameters)
response.raise_for_status()
data = response.json()

rain_today = False
for i in range(0, 5):
    weather_code = data["list"][i]["weather"][0]["id"]
    if weather_code < 600:
        rain_today = True

if rain_today:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=from_number,
        body="It's going to rain today. Take your Umbrella!",
        to=to_number
    )
    print(message.status)