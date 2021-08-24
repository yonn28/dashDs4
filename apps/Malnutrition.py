import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import pathlib
import joblib
from app import app

"""
# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
base_final = pd.read_csv('/datasets/base_malnutrition.csv')


'''
2. Parámetros de corrida
'''

#0. Path a las base:
#pathBaseRelapse = "./datasets/base_relapse.csv"
pathBaseMalnutrition = "datasets/base_malnutrition.csv"

# 1. Path a los modelos:
#pathModeloRelapse = "./models/Modelo_relapse.sav"
pathModeloMalnutrition = "models/Modelo_malnutrition.sav"

'''
3. Cargar la base:
'''

#base_relapse = pd.read_csv(pathBaseRelapse).drop(["IdBeneficiario","Unnamed: 0"],axis=1)
base_malnutrition = pd.read_csv(pathBaseMalnutrition).drop(["IdBeneficiario","Unnamed: 0","Unnamed: 0.1"],axis=1)


'''
4. Cargar los modelos:
'''

#modelo_relapse = joblib.load(pathModeloRelapse)
modelo_malnutrition = joblib.load(pathModeloMalnutrition)

shap_values_fig = SHAPValues.plotShapValuesTop(modelo_malnutrition, base_malnutrition)
"""

layout = dbc.Container([
    dbc.Row([
    html.Img(src='/assets/long_child.jpg', height="200px"),
    ], align="center",
    ),
    """
    dbc.Row([
        dcc.Graph(
                    id = 'SHAPValues_plot', 
                    figure = shap_values_fig,
                )
    ]),
    """
    dbc.Row([

    ]),
])
