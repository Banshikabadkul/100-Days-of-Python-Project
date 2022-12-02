
import requests
api_key = '748c19277ff76e2cf44a2c8ea9595aed'
owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters= {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}
response = requests.get(owm_endpoint, params=parameters)
response.raise_for_status()
print(response)