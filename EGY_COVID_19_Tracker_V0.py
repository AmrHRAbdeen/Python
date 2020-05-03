#####################################
# Needed Packages:
# ---------------------
# pandas -> DataFrame [ pip install pandas ]
# requests -> Request [ pip install requests ]
#####################################
import pandas as pd
import requests


# Send HTTP GET reuest to COVID_19 Server

URL= "http://www.worldometers.info/coronavirus/"
reqRes = requests.get(URL)
print(reqRes)