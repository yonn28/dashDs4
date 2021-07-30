import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pathlib
from app import app
import dash_bootstrap_components as dbc
#colombian map dependencies
import pandas as pd
import geopandas as gpd
from urllib.request import urlopen
import json 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
base_final = pd.read_csv(DATA_PATH.joinpath('base_final.csv'))


geoData = gpd.read_file('https://raw.githubusercontent.com/namonroyr/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson')

with urlopen('https://raw.githubusercontent.com/namonroyr/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson') as response:
    colombia = json.load(response)

dpts_count_target1=base_final.query("Target==1").groupby(['cod_dpto', 'nom_dpto','anno_encuesta']).size().to_frame('Count_Dpto_Target').reset_index()
dpts_count_total=base_final.groupby(['cod_dpto', 'nom_dpto','anno_encuesta']).size().to_frame('Count_Dpto_Total').reset_index()
dpts_count = pd.merge(dpts_count_target1, dpts_count_total, on=["cod_dpto", "nom_dpto"])
dpts_count["count_ratio"] = dpts_count["Count_Dpto_Target"]/dpts_count["Count_Dpto_Total"]*100
dpts_count['cod_dpto']=pd.to_numeric(dpts_count['cod_dpto'])
dpts_count['cod_dpto']=dpts_count['cod_dpto'].astype(int)
dpts_count['cod_dpto']=dpts_count['cod_dpto'].apply(lambda x: '{0:0>2}'.format(x))

figmap = px.choropleth_mapbox(dpts_count, geojson=colombia, locations='nom_dpto', 
                           featureidkey="properties.DPTO_CNMBR",
                           color='count_ratio',
                           color_continuous_scale="Viridis",
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 4.570868, "lon": -74.297333},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
figmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


controlsMap = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label('año'),
                dcc.Dropdown(
                    id='year',
                    options = [{'value': i, 'label': i } for i in dpts_count['anno_encuesta_x'].unique()]
                ), 
            ]
        )
    ],
    body = True,
)


layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(controlsMap, md=4),
            dbc.Col(
                dcc.Graph(
                    id = 'colombia_plot', 
                    figure = figmap
                )
            )
        ],
        align = 'center',
    )
])

@app.callback(
    Output('colombia_plot','figure'),
    Input('year','value'),
)
def graph_map_per_year(year):
    dpts_count_filtered = dpts_count[dpts_count['anno_encuesta_x'] == year]
    figmap = px.choropleth_mapbox(dpts_count_filtered , geojson=colombia, locations='nom_dpto', 
                            featureidkey="properties.DPTO_CNMBR",
                            color='count_ratio',
                            color_continuous_scale="Viridis",
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 4.570868, "lon": -74.297333},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    figmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return figmap