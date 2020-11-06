import requests
import json
 
url = "http://api.openweathermap.org/data/2.5/weather"
querystring = {"q":"London","appid":"00d17476610735c975ff"}
 
response = requests.request("GET", url, params=querystring)
 
temps = json.loads(response.text)
print(json.dumps(temps, indent=4, sort_keys=True))
