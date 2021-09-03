import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from utils import zscore_plot
from app import app
import ssl
import requests

ssl._create_default_https_context = ssl._create_unverified_context

"""
-------------------------------------------Data(Microservices Requests)------------------------------------
"""

#-----------------------------------------*Relapse*-------------------------------------
#probability range
p_range_r = requests.get('https://sharpmicro2-zbca65qbuq-nn.a.run.app/api/v2/rel_p').json()
#number of children at risk
n_children_r = requests.get('https://sharpmicro2-zbca65qbuq-nn.a.run.app/api/v2/rel_n').json()
#Shap values img
shap_r = requests.get('https://sharpmicro2-zbca65qbuq-nn.a.run.app/api/v2/shap_rel').json()
#Table with data to show on the app
df_show_r_dict = requests.get("https://sharpmicro2-zbca65qbuq-nn.a.run.app/api/v2/show_rel", headers={"content-type":"text", "initial":str(0), "end":str(1000)}).json()
df_show_r = pd.DataFrame.from_dict(df_show_r_dict)

show_table_r = df_show_r[['Child ID', 'MIN ZScore', 'MAX ZScore', 'AVG ZScore', 'Malnutrition Count', 'Appropiate Count',
                    'Probability']].copy()

plot_table_r = df_show_r[['Child ID', 'ind_estudia', 'ingresos_promp_imp', 'uni_dias_agua', 'noprivaciones',
                    'tipo_cuidado', 'cod_clase', 'sexo_persona', 'estrato']].copy()
dist_plot_r = zscore_plot.zscore_distplot(show_table_r)

#-----------------------------------------*Malnutrition*----------------------------------
#probability range
p_range_m = requests.get('https://sharpvalues1-zbca65qbuq-nn.a.run.app/api/v2/mal_p').json()
#number of children at risk
n_children_m = requests.get('https://sharpvalues1-zbca65qbuq-nn.a.run.app/api/v2/mal_n').json()
#Shap values img
shap_m = requests.get('https://sharpvalues1-zbca65qbuq-nn.a.run.app/api/v2/shap_mal').json()
#Table with data to show on the app
df_show_m_dict = requests.get("https://sharpvalues1-zbca65qbuq-nn.a.run.app/api/v2/show_mal", headers={"content-type":"text", "initial":str(0), "end":str(20)}).json()
df_show_m = pd.DataFrame.from_dict(df_show_m_dict)

show_table_m = df_show_m[['Child ID', 'MIN ZScore', 'MAX ZScore', 'AVG ZScore', 'Malnutrition Count', 'Appropiate Count',
                    'Probability']].copy()

plot_table_m = df_show_m[['Child ID', 'ind_estudia', 'ingresos_promp_imp', 'uni_dias_agua', 'noprivaciones',
                    'tipo_cuidado', 'cod_clase', 'sexo_persona', 'estrato']].copy()

dist_plot_m = zscore_plot.zscore_distplot(show_table_m)

PAGE_SIZE = 20

"""
--------------------------------------------Layout--------------------------------------------
"""
layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                [
                    html.H4("Risk Selection", className="card-title"),
                    html.Hr(id="hr_1"),
                    dbc.Row(
                        dbc.Col(dcc.Dropdown(
                                    id="model",
                                    options=[{'value': 0, 'label': "Malnutrition"}, {'value': 1, 'label': "Relapse"}],
                                    value=1,
                        )), className="mb-3"),
                    dbc.Row(
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                            [
                                dbc.Row([
                                    dbc.Col(html.H5(id ="n_children", className="card-v"), width={"size": 4,"offset": 1}),
                                    dbc.Col(html.H5(id ="p_range", className="card-v"), width={"size": 5, "offset": 1}),
                                ]),
                                dbc.Row([
                                    dbc.Col(html.H6("Children at Risk", className='text-v')),
                                    dbc.Col(html.H6("Probability Range", className='text-v')),
                                ]),
                            ])
                        ,color="primary", outline=True)
                    )),
                ]),color="light", outline=True)
        , width=3),
        dbc.Col(
            dbc.Card(
                dbc.CardImg(src="/assets/happychildren.jpg")
            , color="light", outline=True), width=9)
    ], className="mb-4",),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                [
                    html.H4("SHAP Values", className="card-title"),
                    html.Hr(id="hr_1"),
                    dbc.CardImg(id="shap_img")
                ]
                ),color="light", outline=True),
        width=5),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                [
                    html.H4("AVG ZScore Distplot for Children", className="card-title"),
                    html.Hr(id="hr_1"),
                    dcc.Graph(id="dist_plot", figure={})
                ]),
            color="light", outline=True)
        , width=7)
    ], className="mb-4",),
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                [
                    html.H4("What Characterizes them?", className="card-title"),
                    html.Hr(id="hr_1"),
                    dcc.Dropdown(id="user_choice", options=[{"label": "Education", "value": "ind_estudia"},
                                              {"label": "Water Days Access", "value": "uni_dias_agua"},
                                              {"label": "Avg Income", "value": "ingresos_promp_imp"},
                                              {"label": "No. Privations", "value": "noprivaciones"},
                                              {"label": "Gender", "value": "sexo_persona"},
                                              {"label": "Care Type", "value": "tipo_cuidado"},
                                              {"label": "Class Cod", "value": "cod_clase"}],
                             value="sexo_persona", clearable=False),
                    dcc.Graph(id="my_bar", figure={})
                ]
                ),color="light", outline=True),
        width = 5),
        dbc.Col(
            dbc.Card(
            dbc.CardBody(
            [
                html.H4("Children Information", className="card-title"),
                html.Hr(id="hr_1"),
                dash_table.DataTable(id="datatable-paging-page-count",
                                     columns=[
                                         {"name": i, "id": i} for i in show_table_r.columns
                                     ],
                                     page_current=0,
                                     page_size=PAGE_SIZE,
                                     page_action="custom",
                                     page_count=50,
                                     style_as_list_view=True,
                                     style_cell={"padding": "5px",
                                                 "minWidth": "50px", "width": "50px", "maxWidth": "50px"
                                                 },  # style_cell refers to the whole table
                                     style_header={
                                         "backgroundColor": "#F9FAFD",
                                         "fontWeight": "bold",
                                         "color": "#017EFA"
                                     },
                                     fixed_rows={"headers": True},
                                     style_cell_conditional=[
                                        {"if": {"column_id": "Child ID"},
                                            "textAlign": "left",
                                            "width": "10%",
                                         },
                                        {"if": {"column_id": "MIN ZScore"},
                                            "width": "10%",
                                         },
                                        {"if": {"column_id": "MAX ZScore"},
                                            "width": "10%",
                                         },
                                     ],
                                     style_table={"height": 400},
                                     style_data_conditional=[
                                         {
                                         "if": {"column_id": "Child ID"},
                                            "backgroundColor": "#F0F2F8",
                                         },
                                         {
                                         "if": {"column_id": "Malnutrition Count"},
                                            "backgroundColor": "#F0F2F8",
                                         },
                                         {
                                         "if": {"column_id": "Probability"},
                                            "backgroundColor": "#F0F2F8",
                                         },
                                     ]
                                     ),
                dbc.Button("Download CSV", color="primary", className="mr-1", id="btn_csv"),
                dcc.Download(id="download-dataframe-csv"),
            ]),color="light", outline=True),
        width = 7)
    ], className="mb-4",)
], fluid=True)

"""
--------------------------------------------Callbacks--------------------------------------------
"""
"""
callback to update graphs depending on the model selected
"""
@app.callback(
    [Output(component_id="n_children", component_property="children"),
    Output(component_id="p_range", component_property="children"),
    Output(component_id="shap_img", component_property="src"),
    Output(component_id="dist_plot", component_property="figure"),],
    [Input(component_id="model", component_property="value"),]
)
def update_graphs(model_choice):
    if model_choice == 0:
        c = n_children_m
        p = p_range_m
        img = shap_m
        dist_p = dist_plot_m
    if model_choice == 1:
        c = n_children_r
        p = p_range_r
        img = shap_r
        dist_p = dist_plot_r
    return c, p, img, dist_p

"""
callback to update data to display on table on the model selected and pages
"""
@app.callback(
    Output('datatable-paging-page-count', 'data'),
    [Input('datatable-paging-page-count', "page_current"),
    Input('datatable-paging-page-count', "page_size"),
    Input(component_id="model", component_property="value"),])
def update_table(page_current,page_size, model):
    if model == 0:
        return show_table_m.iloc[
        page_current*page_size:(page_current+ 1)*page_size
        ].to_dict('records')
    if model == 1:
        return show_table_r.iloc[
        page_current*page_size:(page_current+ 1)*page_size
        ].to_dict('records')

"""
callback to update bar plots according to the user choice on dropdown
"""
@app.callback(
    Output("my_bar", "figure"),
    [Input("user_choice", "value"),
     Input(component_id="model", component_property="value"),]
)

def bar_plots(value, model):
    if model == 0:
        df = plot_table_m
    if model == 1:
        df = plot_table_r
    fig = px.histogram(df, x=value, color_discrete_sequence=['#1CBE4F'])
    fig.update_layout(xaxis_title=value, yaxis_title="Count")
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig

"""
callback to download .csv file with info of the children at risk
"""
@app.callback(
    Output("download-dataframe-csv", "data"),
    [Input("btn_csv", "n_clicks"),
    Input(component_id="model", component_property="value"),],
    prevent_initial_call=True,
)
def func(n_clicks, model):
    if n_clicks > 0:
        if model == 0:
            df = show_table_m
        if model == 1:
            df = show_table_r
        return dcc.send_data_frame(df.to_csv, "children_at_risk.csv")
