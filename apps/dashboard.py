import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pathlib
from app import app
import dash_bootstrap_components as dbc
#colombian map dependencies
from utils import mapcolombia
import pandas as pd


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
#base_final = pd.read_csv('https://storage.googleapis.com/ds4all-test-bd1/base_final.csv')

# Authenticated access to GC Storage
import pandas as pd
from io import BytesIO, StringIO
from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="assets/ds4a-project-322919-838eb9846309.json"
storage_client = storage.Client()
buckets = list(storage_client.list_buckets())
bucket = storage_client.get_bucket("base_final_cloud") # get bucket data as blob
blob = bucket.get_blob('base_final.csv') # convert to string

byte_stream = BytesIO()
blob.download_to_file(byte_stream)
byte_stream.seek(0)
fileobj = byte_stream
base_final = pd.read_csv(fileobj) # read csv 


figmap , dpts_count , colombia  = mapcolombia.getfigmap(base_final)


controlsMap = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label('year'),
                dcc.Dropdown(
                    id='year',
                    options = [{'value': i, 'label': i } for i in dpts_count['anno_encuesta_x'].unique()]
                ), 
            ]
        )
    ],
    body = True,
)


layout = html.Div([
        html.Div([
            html.H4("Colombian map by years"),
            html.Div(controlsMap),
            html.Div(
                dcc.Graph(
                    id = 'colombia_plot', 
                    figure = figmap
                )
            )
        ])
             
])

@app.callback(
    Output('colombia_plot','figure'),
    Input('year','value'),
)
def graph_map_per_year(year = 2018):
    dpts_count_filtered = dpts_count[dpts_count['anno_encuesta_x'] == year]
    figmap = px.choropleth_mapbox(dpts_count_filtered , geojson=colombia, locations='nom_dpto', 
                            featureidkey="properties.DPTO_CNMBR",
                            color='count_ratio',
                            color_continuous_scale='plasma',
                            mapbox_style="carto-positron",
                            zoom=3, center = {"lat": 4.570868, "lon": -74.297333},
                            opacity=0.5,
                            labels={'unemp':'unemployment rate'}
                            )
    figmap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return figmap