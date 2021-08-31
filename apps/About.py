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
                        html.Img(src='/assets/pics/nicolas.png', height="250px",id="nicolas_photo",className='about_us__foto'),
                        html.Div("\t Nicolás Cabrera Malik",className='about_us__name'),
                        html.Div("\t PhD Student",classNhtml.Div("\t Electronic Engineer",className='about_us__rol'),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                className='about_us__img_footer')
                                ], href='http://www.linkedin.com/in/nicolas-cabrera-malik')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/julian.png', height="250px",id="julian_photo",className='about_us__foto'),
                        html.Div("\t Julian Monsalve",className='about_us__name'),
                        html.Div("\t Industrial Engineer",classNhtml.Div("\t Electronic Engineer",className='about_us__rol'),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                className='about_us__img_footer')
                                ], href='http://www.linkedin.com/in/julian-monsalve-ace/')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/david.png', height="250px",id="david_photo",className='about_us__foto'),
                        html.Div("\t David Quintero",className='about_us__name'),
                        html.Div("\t Electronic Engineer",className='about_us__rol'),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                className='about_us__img_footer')
                                ], href='http://www.linkedin.com/in/david-alfredo-quintero-olaya-78a1561b6/')

                        ,html.Hr()]
                    )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [   
                        html.Img(src='/assets/pics/natalia.png', height="250px",id="natalia_photo",className='about_us__foto'),
                        html.Div("\t Natalia Monroy",className='about_us__name'),
                        html.Div("\t Computer Science Student",classNhtml.Div("\t Electronic Engineer",className='about_us__rol'),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                className='about_us__img_footer')
                                ], href='https://www.linkedin.com/in/namonroy96/')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/Daniel.png', height="250px",id="daniel_photo",className='about_us__foto'),
                        html.Div("\t Daniel Ramirez",className='about_us__name'),
                        html.Div("\t Industrial Engineer",classNhtml.Div("\t Electronic Engineer",className='about_us__rol'),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                className='about_us__img_footer')
                                ], href='https://www.linkedin.com/in/danielramirezmilano/')

                        ,html.Hr()]
                    ),
                dbc.Col(
                    [
                        html.Img(src='/assets/pics/Yonny.png', height="250px",id="yonny_photo",className='about_us__foto'),
                        html.Div("\t Yonny Nova",className='about_us__name'),
                        html.Div("\t Electronic Engineer",className='about_us__rol'),
                        html.A([
                                html.Img(
                                src='/assets/linkedin.png',
                                className='about_us__img_footer')
                                ], href='https://www.linkedin.com/in/yonny-clinton-nova-cucaita/')

                        ,html.Hr()]
                    )
            ]
        )
    ]
)