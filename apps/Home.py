import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import app



banner_jumbotron = dbc.Jumbotron(
    [
        dbc.Container([
            html.H1("KidNutrilytics\n", className="display-3 product_title"),
            #html.Br(),
            html.Hr(className="my-4"),
            html.P(
                html.U("The ultimate platform to predict malnutrition in children under five years of age"),
                className="lead text_jumbotron",
            ),
            html.Br(),
            html.P(
                "Our models were fitted with 800.000+ registers of children at ICBF",
                className="lead text_jumbotron",
            ),
            html.P(dbc.Button("Learn more", color="primary",
                external_link=True, href="#col-home-2"), className="lead"),
        ], fluid=True, className="text-center text-light"),
    ], className="jumbotron vertical-center", fluid=True
)



text_statistics = html.P("Get insights for the malnutrition in children at ICBF."
                    " Timelines, maps and more plots are there for you.",
                    className="lead just_center")

text_pred_db = html.P("Predict the probability of malnutrition or relapse in children under five years of age at ICBF "
                    "within the next 6 months. Moreover, you can download the information of the children that should be prioritized."
                    " We made use of 60+ nutritional and sociodemographic features.",
                    className="lead just_center")

text_pred_form = html.P("Predict the probability  of malnutrition or relapse on it within the next 6 months"
                        " of a single children by just filling up a form. With only 10 features we can suggest"
                        " if the child should be prioritized.",
                    className="lead just_center")


print("Running...")

# Layout
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
            #html.Img(src='/assets/happychildren.jpg', height="200px"),
                banner_jumbotron,

            ],width=12, className="sm-12"),
        ], #justify="center",#align="center",)
        ),
        dbc.Row([
            
            dbc.Col([html.P("Dashboard", className="homeFont just_center"),
                html.Div([
                    html.Img(src='/assets/home/statistics.png'),
                ], className = "just_center"),
                text_statistics,

                html.P(dbc.Button("Get me there!", id="but-statistics", color="primary",
                external_link=True, href="/apps/Dashboard", className = "just_center"), className="lead"),

            ], width=4, className="text-justify md-4",),# align="center"),


            dbc.Col([html.P("Database Prediction", className="homeFont just_center"),
                html.Div([
                    html.Img(src='/assets/home/db.png'),
                ], className = "just_center"),
                text_pred_db,

                html.P(dbc.Button("Get me there!", id="but-malnutrition", color="primary",
                external_link=True, href="/apps/Malnutrition", className = "just_center"), className="lead"),

            ], width=4,id="col-home-2", className="text-justify md-4", align="center"),


            dbc.Col([html.P("Individual Prediction", className="homeFont just_center"),
                html.Div([
                    html.Img(src='/assets/home/form.png'),
                ], className = "just_center"),
                text_pred_form,

                html.P(dbc.Button("Get me there!", id="but-form", color="primary",
                external_link=True, href="/apps/PredicTool", className = "just_center"), className="lead"),

            ], width=4, className="text-justify md-4",)# align="center"),

        ], justify="center"), #align="center",

    ], fluid=True #className="container-fluid"
)