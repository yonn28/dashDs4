import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pathlib
from app import app
import dash_bootstrap_components as dbc
# colombian map dependencies
from utils import mapcolombia
from utils import plot_by_year
import pandas as pd
from urllib.request import urlopen
import requests
import math
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context

with urlopen('https://raw.githubusercontent.com/namonroyr/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson') as response:
    colombia = json.load(response)

mapa = requests.get("https://mapsmicroservice-zbca65qbuq-nn.a.run.app/api/v1/maps")
dpts_count = pd.DataFrame.from_dict(mapa.json())


fig_years_dist = plot_by_year.ploting_distribution()

years = dpts_count['Año'].unique()
slider_items = {int(math.floor(years[i])):str(math.floor(years[i])) for i in range(len(years))}

"""
controlslider = html.Div([
    dcc.RangeSlider(
        id='slider-year',
        min=2017,
        max=2020,
        step=None,            # True, False - insert dots, only when step>1
        allowCross=False,
        marks=slider_items,
        value=2017,
    )  
])
"""

card_map = dbc.Card(
    dbc.CardBody([    
        html.H4("Malnutrition Relapse % by Department"),
        html.Hr(id="hr_1"),
        # html.Div(control_dropdown),
        html.Div(
            dcc.Graph(
                id='colombia_plot',
                figure={}
            )
        )     
    ])
,color="primary", outline=True)

card_map2 = dbc.Card(
    dbc.CardBody([    
        html.H4("Malnutrition % by Department"),
        html.Hr(id="hr_1"),
        html.Div(
            dcc.Graph(
                id='colombia_plot_2',
                figure={}
            )
        )     
    ])
,color="primary", outline=True)

card_graph_distribution = dbc.Card(
    dbc.CardBody([
        dbc.Card([
            dbc.CardBody([
                html.H4("Malnutrition Relapse by Year", className="card-title"),
                html.Hr(id="hr_1"),
                dcc.Graph(
                    id='years_dist_plot',
                    figure=fig_years_dist
                )
            ])
        ],color="primary", outline=True)
    ])
,color="light", outline=True)

colombian_maps = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            dbc.Col(
                dcc.Slider(
                    id='slider-year',
                    min=2017,
                    max=2020,
                    step=None,
                    marks=slider_items,
                    value=2017,
                ), width=12
            )
        ]),
        dbc.Row([
            dbc.Col(
                card_map2, width = 6
            ),
            dbc.Col(
                card_map, width = 6
            )
        ])
    ])
],color="light", outline=True)


layout = dbc.Container([
    dbc.Row(dbc.Col(colombian_maps, width=12)),
    dbc.Row([
        dbc.Col(
            card_graph_distribution, width=12
        )
      ])
], fluid=True)


@app.callback([Output('colombia_plot', 'figure'),
              Output('colombia_plot_2', 'figure'),],
              [Input('slider-year', 'value')])
def display_maps(value):
    dpts_count_filtered = dpts_count[dpts_count['Año']==value]
    figmap_rel = mapcolombia.getfigmap(dpts_count_filtered, 'Relapse_Percentage', 'peach', colombia)
    figmap_mal = mapcolombia.getfigmap(dpts_count_filtered, 'Malnutrition_Percentage', 'emrld', colombia)
    return figmap_rel, figmap_mal