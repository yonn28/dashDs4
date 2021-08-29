import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
from utils import PredictMini
from app import app
from urllib.request import urlopen
import joblib
import pathlib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


with urlopen('https://storage.googleapis.com/base_final_cloud/Modelo_relapse_subset.sav') as response:
    Modelo_relapse_subset = joblib.load(response)

with urlopen('https://storage.googleapis.com/base_final_cloud/Modelo_malnutrition_subset.sav') as response:
    Modelo_malnutrition_subset = joblib.load(response)

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

# Data processing: Calculate SHAP values and brings the image
base_variables = PredictMini.convertirDicEnBase(valores)
img, shap_values = PredictMini.plotShapValues(Modelo_relapse_subset,base_variables)
#print(PredictMini.obtenerProbabilidad(Modelo_relapse_subset,base_variables))

features = ["AVG_ZScorePesoTalla_12M","MAX_ZScorePesoTalla_12M","Veces_DesnutricionSM_12M",
            "Veces_SobrePeso_12M","MIN_ZScorePesoTalla_12M"]

# Prob. predicted for the model
prob = 0.5 + shap_values[1][0].sum()

# List of child care categories
child_care_opt = ["Attends a community place, kindergarten, child development center or school.",
"With his or her parent at home", "With parent at work", "With maid or nanny at home",
"In the care of a relative 18 years of age or older", "In the care of a relative under 18 years of age",
"At home alone","Not applicable by flow"]


# Dropdown to select the model
drop_model = dbc.FormGroup(
    [
        #html.
        dbc.Label("Model", html_for="model", className="label_selector", width=3),
        dbc.Col([
            dcc.Dropdown(
                id="model",
                options=[{'value': "0", 'label': "Malnutrition"}, {'value': "1", 'label': "Relapse"}],
                value=0,
                #className="container-fluid"
            ),
        ], width=9, align="center"),#className="lg-auto",),
    ],
    row=True,
    #inline=True,
    #className="mr-5",
)

# Dropdown child-care
drop_child_care = dbc.FormGroup(
    [
        #html.
        dbc.Label("Children care type", html_for="ch_care", className="label_selector", width=3),
        dbc.Col([
            dcc.Dropdown(
                id="ch_care",
                options=[{'value': i+1, 'label': care_opt} for i, care_opt in enumerate(child_care_opt)],
                value=1,
                #className="container-fluid"
            ),
        ], width=9, align="center"),#className="lg-auto",),
    ],
    row=True,
    #inline=True,
    #className="mr-5",
)



#{i : str(i) for i in np.linspace(-3.0,3.0,num=int((6/0.01)+1))}
#style={"font-size":"0.8125rem","font-weight":"bold"}
slider_min_z = dbc.FormGroup(
    [
        dbc.Label("Min. Z-score weight-height:", html_for="slider-min-z",
             width=4, className="label_selector" , align="center"),
        dbc.Col(
            dcc.Slider(
                id='slider-min-z',
                min=-3,
                max=3,
                step=0.01,
                marks={int(i) : str(i) for i in np.linspace(-3.0,3.0,num=int((6/1)+1))},
                value=0,
                tooltip= {"always_visible":True,"placement":"top"},
                #className="pt-0"
            ),
            width=8, align="center"
        ),
    ],
    row=True, className="mb-0 ml-0",
)

slider_max_z = dbc.FormGroup(
    [
        dbc.Label("Max. Z-score weight-height:", html_for="slider-max-z",
             width=12, className="label_selector" , align="center"),
        dbc.Col(
            dcc.Slider(
                id='slider-max-z',
                min=-3,
                max=3,
                step=0.01,
                marks={int(i) : str(i) for i in np.linspace(-3.0,3.0,num=int((6/1)+1))},
                value=0,
                tooltip= {"always_visible":True,"placement":"top"},
            ),
            width=12, align="center"
        ),
    ], className="mb-0",
    #row=True,
)

slider_avg_z = dbc.FormGroup(
    [
        dbc.Label("Avg. Z-score weight-height:", html_for="slider-avg-z",
             width=12, className="label_selector" , align="center"),
        dbc.Col(
            dcc.Slider(
                id='slider-avg-z',
                min=-3,
                max=3,
                step=0.01,
                marks={int(i) : str(i) for i in np.linspace(-3.0,3.0,num=int((6/1)+1))},
                value=0,
                tooltip= {"always_visible":True,"placement":"top"},
            ),
            width=12, align="center"
        ),
    ], className="mb-0",
    #row=True,
)


slider_under = dbc.FormGroup(
    [
        dbc.Label("Undernutrition times:", html_for="slider-under",
             width=12, className="label_selector" , align="center"),
        dbc.Col(
            dcc.Slider(
                id='slider-under',
                min=0,
                max=12,
                step=1,
                marks={int(i) : str(i) for i in range(13)},
                value=0,
                #tooltip= {"always_visible":True,"placement":"top"},
            ),
            width=12, align="center"
        ),
    ],
    #row=True,
)

slider_over = dbc.FormGroup(
    [
        dbc.Label("Overweight times:", html_for="slider-over",
             width=12, className="label_selector" , align="center"),
        dbc.Col(
            dcc.Slider(
                id='slider-over',
                min=0,
                max=12,
                step=1,
                marks={int(i) : str(i) for i in range(13)},
                value=0,
                #tooltip= {"always_visible":True,"placement":"top"},
            ),
            width=12, align="center"
        ),
    ],
    #row=True,
)


# Section where the user type the variables' values
selectors = html.Div([
                html.H5("Select all parameters that apply", className="card-title"),
                dbc.Alert(["If you select ",
                             html.Em("\"Relapse\""),
                            " model, we assume that the child already had malnutrition."], color="success"),
                drop_model,
                html.P(
                    "Answer the following questions with respect "
                    "to the past 12 months.",
                    className="card-text",
                ),
                #dbc.Row([
                    #dbc.Col([
                        #dbc.Form([           
                            drop_child_care,
                        #],),#inline=True),
                    #]),
                #]),
                
                
                slider_min_z,
                dbc.Row(
                [
                    dbc.Col(
                        slider_max_z,
                     width=6,),
                     dbc.Col(
                        slider_avg_z,
                     width=6,),
                ],
                form=True, align="start", className="mb-0 pt-0",
                ),

                dbc.Row(
                [
                    dbc.Col(
                        slider_under,
                     width=6,),
                     dbc.Col(
                        slider_over,
                     width=6,),
                ],
                form=True, align="start", className="mb-0",
                ),

                
                
                dbc.Button(
                    "Click here", color="success", className="mt-auto"
                ),

])




# Middle-section of the page - Predictor
prediction_cards = dbc.Card(
            dbc.CardBody(
                [
                html.H1('Prediction tool for individuals',className="card-title"),
                dbc.Row([
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        selectors,
                                    ]
                                ), color="primary", outline=True
                            ),
                        ], width=8),
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        
                                        html.H5("Instructions", className="card-title"),
                                        #html.P(description_short_SHAP,className="text-justify"),
                                        dbc.Alert(html.P(("Prediction of the probability that a child suffers malnutrition or relapse "
                                        "on it within the next 6 months. Please modify the parameters on the left and then press ",
                                        html.Em("\"RUN PREDICTOR\""), " to obtain the prediction."),className="text-justify"), color="success"),
                                        html.P(
                                            "This card has some text content.",
                                            className="card-text",
                                        ),
                                        dbc.Button(
                                            "Run predictor", color="warning", className="mt-auto"
                                        ),
                                    ]
                                ), color="primary", outline=True
                            ),
                        ],width=4),
                    ],)
                ])
            )


text_short_SHAP_1 = (("What you see on the left side is a waterfall plot visualizing "
"SHAP values for each model feature. Feature values in"), html.Span(" pink ", style={"color": "#f8026a"}),
("cause an increase in the "
"final prediction (Relapse probability/malnutrition probability). In contrast, feature "
"values in blue cause a decrease in the final prediction. Size of the bar shows the "
"magnitude of the feature's effect. A larger bar means that the corresponding feature "
"has larger impact. The sum of all feature shap values explains why model prediction "
"was different from the baseline."))

text_short_SHAP_2 = (f"Model predicted {prob:.3f} (Relapse in malnutrition), whereas the base_value is 0.5. Biggest "
"effect is caused by the children being classified 3 times with malnutrition in the past "
"12 months; This has increased his chances of a relapse significatively. This same effect " 
"is caused by having an average ZScorePesoTalla of X, and… (asi con c/u?). In contrast, "
"the fact that the children is studying decreases the final probability. ")

description_short_SHAP = dbc.Alert(
            [   
                html.P(text_short_SHAP_1),
                html.P(text_short_SHAP_2),
                html.A("example link", href="#", className="alert-link"),
                #html.B(red, style:"red")
            ],
            color="dark",
        )



# Bottom-section of the page - SHAP values visualization and their interpretation  
Shap_cards = dbc.Card(
                dbc.CardBody(
                [
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody(
                                        html.H3("SHAP values summary", className="card-title text-center"),
                                        #html.Img(src=img, height="275px"),
                                ),
                                dbc.CardImg(src=img, bottom=True),
                            ], color="primary", outline=True),
                        ],width=8),
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H3("Interpretation of the SHAP values", className="card-title"),
                                        html.P(description_short_SHAP,className="text-justify"),
                                    ]
                                ), color="primary", outline=True, 
                            ),
                        ],width=4),
                    ]),
                ],
            )
        )




# Layout
layout = dbc.Container(
    [#dbc.Container([
        #html.H1('Prediction tool for individuals'),
        dbc.Row([
            #html.Img(src='/assets/happychildren.jpg', height="200px"),
            ], justify="center",#align="center", 
        ),
        dbc.Row([
            prediction_cards
            ], style={"margin-top": "20px"}, justify="center",
        ),
        dbc.Row([
            #dbc.Col(html.Img(src=img, height="275px"), className="text-center"), #
            #dbc.Col(dbc.Card(description_short_SHAP, color="primary", outline=True)),
            Shap_cards,
            ], style={"margin-top": "20px"}, justify="center",#align="center",   
        ),
    ],fluid=True #className="container-fluid"
)


# Callbacks