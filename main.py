import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash_auth
from app import app

# Connect to app pages
from apps import dashboard, form

#USERNAMEINFO = [['user','password']]
#auth = dash_auth.BasicAuth(app,USERNAMEINFO)

sidebar =  html.Div(
    [
        html.Div(
            [   
                html.P("ANALYTICS"),
                dcc.Link('Dashboard', href='/apps/Dashboard'),
                html.P("CHILDREN AT RISK"),
                dcc.Link('Malnutrition', href='/apps/Malnutrition')
            ], className='nav-bar__links'
        ),
        html.Div(
            [
                html.Img(src='/assets/bienestar.png'),
                html.Img(src='/assets/team.png')
            ],
        className="img_footer")
    ], className='app_side_bar'
)

header = html.Div([
    html.Img(src='/assets/correlation.png')
], className="app_header")

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div([
        header,
        html.Div(id='page-content', children=[],className='content')
    ], className='app-container__header__content')
    
], className='rooter_container')

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/Dashboard':
        return dashboard.layout
    if pathname == '/apps/Malnutrition':
        return form.layout
    else:
        return dashboard.layout


if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8080)



