'''
Created on Apr 29, 2017

@author: Christian
'''

import json
import requests 
from bs4 import BeautifulSoup

username = "06a1ee12-581e-456f-90bf-a13383655a24"
password = "D5SBTi9fk4"
host ="twcservice.mybluemix.net"
port = 443
#url = "https://06a1ee12-581e-456f-90bf-a13383655a24:D5SBTi9fk4@twcservice.mybluemix.net"

lat = -45.83#4656
long= -67.49#0327
forecast_two_day ="/v1/geocode/"+str(lat)+"/"+str(long)+"/forecast/hourly/48hour.json"
propForecast="?units=m&language=es-MX"
hours=23 
almanac="/v1/geocode/"+str(lat)+"/"+str(long)+"/almanac/monthly.json"
propAlmanac="?start=01&end=05units=m&language=es-MX"
propHistor="?hours="+str(hours)+"units=m&language=es-MX"
url = "https://"+username+":"+password+"@twcservice.mybluemix.net:443/api/weather"+forecast_two_day+propForecast

def introduction2():
   
    jsonurl= requests.get(url)

    data_string = json.loads(jsonurl.text)
    

    for x in range(0,5):
        print(data_string)
    pass
       
 
introduction2() 


