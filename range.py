from datetime import datetime as dt
import dash
import dash_html_components as html
import dash_core_components as dcc


import render_graf
import available_fields as af

bars = af.default_data[:4]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

d_format = "%Y-%m-%d"

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.DatePickerRange(
        id='my-date-picker-range',
        min_date_allowed=dt(2018, 11, 1),
        max_date_allowed=dt(2020, 2, 20),
        initial_visible_month=dt(2019, 10, 1),
        start_date=dt(2019, 10, 1),
        end_date=dt(2019, 12, 3),
        display_format='DD.MM.YY'
    ),


    html.Div(id='output-container-date-picker-range')
])



@app.callback(
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')]
)

def update_output(start_date, end_date):
        start_date = dt.strptime(start_date.split('T')[0], d_format)
        end_date = dt.strptime(end_date.split('T')[0], d_format)
        return render_graf.render_graf(start_date, end_date, bars)




if __name__ == '__main__':
    app.run_server(debug=True)