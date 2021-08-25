import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import pathlib
import joblib
#from utils import SHAPValues
from app import app


layout = dbc.Container([
    dbc.Row([
    html.Img(src='/assets/happychildren.jpg', height="200px"),
    ], align="center",
    ),
    dbc.Row([
    ]),
])