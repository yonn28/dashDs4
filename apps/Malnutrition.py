import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from utils import SHAP_Val
from utils import top10table
from app import app
from urllib.request import urlopen
import joblib
import pathlib
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


with urlopen('https://storage.googleapis.com/ds4all-test-bd1/Modelo_malnutrition.sav') as response:
    modelo_malnutrition = joblib.load(response)

base_malnutrition = pd.read_csv('https://storage.googleapis.com/ds4all-test-bd1/base_malnutrition.csv').drop(["IdBeneficiario","Unnamed: 0","Unnamed: 0.1"],axis=1)

top10_df = top10table.createTable_top(modelo_malnutrition, base_malnutrition)
df_f = top10_df[['MIN_ZScorePesoTalla_12M', 'AVG_ZScorePesoTalla_12M', 'MAX_ZScorePesoTalla_12M', 'Veces_DesnutricionSM_12M',
           'Veces_SobrePeso_12M', 'Veces_Normal_12M','TienePasado', 'Veces_Normal_12M', 'sexo_persona_1.0', 'sexo_persona_-999',
           'tip_cuidado_niños_2.0', 'tip_cuidado_niños_3.0', 'tip_cuidado_niños_4.0', 'tip_cuidado_niños_5.0',
           'tip_cuidado_niños_6.0', 'tip_cuidado_niños_7.0', 'tip_cuidado_niños_8.0', 'tip_cuidado_niños_9.0',
           'tip_cuidado_niños_-999','ingresos_promp_imp', 'gasto_ppers_imp', 'gasto_alim_ppers_imp', 'uni_dias_agua','cod_clase_2.0',
           'cod_clase_3.0', 'cod_clase_-999', 'noprivaciones', 'ind_estudia_1.0', 'ind_estudia_-999']]

img = SHAP_Val.plotShapValuesTop(modelo_malnutrition, top10_df)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Img(src='/assets/long_child.jpg', height="200px"), width=12)
    ], align="center",
    ),
    dbc.Row([
        dbc.Col(html.Img(src=img, height="550px"), style={"margin-top": "20px"})
    ], align="center",
    )
], fluid=True)