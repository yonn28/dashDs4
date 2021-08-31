import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import app






banner_jumbotron = dbc.Jumbotron(
    [
        html.H1("Jumbotron", className="display-3"),
        html.P(
            "Use a jumbotron to call attention to "
            "featured content or information.",
            className="lead",
        ),
        html.Hr(className="my-2"),
        html.P(
            "Jumbotrons use utility classes for typography and "
            "spacing to suit the larger container."
        ),
        html.P(dbc.Button("Learn more", color="primary"), className="lead"),
    ], className="jumbotron"
)



# Layout
layout = dbc.Container(
    [

        



        dbc.Row([
            #html.Img(src='/assets/happychildren.jpg', height="200px"),
            banner_jumbotron,
            ], #justify="center",#align="center", 
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