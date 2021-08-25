import os
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import shap # package used to calculate Shap values
from app import app
from urllib.request import urlopen
from joblib import load
import pathlib
#from utils import SHAPVal
"""
from io import BytesIO
import pickle5 as pickle
import requests
mLink = 'https://storage.googleapis.com/ds4all-test-bd1/Modelo_malnutrition.sav'
mfile = BytesIO(requests.get(mLink).content)
modelo_malnutrition = pickle.load(mfile)
"""

#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("../assets/models").resolve()

"""
MODEL_DIR = os.environ["MODEL_DIR"]
MODEL_FILE_MALN = os.environ["MODEL_FILE_MALN"]
MODEL_PATH_MALN = os.path.join(MODEL_DIR, MODEL_FILE_MALN)
"""

#modelo_malnutrition_path = DATA_PATH+'Modelo_malnutrition.sav'
#with urlopen('https://storage.googleapis.com/ds4all-test-bd1/Modelo_malnutrition.sav') as response:

modelo_malnutrition = load('Modelo_malnutrition.sav')

base_malnutrition = pd.read_csv('https://storage.googleapis.com/ds4all-test-bd1/base_malnutrition.csv').drop(["IdBeneficiario","Unnamed: 0","Unnamed: 0.1"],axis=1)
#SHAP_Val.plotShapValuesTop(modelo_malnutrition, base_malnutrition)

#shap_img = '/assets/shap.png'

layout = dbc.Container([
    dbc.Row([
    html.Img(src='/assets/long_child.jpg', height="200px"),
    ], align="center",
    )
])