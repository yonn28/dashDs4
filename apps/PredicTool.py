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

valores = {"AVG_ZScorePesoTalla_12M":-2.5,
           "MAX_ZScorePesoTalla_12M":-1.0,
           "Veces_DesnutricionSM_12M":3.0,
           "Veces_SobrePeso_12M":0.0,
           "MIN_ZScorePesoTalla_12M":-3.0, #
           "tip_cuidado_niños":1, #Mas adelante
           "ind_discap":"ninguna", #ninguna o si
           "ind_leer_escribir":1.0, #Posibles valores 1:si 2:no
           "ind_estudia":0.0, #Posibles valores 1: si 2:no
           "ind_recibe_comida":0.0} #osibles valores 1:si 2:no

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
print(PredictMini.obtenerProbabilidad(Modelo_relapse_subset,base_variables))


layout = dbc.Container([
    dbc.Row([
    html.Img(src='/assets/happychildren.jpg', height="200px"),
    ], align="center",
    ),
    dbc.Row([
        dbc.Col(html.Img(src=img, height="550px"), style={"margin-top": "20px"})
    ], align="center",
    )
], fluid=True)