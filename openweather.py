import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key ="36488cb41a0f3197364de1c4915e1643"

account_sid = "AC866a46c56fbebab4a434bb0c892cc52f"
auth_token = "9526abf498ddd394d9e75a6d755da17d"

weather_params={
    "lat":7.873054,
    "lon":80.771797,
    "appid":api_key,
    "cnt":4,
}
response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
data = response.json()
# print(data["list"][0]["weather"][0])

will_rain=False
for hr_data in data["list"]:
    cond_code=(hr_data["weather"][0]["id"])
    if cond_code<700:
        will_rain=True
    # if cond_code<700:
    #     print("bring an umbrella")
    # else:
    #     print("no need of umbrella")
# ! this is of 12 hours 
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Bring or take a umbrella with you today",
    from_="+12316675124",
    to="+917982886835",
    )
    print(message.status)