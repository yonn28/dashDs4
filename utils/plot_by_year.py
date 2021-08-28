import pandas as pd
import plotly.express as px
from itertools import cycle
import requests


def ploting_distribution():
    ry = requests.get('https://microservice1-zbca65qbuq-nn.a.run.app/api/v1/y')
    y = ry.json()
    rx = requests.get('https://microservice1-zbca65qbuq-nn.a.run.app/api/v1/x')
    porcentajes_mes_dict = requests.get('https://microservice1-zbca65qbuq-nn.a.run.app/api/v1/df')
    porcentajes_mes=pd.DataFrame.from_dict(porcentajes_mes_dict.json())
    x = rx.json()
    y1 = y[:12]
    y2 = y[12:24]
    y3 = y[24:]
    fig = px.line(porcentajes_mes, x=x, y=[y1,y2,y3], color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
    names = cycle(['Malnutrition 2017', 'Malnutrition 2018', 'Malnutrition 2019']) 
    fig.for_each_trace(lambda x : x.update(name = next(names)))
    fig.update_layout(xaxis_title="Month", yaxis_title="Percentage")
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    fig.update_layout(legend=dict(x=0.1,y=1))
    return fig