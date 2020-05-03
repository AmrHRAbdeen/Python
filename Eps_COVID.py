import pandas
import requests


URL="https://www.worldometers.info/coronavirus/"

print("Getting Egypt Statistics ... ")
reqResponse=requests.get(URL)

pageContent=reqResponse.text

# Convert HTML tables to Pandas DataFrames
dataFrames = pandas.read_html(pageContent)
# Get Specific table/DataFrame
dataFrame = dataFrames[0]
# Get length of Rows/Countries 
index=dataFrame.index
num=len(index)
# Search for Egypt
for cnt in range (0,len(index)):
    if dataFrame.loc[cnt][0] == 'Egypt':
        totalInfected=dataFrame.loc[cnt][1]
        print("Total Number of infected Cases in Egypt:{}".format(totalInfected))
        EgyNewCases=dataFrame.loc[cnt][2]
        # Checking if there's new data or not using isnull() function
        newVal=dataFrame.isnull()
        if(newVal.loc[cnt][2] == True):
            print("Data has not yet been updated ")
        else:
            print("New Infected cases in Egypt:{}".format(dataFrame.loc[cnt][2]))    