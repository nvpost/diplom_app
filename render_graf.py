from datetime import datetime as dt
import dash
import dash_html_components as html
import dash_core_components as dcc


import graf_data
d_format = "%Y-%m-%d"

def render_graf(start_date, end_date, bars):
    int_days_delta = (end_date-start_date).days

    return html.Div(children=[
        html.Div(children='Dash: A web application framework for Python'),
        html.Div(children="Start_date: "+start_date.strftime(d_format)),
        html.Div(children="End_Date: "+end_date.strftime(d_format)),
        html.Div(children="Разница в днях: " + str(int_days_delta)),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': graf_data.get_data(start_date, end_date, 1, bars),
                'layout': {'title': 'Dash Data Visualization'}
            }
        )
    ]),
