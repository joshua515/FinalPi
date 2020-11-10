#Covid Api
import requests 
import json

stateparam = input("What State do you want to look at? 'Use state acronym ")



parameters = {
    "state": "{}".format(stateparam),


}

Response = requests.get("https://data.cdc.gov/resource/9mfq-cb36.json?submission_date=2020-10-29T00:00:00.000&$select=state,tot_cases", params = parameters)
print (Response.status_code)



def jprint(obj):
    #mkaes formatted string of json data object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(Response.json())
