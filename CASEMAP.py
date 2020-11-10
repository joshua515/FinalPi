import numpy as np
import pandas as pd

import chart_studio.plotly as py
import chart_studio.tools as tls


# credientials to access plotly map
tls.set_credentials_file(username='Trexxz', api_key='9NS3Rm5M37XgJXMP1boe')

# grab data from CDC covid data
address = 'C:\\Users\\dejat\\OneDrive\\Documents\\covidthing.csv'
states = pd.read_csv(address)
states.columns = ['state', 'cases']
states.head()

states['text'] = 'cases'+states['cases'].astype(str)

data = [dict(type='choropleth',autocolorscale=False, locations = states['state'], z= states['cases'], locationmode='USA-states', text = states['text'] , colorscale = 'emrld', colorbar= dict(title="Number of cases"))]

layout = dict(title="Covid cases in USA", geo = dict(scope='usa', projection=dict(type='albers usa'), showlakes = True, lakecolor = 'rgb(66,165,245)',),)

fig = dict(data=data, layout=layout)

py.plot(fig)


