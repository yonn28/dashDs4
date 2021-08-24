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


# get relative data folder
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("../datasets").resolve()
#base_malnutrition = pd.read_csv('https://storage.googleapis.com/ds4all-test-bd1/base_malnutrition.csv').drop(["IdBeneficiario","Unnamed: 0","Unnamed: 0.1"],axis=1)
#modelo_malnutrition = joblib.load('https://storage.googleapis.com/ds4all-test-bd1/Modelo_malnutrition.sav')

#shap_values_fig = SHAPValues.plotShapValuesTop(modelo_malnutrition, base_malnutrition)

layout = dbc.Container([
    dbc.Row([
    html.Img(src='/assets/long_child.jpg', height="200px"),
    ], align="center",
    ),
    dbc.Row([
    ]),
])


"""
    dbc.Row([
        dcc.Graph(
                    id = 'SHAPValues_plot',
                    figure = shap_values_fig,
                )
    ]),
    """