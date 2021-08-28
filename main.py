import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
#import dash_auth
from app import app

# Connect to app pages
#from apps import dashboard, Malnutrition, PredicTool
from apps import PredicTool
# USERNAMEINFO = [['user','password']]
# auth = dash_auth.BasicAuth(app,USERNAMEINFO)

"""
header = html.Div([
    html.Img(src='/assets/correlation.png')
], className="app_header")
"""

header = dbc.Navbar(
    [
        html.A(
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand("ICBF - Children Malnutrition in Colombia", className="font-weight-bold"), align="left")
                ],
                align="center",
            ),
        ),
        dbc.Collapse(
            html.Img(src='/assets/correlation.png', height="50px", className="ml-auto flex-nowrap mt-3 mt-md-0"), id="navbar-collapse", navbar=True, is_open=False
        ),
    ],
    color="white",
    light=True,
)

sidebar = html.Div(
    [
        dbc.Nav(
            [
                html.Hr(),
                html.P("ANALYTICS", className='text-p'),
                #dbc.NavLink('Dashboard', href='/apps/Dashboard', active="exact"),
                html.P("CHILDREN AT RISK", className='text-p'),
                #dbc.NavLink('Malnutrition', href='/apps/Malnutrition', active="exact"),
                #dbc.NavLink('Relapse', href='/apps/Relapse', active="exact"),
                dbc.NavLink('Prediction Tool', href='/apps/PredicTool', active="exact"),
                #dbc.NavLink('About Us', href='/apps/About', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Div(
            [
                html.Img(src='/assets/bienestar.png'),
                html.Img(src='/assets/team.png')
            ],
            className="img_footer")
    ], className='app_side_bar'
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div([
        header,
        html.Div(id='page-content', children=[], className='content')
    ], className='app-container__header__content')

], className='rooter_container')


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    #if pathname == '/apps/Dashboard':
        #return dashboard.layout
    #if pathname == '/apps/Malnutrition':
        #return Malnutrition.layout
    if pathname == '/apps/PredicTool':
        return PredicTool.layout
    #else:
        #return dashboard.layout


if __name__ == '__main__':
    #app.run_server(debug=True, host="0.0.0.0", port=8080)
    app.run_server(debug=True, port=8080)



