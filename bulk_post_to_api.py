import pandas as pd
import requests

# URL of your endpoint
URL = "https://eoxvprzug2.execute-api.eu-central-1.amazonaws.com/prod/connect"

#read the testfile
data = pd.read_csv('test_sample.csv', sep = ',')

# write all the rows from the testfile to the api as put request
for i in data.index:
    try:
        # convert the row to json
        export = data.loc[i].to_json()

        #send it to the api
        response = requests.post(URL, data = export)

        # print the returncode
        print(export)
        print(response)
    except:
        print(data.loc[i])