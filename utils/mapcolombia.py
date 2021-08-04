import pandas as pd
import plotly.express as px
import geopandas as gpd
from urllib.request import urlopen
import json 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def getfigmap(base_final):

    with urlopen('https://raw.githubusercontent.com/namonroyr/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson') as response:
        colombia = json.load(response)

    dpts_count_target1=base_final.query("Target==1").groupby(['cod_dpto', 'nom_dpto','anno_encuesta']).size().to_frame('Count_Dpto_Target').reset_index()
    dpts_count_total=base_final.groupby(['cod_dpto', 'nom_dpto','anno_encuesta']).size().to_frame('Count_Dpto_Total').reset_index()
    dpts_count = pd.merge(dpts_count_target1, dpts_count_total, on=["cod_dpto", "nom_dpto"])
    dpts_count["count_ratio"] = dpts_count["Count_Dpto_Target"]/dpts_count["Count_Dpto_Total"]*100
    dpts_count['cod_dpto']=pd.to_numeric(dpts_count['cod_dpto'])
    dpts_count['cod_dpto']=dpts_count['cod_dpto'].astype(int)
    dpts_count['cod_dpto']=dpts_count['cod_dpto'].apply(lambda x: '{0:0>2}'.format(x))

    figmap = px.choropleth_mapbox(dpts_count , geojson=colombia, locations='nom_dpto', 
                            featureidkey="properties.DPTO_CNMBR",
                            color='count_ratio',
                            color_continuous_scale="Viridis",
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 4.570868, "lon": -74.297333},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    figmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return  figmap, dpts_count ,colombia 