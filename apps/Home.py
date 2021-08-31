import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import app







# Layout
layout = dbc.Container(
    [
        dbc.Row([
            html.Img(src='/assets/happychildren.jpg', height="200px"),
            ], justify="center",#align="center", 
        ),
        dbc.Row([
            
            dbc.Col(["Hola"

            ], className="md-4"),

            dbc.Col(["Hola"

            ], className="md-4"),

            dbc.Col(["Hola"

            ], className="md-4"),


            ], justify="center", #align="center",
        ),
        
    ], fluid=True #className="container-fluid"
)