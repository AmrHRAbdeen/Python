######################################################
# Developing a script to GET EGYPT COVID_19 Stats 
######################################################
import pandas
import requests

# URL for COVID_19 Stats
URL = "https://www.worldometers.info/coronavirus/"
# GET request to URL
requestRes = requests.get(URL)
pageContent = requestRes.text
#print(pageContent)
# Pandas used to convert HTML tables into dataFrames
dataFrames = pandas.read_html(pageContent)
#print(dataFrames)
#access table of interest 
dataFrame = dataFrames[0]

# Length of Rows 
rowsLen = dataFrame.index 
print(rowsLen)
# Search for Egypt in DataFrame
for cnt in range(0, len(rowsLen[1])):
    pass
