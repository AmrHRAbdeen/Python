#############################################################
# Developing a script to GET my Country COVID_19 statistics 
#############################################################
import requests
import pandas


URL ="https://www.worldometers.info/coronavirus/"
print("Getting Egypt COVID_19 statistics ...")
pageResponse = requests.get(URL)
pageContent = pageResponse.text
#print(pageContent)
dataFrame=  pandas.read_html(pageContent)
#print(dataFrame)
#print(dataFrame[0].loc[0][0])
for cnt in range(0,200):
    if(dataFrame[0].loc[cnt][0] == 'Egypt'):
        print("Egypt index is ={}".format(cnt))
        print("Egypt No of total cases of COVID_19 is :{}".format(dataFrame[0].loc[cnt][1]))
        print("Egypt No of New cases of COVID_19 is : {}".format(dataFrame[0].loc[cnt][2])) 
