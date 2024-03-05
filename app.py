'''app.py'''

from dash import dcc, html
import pandas as pd
from dash import Dash, dash_table

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
                        '/assets/styles.css'
]

df = pd.read_csv('D:\\Git_repos\\dash_projects\\p_wurds\\data\\p_wurds.csv')

app = Dash(__name__, external_stylesheets=external_stylesheets)

conditional_formatting_rules = [
    {
        'if': {'row_index': 'odd'},
        'backgroundColor': 'rgb(248, 248, 248)'
    }
]


app.layout = html.Div([
    html.H1("P words"),
    dash_table.DataTable(
        id='P words',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'scroll',
                     
                     
        },
        page_size=10,
        style_data_conditional=conditional_formatting_rules,
        className='xxx'

    )
])
x=2

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
