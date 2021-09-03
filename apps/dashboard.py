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
import math

figmap, dpts_count, colombia = mapcolombia.getfigmap()
fig_years_dist = plot_by_year.ploting_distribution()

figmap2 = figmap #this is temporary until get real information

years = dpts_count['Año'].unique()
slider_items = {int(i) : str(math.floor(years[i])) for i in range(len(years))}

controlslider = html.Div([
    dbc.Alert("Show national distributions for reincidence filter by sociodemografic data", color="primary"),
    dcc.Slider(
        id ='slider-year',
        min = 0,
        max = len(years)-1,
        step = None,
        marks = slider_items,
        value = 0
    )  
])


control_dropdown = html.Div(
    [   
        dbc.Label('year'),
        dcc.Dropdown(
            id='year_dropdown',
            options = [{'value': i, 'label': i} for i in dpts_count['Año'].unique()],
            value = dpts_count['Año'].unique()[0]
        )
    ]
)

card_map = dbc.Card(
    dbc.CardBody([    
        html.H4("Colombian map by years"),
        # html.Div(control_dropdown),
        html.Div(
            dcc.Graph(
                id='colombia_plot',
                figure=figmap
            )
        )     
    ])
)

card_map2 = dbc.Card(
    dbc.CardBody([    
        html.H4("distribution by socio demografic data"),
        html.Div(control_dropdown),
        html.Div(
            dcc.Graph(
                id='colombia_plot_2',
                figure=figmap2
            )
        )     
    ])
)

card_graph_distribution = dbc.Card([
    dbc.CardBody([
        html.H4("Reincidence by year", className="card-title"),
        dcc.Graph(
            id='years_dist_plot',
            figure=fig_years_dist
        )
    ])
])

colombian_maps = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            dbc.Col(
                controlslider, width = 12
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
])


layout = html.Div([
    colombian_maps,
    dbc.Row([
        dbc.Col(
            card_graph_distribution, width = 12
        )
      ],className='dashboard__margin__top'
    )
], className = 'dashboard__margin__top')



@app.callback(Output('colombia_plot', 'figure'),
              Input('slider-year', 'value'))
def display_map(value):
    year = math.floor(years[value])
    dpts_count_filtered = dpts_count[dpts_count['Año'] == year]
    figmap = px.choropleth_mapbox(dpts_count_filtered, geojson=colombia, locations='nom_dpto',
                            featureidkey="properties.DPTO_CNMBR",
                            color='count_ratio',
                            color_continuous_scale='ylorrd',
                            mapbox_style="carto-positron",
                            zoom=3, center={"lat": 4.570868, "lon": -74.297333},
                            opacity=0.5,
                            labels={'unemp': 'unemployment rate'}
                            )
    figmap.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return figmap


@app.callback(Output('colombia_plot_2', 'figure'),
              Input('year_dropdown', 'value'))
def display_map_2(value):
    dpts_count_filtered = dpts_count[dpts_count['Año'] == value]
    figmap2 = px.choropleth_mapbox(dpts_count_filtered, geojson=colombia, locations='nom_dpto',
                            featureidkey="properties.DPTO_CNMBR",
                            color='count_ratio',
                            color_continuous_scale='ylorrd',
                            mapbox_style="carto-positron",
                            zoom=3, center={"lat": 4.570868, "lon": -74.297333},
                            opacity=0.5,
                            labels={'unemp': 'unemployment rate'}
                            )
    figmap2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return figmap2