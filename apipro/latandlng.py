import requests
from datetime import datetime
my_lat = 20.593683
my_lng = 78.962883

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    
    response.raise_for_status()
    
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if my_lat-5 <= iss_latitude <=my_lat+5 and my_lng <= iss_longitude <= my_lng+5:
        return True

def is_night():

    parameters = {
        "lat":my_lat,
        "lng":my_lng,
        "formatted":0,
    }
    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) 
    #!"T" itself is removed during the splitting process
    
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    time_now = datetime.now().hour
    
    if time_now>= sunset or time_now<=sunset:
        return True
def final():
    if is_night() and is_iss_overhead():
        return f"This is the correct time"
    else:
        return f"Not correct time"
    
print(final())