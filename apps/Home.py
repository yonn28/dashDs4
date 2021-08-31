import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import app






banner_jumbotron = dbc.Jumbotron(
    [
        dbc.Container([
            html.H1("KidNutrilytics\n", className="display-3 product_title"),
            #html.Br(),
            html.Hr(className="my-4"),
            html.P(
                "The ultimate platform to predict malnutrition "
                "in children under five",
                className="lead text_jumbotron",
            ),
            html.P(dbc.Button("Learn more", color="primary",
                external_link=True, href="#col-home-2", active=True), className="lead"),
        ], fluid=True, className="text-center text-light"),
    ], className="jumbotron vertical-center", fluid=True
)

print("Running...")

# Layout
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
            #html.Img(src='/assets/happychildren.jpg', height="200px"),
                banner_jumbotron,

            ],width=12, className="sm-12"),
        ], #justify="center",#align="center",)
        ),
        dbc.Row([
            
            dbc.Col(["Hola"

            ], className="md-4"),

            dbc.Col(["Hola"

            ],id="col-home-2", className="md-4"),

            dbc.Col(["Hola"

            ], className="md-4"),


            ], justify="center", #align="center",
        ),
        
    ], fluid=True #className="container-fluid"
)