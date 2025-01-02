import requests
from datetime import datetime
my_lat = 20.593683
my_lng = 78.962883
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# if response.status_code != 200:
#     raise Exception("Bad response")
# elif response.status_code == 401:
#     raise Exception("you are not authorized to access this data")

# response.raise_for_status()
# data = response.json()["iss_position"]
# print(data)

parameters = {
    "lat":my_lat,
    "lng":my_lng,
    "formatted":0,
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print("\n")
print(sunrise.split("T")[1].split(":"))

# current time

time_now = datetime.now()
print(time_now)