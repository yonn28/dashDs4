import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import shap # package used to calculate Shap values
from app import app
from urllib.request import urlopen
import joblib # Cargar y guardar modelos sklearn

modelo_malnutrition_path = '/assets/models/Modelo_malnutrition.sav'
#with urlopen('https://storage.googleapis.com/ds4all-test-bd1/Modelo_malnutrition.sav') as response:
#modelo_malnutrition = joblib.load(modelo_malnutrition_path)

base_malnutrition = pd.read_csv('https://storage.googleapis.com/ds4all-test-bd1/base_malnutrition.csv').drop(["IdBeneficiario","Unnamed: 0","Unnamed: 0.1"],axis=1)

shap_fig =

layout = dbc.Container([
    dbc.Row([
    html.Img(src='/assets/long_child.jpg', height="200px"),
    ], align="center",
    ),
    dbc.Row([

    ]),
])