'''app.py'''

from dash import Dash, dcc, html, callback, Input, Output
import pandas as pd

df = pd.read_csv('D:\\Git_repos\\dash_projects\\p_wurds\\p_wurds.csv')

external_stylesheets = ['/assets/styles.css']

app = Dash(__name__)
app.css.append_css({"external_url": "/assets/styles.css"})

app.layout = html.Div(
    id='main-container',
    style={
        'display'           : 'flex',
        'flex-direction'    : 'column',  
        'height'            : '100vh'  #full viewport height
    },

    children=[
        html.H1('パスワード', id='table-header'),

        html.Div(
                id='table-container',
                style={
                    'flex': '1',
                    'overflowX': 'auto'
                    },

                children=[
                    html.Table(
                        id='data-table',
                        className='styled-table',
                        children=[
                            html.Thead(
                                html.Tr([html.Th(col) for col in df.columns])
                            ),
                            html.Tbody([
                                html.Tr([
                                    html.Td(df.iloc[i][col]) for col in df.columns
                                ]) for i in range(len(df))
                            ])
                        ]
                    )
                ]
            )
        ]
)
    

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
