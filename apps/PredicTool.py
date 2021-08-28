import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
#import shap # package used to calculate Shap values
from utils import PredictMini
from app import app
from urllib.request import urlopen
import joblib
import pathlib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


with urlopen('https://storage.googleapis.com/base_final_cloud/Modelo_relapse_subset.sav') as response:
    Modelo_relapse_subset = joblib.load(response)

#SHAP_Val.plotShapValuesTop(modelo_malnutrition, base_malnutrition)

valores = {"AVG_ZScorePesoTalla_12M":-2.5, #[-3,3] --> Slider float
           "MAX_ZScorePesoTalla_12M":-1.0, #[-3,3] --> Slider float
           "Veces_DesnutricionSM_12M":3.0, # 0 en adelante --> Slider enteros positivos
           "Veces_SobrePeso_12M":0.0, # 0 en adelante --> Slider enteros positivos
           "MIN_ZScorePesoTalla_12M":-3.0, # [-3,3] --> Slider float
           "tip_cuidado_niños":1, #Mas adelante --> Dropdown
           "ind_discap":"ninguna", #ninguna o si --> Switch
           "ind_leer_escribir":1.0, #Posibles valores 1:si 2:no  --> Switch
           "ind_estudia":0.0, #Posibles valores 1: si 2:no --> Switch
           "ind_recibe_comida":0.0} #osibles valores 1:si 2:no --> Switch

'''

#Posibles valores de tip_cuidado_niños
1- Asiste a un lugar comunitario, jardín o centro de desarrollo infantil o colegio 
2- Con su padre o madre en la casa
3- Con su padre o madre en el trabajo
4- Con empleada o niñera en la casa
5- Al cuidado de un pariente de 18 años o más
6- Al cuidado de un pariente menor de 18 años
7- En casa solo
9-No aplica por flujo
'''

base_variables = PredictMini.convertirDicEnBase(valores)
img = PredictMini.plotShapValues(Modelo_relapse_subset,base_variables)
#print(PredictMini.obtenerProbabilidad(Modelo_relapse_subset,base_variables))




cards = dbc.Card(
            dbc.CardBody(
                [
                dbc.CardDeck(
                [
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Card 1", className="card-title"),
                                html.P(
                                    "This card has some text content, which is a little "
                                    "bit longer than the second card.",
                                    className="card-text",
                                ),
                                dbc.Button(
                                    "Click here", color="success", className="mt-auto"
                                ),
                            ]
                        ), color="primary", outline=True
                    ),
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H5("Card 2", className="card-title"),
                                html.P(
                                    "This card has some text content.",
                                    className="card-text",
                                ),
                                dbc.Button(
                                    "Click here", color="warning", className="mt-auto"
                                ),
                            ]
                        ), color="primary", outline=True
                    ),
                ]
            )
        ],
    )
)

description_short_SHAP = dbc.Alert(
            [
                "This is a primary alert with an ",
                html.A("example link", href="#", className="alert-link"),
            ],
            color="primary",
        )


layout = dbc.Container(
    [#dbc.Container([
        html.H1('Prediction tool for individuals'),
        dbc.Row([
            html.Img(src='/assets/happychildren.jpg', height="200px"),
            ], justify="center",#align="center", 
        ),
        dbc.Row([
            cards
            ], style={"margin-top": "20px"}, justify="center",
        ),
        dbc.Row([
            dbc.Col(html.Img(src=img, height="275px"), className="text-center"), #
            dbc.Col(dbc.Card(description_short_SHAP, color="primary", outline=True)),
            ], style={"margin-top": "20px"}, justify="center",#align="center",
            
        )
    ],fluid=True #className="container-fluid"
)