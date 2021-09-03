import pandas as pd
import plotly.express as px
import geopandas as gpd
from urllib.request import urlopen
import json 
import ssl
import requests
ssl._create_default_https_context = ssl._create_unverified_context

def getfigmap(df, var, color, colombia):
    figmap = px.choropleth_mapbox(df, geojson=colombia, locations='nom_dpto', 
                            featureidkey="properties.DPTO_CNMBR",
                            color=var,
                            color_continuous_scale=color,
                            mapbox_style="carto-positron",
                            zoom=4, center = {"lat": 4.570868, "lon": -74.297333},
                            opacity=0.5,
                            labels={'Relapse_Percentage': '%', 'Malnutrition_Percentage':'%'}
                            )
    figmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return figmap