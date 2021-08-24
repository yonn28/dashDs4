import dash_bootstrap_components as dbc
import dash

# meta_tags are required for the app layout to be mobile responsive

app = dash.Dash(__name__, title='ICBF',
                external_stylesheets=[dbc.themes.YETI],
                suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server