
 
#Covid Api
import requests 
import json
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt

import plotly.plotly as py
import plotly.tools as tls


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

#Plotly Map

# credientials to access plotly map
tls.set_credentials_file(username='Trexxz', api_key='9NS3Rm5M37XgJXMP1boe')

# grab data from CDC covid data
address = '/home/pi/Documents/covidthing.csv'
states = pd.read_csv(address)
states.columns = ['state', 'cases']
states.head()

# Format Csv file states and values into one list
states['text'] = 'cases'+states['cases'].astype(str)

# Data for plotting actual map
data = [dict(type='choropleth',autocolorscale=False,
             locations = states['state'], z= states['cases'],
             locationmode='USA-states', text = states['text'] ,
             colorscale = 'Blues', colorbar= dict(title="Number of cases"))]

# Sets up the map layout
layout = dict(title="Covid cases in USA", geo = dict(scope='usa', projection=dict(type='albers usa'), showlakes = True, lakecolor = 'rgb(66,165,245)',),)
fig = dict(data=data, layout=layout)

# Pulls up map
py.plot(fig)
