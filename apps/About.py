'''

1. Librerias:
    
    
'''

#Dash libraries:
    
import dash_bootstrap_components as dbc
import dash_html_components as html


'''

2. Define the layout:
    

'''

layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [   
                        html.Img(src='/assets/pics/Nicolas.png', height="250px",id="nicolas_photo",style={"display":"block","margin-right":"auto","margin-left":"auto"}),
                        html.Div("\t Nicolás Cabrera Malik",style={'color': 'blue', 'fontSize': 20,"text-align": "center"}),
                        html.Div("\t PhD Student",style={'color': 'darkblue', 'fontSize': 15,"text-align": "center"}),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                style={
                                    'height' : '20px',
                                    'width' : '20px',
                                    "display":"block","margin-right":"auto","margin-left":"auto"
                                    })
                                ], href='http://www.linkedin.com/in/nicolas-cabrera-malik')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/Julian.png', height="250px",id="julian_photo",style={"display":"block","margin-right":"auto","margin-left":"auto"}),
                        html.Div("\t Julian Monsalve",style={'color': 'blue', 'fontSize': 20,"text-align": "center"}),
                        html.Div("\t Industrial Engineer",style={'color': 'darkblue', 'fontSize': 15,"text-align": "center"}),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                style={
                                    'height' : '20px',
                                    'width' : '20px',
                                    "display":"block","margin-right":"auto","margin-left":"auto"
                                    })
                                ], href='http://www.linkedin.com/in/julian-monsalve-ace/')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/David.png', height="250px",id="david_photo",style={"display":"block","margin-right":"auto","margin-left":"auto"}),
                        html.Div("\t David Quintero",style={'color': 'blue', 'fontSize': 20,"text-align": "center"}),
                        html.Div("\t Electronic Engineer",style={'color': 'darkblue', 'fontSize': 15,"text-align": "center"}),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                style={
                                    'height' : '20px',
                                    'width' : '20px',
                                    "display":"block","margin-right":"auto","margin-left":"auto"
                                    })
                                ], href='http://www.linkedin.com/in/david-alfredo-quintero-olaya-78a1561b6/')

                        ,html.Hr()]
                    )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [   
                        html.Img(src='/assets/pics/Natalia.png', height="250px",id="natalia_photo",style={"display":"block","margin-right":"auto","margin-left":"auto"}),
                        html.Div("\t Natalia Monroy",style={'color': 'blue', 'fontSize': 20,"text-align": "center"}),
                        html.Div("\t Computer Science Student",style={'color': 'darkblue', 'fontSize': 15,"text-align": "center"}),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                style={
                                    'height' : '20px',
                                    'width' : '20px',
                                    "display":"block","margin-right":"auto","margin-left":"auto"
                                    })
                                ], href='https://www.linkedin.com/in/namonroy96/')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/Daniel.png', height="250px",id="daniel_photo",style={"display":"block","margin-right":"auto","margin-left":"auto"}),
                        html.Div("\t Daniel Ramirez",style={'color': 'blue', 'fontSize': 20,"text-align": "center"}),
                        html.Div("\t Industrial Engineer",style={'color': 'darkblue', 'fontSize': 15,"text-align": "center"}),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                style={
                                    'height' : '20px',
                                    'width' : '20px',
                                    "display":"block","margin-right":"auto","margin-left":"auto"
                                    })
                                ], href='https://www.linkedin.com/in/danielramirezmilano/')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/Yonny.png', height="250px",id="yonny_photo",style={"display":"block","margin-right":"auto","margin-left":"auto"}),
                        html.Div("\t Yonny Nova",style={'color': 'blue', 'fontSize': 20,"text-align": "center"}),
                        html.Div("\t Electronic Engineer",style={'color': 'darkblue', 'fontSize': 15,"text-align": "center"}),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                style={
                                    'height' : '20px',
                                    'width' : '20px',
                                    "display":"block","margin-right":"auto","margin-left":"auto"
                                    })
                                ], href='https://www.linkedin.com/in/yonny-clinton-nova-cucaita/')

                        ,html.Hr()]
                    )
            ]
        )
    ]
)