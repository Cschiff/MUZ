'''
Created on Apr 29, 2017

@author: Christian
'''

import json
import requests 

username = "06a1ee12-581e-456f-90bf-a13383655a24"
password = "D5SBTi9fk4"
host ="twcservice.mybluemix.net"
port = 443

lat  = -45.83
long = -67.49

current_conditions = "/v1/geocode/" + str(lat) + "/" + str(long) + "/observations.json"
forecast_48hs = "/v1/geocode/" + str(lat) + "/" + str(long) + "/forecast/hourly/48hour.json"
almanac = "/v1/geocode/" + str(lat) + "/" + str(long) + "/almanac/monthly.json"

units = "m"
lang = "es-MX"
hours = 23
start_date = 1
end_date = 5

common_props = "units=" + units + "&" + "language=" + lang
props_current_conditions = "?" + common_props
props_forecast = props_current_conditions
props_almanac = "?start=" + str(start_date) + "&" "end=" + str(end_date) + common_props
props_historic = "?" + str(hours) + common_props

def generate_url(query, props):
  url = "https://" + username + ":" + password + "@twcservice.mybluemix.net:" + str(port) + "/api/weather" + query + props
  return url

url_current_conditions = generate_url(current_conditions, props_current_conditions)
url_forecast_48 = generate_url(forecast_48hs, props_forecast)
url_almanac = generate_url(almanac, props_almanac)

def api_request(url):

    jsonurl= requests.get(url)

    data_string = json.loads(jsonurl.text)
    
    print(data_string)

api_request(url_current_conditions)
