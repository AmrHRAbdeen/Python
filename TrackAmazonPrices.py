###############################################################
# This script is used to get specific content from Webpages...
# @Author: Amr Abdeen
# @Date: 23 March,2020
# COVID-19 CRISIS!
###############################################################
import requests
### Beautiful Soup is a Python package for parsing HTML and XML documents.###
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display_html
import facebook


URL="https://www.worldometers.info/coronavirus/"

EgyptCOVID_19Tracker= requests.get(URL)

print(EgyptCOVID_19Tracker)
html_string = EgyptCOVID_19Tracker.text

# Converting HTML text to data Frames 
dfs = pd.read_html(html_string,header=0)
df=dfs[0]


if (df.loc[0][0]) == 'China':
    print("Got it")

#print all Country names
for row in range(0,1):
    for cnt in range(0,150):
        if(df.loc[cnt][0] == 'Egypt'):
            print("Egypt is here")
            print("Egypr index is: {}".format(cnt))
            print("Getting the number of total cases:{}".format(df.loc[cnt][1]))
            print("Getting the number of New cases:{}".format(df.loc[cnt][2]))
        #print(df.loc[cnt][0])