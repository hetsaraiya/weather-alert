
import requests
from pushbullet import PushBullet

LONG = "longitude of your city"
LAT = "latitude of your city"


Weather_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"


api_key = "your openweathermap api key"
access_token = "your pushbullet key"


weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(Weather_Endpoint, params=weather_params)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = weather_data["hourly"][0]["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain == True:
    pb = PushBullet(access_token)
    print(weather_data["hourly"][0]["weather"][0]["main"])
    push = pb.push_note(weather_data["hourly"][0]["weather"][0]["main"], "bring your umbrella cause it's gonna rain")
else:
    print("feel free")
    print(weather_data["hourly"][0]["weather"][0]["main"])
