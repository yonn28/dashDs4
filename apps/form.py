import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import shap # package used to calculate Shap values
from app import app

layout = dbc.Container([
    dbc.Row([
    html.Img(src='/assets/long_child.jpg', height="200px"),
    ], align="center",
    ),
    dbc.Row([

    ]),
])