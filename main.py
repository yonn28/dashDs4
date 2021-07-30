import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

# Connect to app pages
from apps import dashboard, form

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.H1('Analyzing malnutrition recidivism in children attended by the ICBF'),
        html.Div(
            [
                dcc.Link('dashboard', href='/apps/dashboard'),
                html.Span(' '),
                html.Span('|'),
                html.Span(' '),
                dcc.Link('form', href='/apps/form'),
            ]
        ),
    ],className='app_header'),
    html.Div(id='page-content', children=[])
    
], className='page_reset')

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/dashboard':
        return dashboard.layout
    if pathname == '/apps/form':
        return form.layout
    else:
        return dashboard.layout


if __name__ == '__main__':
    app.run_server(port='8050', debug=True)