import requests
from twilio.rest import Client
from decouple import config

# MY_LATITUDE = 37.5683
# MY_LONGITUDE = 126.9778
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/onecall?"
#                             f"lat={MY_LATITUDE}"
#                             f"&lon={MY_LONGITUDE}"
#                             f"&exclude=current,minutely,daily,alerts"
#                             f"&appid={MY_API}")


my_tokens = {
        "OWM_Endpoint": config("OWM_Endpoint", default=""),
        "MY_API": config("MY_API", default=""),
        "account_sid": config("account_sid", default=""),
        "auth_token": config("auth_token", default=""),
}


weather_params = {
    "lat": 7.1907,
    "lon": 125.4553,
    "appid": my_tokens,
    "exclude": "current,minutely,daily"
}

response = requests.get(my_tokens["OWM_Endpoint"], params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

code = weather_data["hourly"][0]["weather"][0]["id"]
condition_code = [code for item in weather_slice]

will_rain = False

for x in condition_code:
    if x < 700:
        will_rain = True

if will_rain:
    client = Client(my_tokens["account_sid"], my_tokens["auth_token"])
    message = client.messages \
        .create(
            body="Buddy bud bud, it's gonna rain today! Bring your umbrella",
            from_="",
            to=""
        )

