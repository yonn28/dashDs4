import pandas as pd
import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import geopandas as gpd
from urllib.request import urlopen
import json 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

base_final = pd.read_csv("base_final.csv")
base_final = base_final.drop(columns = ['Unnamed: 0', 'Sexo'])


app = dash.Dash( __name__ , external_stylesheets=[dbc.themes.BOOTSTRAP])


geoData = gpd.read_file('https://raw.githubusercontent.com/namonroyr/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson')

with urlopen('https://raw.githubusercontent.com/namonroyr/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson') as response:
    colombia = json.load(response)

dpts_count_target1=base_final.query("Target==1").groupby(['cod_dpto', 'nom_dpto']).size().to_frame('Count_Dpto_Target').reset_index()
dpts_count_total=base_final.groupby(['cod_dpto', 'nom_dpto']).size().to_frame('Count_Dpto_Total').reset_index()
dpts_count = pd.merge(dpts_count_target1, dpts_count_total, on=["cod_dpto", "nom_dpto"])
dpts_count["count_ratio"] = dpts_count["Count_Dpto_Target"]/dpts_count["Count_Dpto_Total"]*100
dpts_count['cod_dpto']=pd.to_numeric(dpts_count['cod_dpto'])
dpts_count['cod_dpto']=dpts_count['cod_dpto'].astype(int)
dpts_count['cod_dpto']=dpts_count['cod_dpto'].apply(lambda x: '{0:0>2}'.format(x))

figMap = px.choropleth_mapbox(dpts_count, geojson=colombia, locations='nom_dpto', 
                           featureidkey="properties.DPTO_CNMBR",
                           color='count_ratio',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 4.570868, "lon": -74.297333},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
figMap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


app.layout = dbc.Container([
    dcc.Graph(
        id = 'colombia_plot', 
        figure = figMap
    )
])



if __name__ == '__main__':
    app.run_server(port='8050', debug=True)