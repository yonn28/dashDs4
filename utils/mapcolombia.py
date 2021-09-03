import pandas as pd
import plotly.express as px
import geopandas as gpd
from urllib.request import urlopen
import json 
import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context


def getfigmap():

    with urlopen('https://raw.githubusercontent.com/namonroyr/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson') as response:
        colombia = json.load(response)

    mapa = requests.get("https://mapsmicroservice-zbca65qbuq-nn.a.run.app/api/v1/maps")
    dpts_count = pd.DataFrame.from_dict(mapa.json())

    figmap = px.choropleth_mapbox(dpts_count , geojson=colombia, locations='nom_dpto', 
                            featureidkey="properties.DPTO_CNMBR",
                            color='Relapse_Percentage',
                            color_continuous_scale='plasma',
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 4.570868, "lon": -74.297333},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    figmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return  figmap, dpts_count ,colombia 