import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
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
                options=[{'value': 0, 'label': "Malnutrition"}, {'value': 1, 'label': "Relapse"}],
                value=0,
                #className="container-fluid"
            ),
        ], width=9, align="center"),#className="lg-auto",),
    ],
    row=True,
    #inline=True,
    className="ml-0 mr-0",
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
    className="ml-0 mr-0",
)


#style={"font-size":"0.8125rem","font-weight":"bold"}
step = 1
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
                marks={int(i) : str(i) for i in np.linspace(-3.0,3.0,num=int((6/step)+1))},
                value=0,
                tooltip= {"always_visible":True,"placement":"top"},
                #className="pt-0"
            ),
            width=8, align="center"
        ),
    ],
    row=True, className="mb-0 ml-0 mr-0",
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


switches = dbc.Row([
            dbc.Col([
                dbc.FormGroup([
                    dbc.Label("Toggle a bunch", html_for="switches",
                        hidden=True, width=12, align="center"),
                    dbc.Checklist(
                        options=[
                            {"label": "Disability", "value": 1},
                            {"label": "Literate", "value": 2},
                            {"label": "Study", "value": 3},
                            {"label": "Receives food", "value": 4},
                        ],
                        value=[1],
                        id="switches",
                        switch=True,
                        #inline=True,
                        #labelClassName="label_selector",
                        labelCheckedClassName="label_selector",
                        #style={"display": "flex", "justify-content": "space-evenly"},
                        className="just_even_2",
                    ),
                ],),  #row=True
            ], width=12, )#style={"display": "flex", "justify-content": "space-evenly"},),
        ], form=True, align="start", className="mb-0 pt-0",)


# Section where the user type the variables' values
selectors = html.Div([
                html.H5("Select all parameters that apply", className="card-title"),
                dbc.Alert(["If you select ",
                             html.Em("\"Relapse\""),
                            " model, we assume that the child already had malnutrition."], color="success"),
                drop_model,
                html.P(
                    "Answer the following 10 questions with respect "
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

                
                
                #dbc.Button("Click here", color="success", className="mt-auto"),

])




exp_prob = dcc.Markdown('''
---
>
> How to read the probability?.
> 
''')  


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
                                        #dbc.Row(
                                            #[
                                                #dbc.Col([
                                                    switches,
                                                #], width=12),
                                            #]),#, justify="center"),

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
                                        #html.P(
                                            #"This card has some text content.",
                                            #className="card-text",
                                        #),
                                        dbc.Row([
                                            dbc.Col([
                                                dbc.Button(
                                                    id="button_pred", children="Run predictor", n_clicks=0,
                                                    color="warning", className="mt-auto"
                                                ),
                                            ], className="just_center"), #style={"display": "flex","justify-content": "center"}),
                                        ],),


                                        exp_prob,
                                        html.Div([
                                            html.Ul([
                                                html.Li([html.Span("Low risk: ", style={"color": "#1fbd38"}),
                                                "The child is currently at low risk of suffering this disease."]),
                                                html.Li([html.Span("Slight risk: ", style={"color": "#fff000"}),
                                                "The child has slight risk of suffering this disease."]),
                                                html.Li([html.Span("Latent risk: ", style={"color": "#f86e02"}),
                                                "The child has latent risk of suffering this disease."]),
                                                html.Li([html.Span("High risk: ", style={"color": "#f30404"}),
                                                "The child should be prioritized."]),
                                            ]),
                                        ]),
                                        dbc.Progress(id="prog-bar", value="", color="",
                                            striped=True, animated=True, 
                                            className="mb-3 mt-4" , style={"height": "30px"}),
                                    ]
                                ), color="primary", outline=True
                            ),
                        ],width=4),
                    ],)
                ])
            )


text_short_SHAP_1 = ("What you see on the left side is a waterfall plot to visualize "
"SHAP values for each model feature. Feature values in", html.Span(" pink ", className="pink_bold"),
"cause an increase in the "
"final prediction (malnutrition/relapse probability). In contrast, feature "
"values in" , html.Span(" blue ", className="blue_bold"), "cause a decrease in the final prediction. Size of the bar shows the "
"magnitude of the feature's effect. A larger bar means that the corresponding feature "
"has larger impact. The sum of all feature SHAP values explains why model prediction "
"was different from the baseline.")


#f"Model predicted {prob:.3f}
text_short_SHAP_2 = ("Model predicted a probability of ",
html.Span(children=[],id="prob-span", className="pink_bold"),
" of suffering ", html.Span(children=[],id="model-span", className="pink_bold"),
", whereas the base_value is 0.5. ", html.P(id="msg-least",children=[]), html.P(id="msg-great",children=[]))

description_short_SHAP = dbc.Alert(
            [   
                html.P(text_short_SHAP_1),
                html.P(text_short_SHAP_2),
                #html.A("example link", href="#", className="alert-link"),
                #html.B(red, style:"red")
            ],
            color="dark", className="text-justify p-4",
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
                                dbc.CardImg(id="shap_img", bottom=True), #, src=""
                                #html.Img(id="shap_img",src=""),
                            ], color="primary", outline=True),
                        ],width=8),
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H3("Interpretation of the SHAP values", className="card-title"),
                                        #html.P(description_short_SHAP,className="text-justify"),
                                        description_short_SHAP,
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
            ], className="mt-4", justify="center", #style={"margin-top": "20px"}
        ),
        dbc.Row([
            Shap_cards,
            ], className="mt-4", justify="center",#align="center",   style={"margin-top": "20px"}
        ),
    ],fluid=True #className="container-fluid"
)


# Callbacks


@app.callback(
    [Output(component_id = "shap_img", component_property = "src"),
    Output(component_id = "prob-span", component_property = "children"),
    Output(component_id = "model-span", component_property = "children"),
    Output(component_id = "prog-bar", component_property = "children"),
    Output(component_id = "prog-bar", component_property = "value"),
    Output(component_id = "prog-bar", component_property = "color"),
    Output(component_id = "msg-least", component_property = "children"),
    Output(component_id = "msg-great", component_property = "children"),
    ],
    [Input(component_id = "button_pred", component_property = "n_clicks"),
    ],
    [State(component_id = "model", component_property = "value"),
    State(component_id = "ch_care", component_property = "value"),
    State(component_id = "slider-min-z", component_property = "value"),
    State(component_id = "slider-max-z", component_property = "value"),
    State(component_id = "slider-avg-z", component_property = "value"),
    State(component_id = "slider-under", component_property = "value"),
    State(component_id = "slider-over", component_property = "value"),
    State(component_id = "switches", component_property = "value"),
    ]
)
def on_button_click(n, model_val, care, min_z, max_z, avg_z, under, over, switch_list):
    """
    print(f"button-n_clicks are: {n}, and type: {type(n)}")
    print(f"value model is: {model_val}, and type: {type(model_val)}")
    print(f"value care is: {care}, and type: {type(care)}")
    print(f"value min_z is: {min_z}, and type: {type(min_z)}")
    print(f"value max_z is: {max_z}, and type: {type(max_z)}")
    print(f"value avg_z is: {avg_z}, and type: {type(avg_z)}")
    print(f"value under is: {under}, and type: {type(under)}")
    print(f"value over is: {over}, and type: {type(over)}")
    print(f"value switch_list is: {switch_list}, and type: {type(switch_list)}")
    """
    # Trigger: each time the user gives a click
    if n >= 0:
        # Building the feature vector
        valores = {"AVG_ZScorePesoTalla_12M": avg_z, #[-3,3] --> Slider float
           "MAX_ZScorePesoTalla_12M": max_z, #[-3,3] --> Slider float
           "Veces_DesnutricionSM_12M": under, # 0 en adelante --> Slider enteros positivos
           "Veces_SobrePeso_12M": over, # 0 en adelante --> Slider enteros positivos
           "MIN_ZScorePesoTalla_12M": min_z, # [-3,3] --> Slider float
           } 

        valores["tip_cuidado_niños"] = 9 if care == 8 else care
        valores["ind_discap"] =        "si" if 1 in switches else "ninguna"
        valores["ind_leer_escribir"] =  1 if 2 in switches else 2
        valores["ind_estudia"] =        1 if 3 in switches else 2
        valores["ind_recibe_comida"] =  1 if 4 in switches else 2

        # Turning the feature dict in a pd.dataframe
        base_variables = PredictMini.convertirDicEnBase(valores)

        # Parameter tuning according the selected model
        if model_val == 0:
            img, shap_values = PredictMini.plotShapValues(Modelo_malnutrition_subset,base_variables)
            str_modelo =  "malnutrition"
            ranges = [0.34, 0.46, 0.59]
            print("Malnutrition")
        if model_val == 1:
            img, shap_values = PredictMini.plotShapValues(Modelo_relapse_subset,base_variables)
            str_modelo =  "relapse"
            ranges = [0.45, 0.55, 0.63]
            print("Relapse")
        
        # Prob. predicted for the model
        shap_vals = shap_values[1][0]
        prob = 0.5 + shap_vals.sum()

        # Bar color selection
        if prob <= ranges[0]:
            color_bar = "#1fbd38" #alt. success
        elif prob <= ranges[1]:
            color_bar = "#fff000" #alt. warning
        elif prob <= ranges[2]:
            color_bar = "#f86e02"
        elif prob <= 1:
            color_bar = "#f30404" #alt. danger
        
        # print(type(shap_values[1][0]))
        
        
        var_least, var_great = PredictMini.greatest_least(shap_vals)

        msg_least = ""
        msg_greatest = ""

        if var_least != "":
            msg_least = ("The variable ", html.Span(var_least,className="blue_bold"), " was the one with ",
            "the greatest effect in ", html.Span("reducing", className="blue_bold"), " the risk of suffering ",
            html.Span(str_modelo, className="pink_bold"), ". ")


        if var_great != "":
            msg_great = ("The variable ", html.Span(var_great, className="pink_bold"), " was the one with ",
            "the greatest effect in ", html.Span("increasing", className="pink_bold"), " the risk of suffering ",
            html.Span(str_modelo, className="pink_bold"), ".")


        return (img, f"{prob:.3f}", str_modelo, f"{prob*100:.0f}%", f"{prob*100:.0f}", color_bar, msg_least, msg_great)




"""
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
"""


"""
#Posibles valores de tip_cuidado_niños
1- Asiste a un lugar comunitario, jardín o centro de desarrollo infantil o colegio 
2- Con su padre o madre en la casa
3- Con su padre o madre en el trabajo
4- Con empleada o niñera en la casa
5- Al cuidado de un pariente de 18 años o más
6- Al cuidado de un pariente menor de 18 años
7- En casa solo
9-No aplica por flujo


# Data processing: Calculate SHAP values and brings the image

img, shap_values = PredictMini.plotShapValues(Modelo_relapse_subset,base_variables)
#print(PredictMini.obtenerProbabilidad(Modelo_relapse_subset,base_variables))

features = ["AVG_ZScorePesoTalla_12M","MAX_ZScorePesoTalla_12M","Veces_DesnutricionSM_12M",
            "Veces_SobrePeso_12M","MIN_ZScorePesoTalla_12M"]

# Prob. predicted for the model
prob = 0.5 + shap_values[1][0].sum()

# List of child care categories
child_care_opt
"""
