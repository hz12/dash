
import sys
sys.path.append('D:\Program Files\Python38\Lib\site-packages')
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import re
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    '风场': ['OFES'],
    '波浪': ['高度计资料', 'CFOSAT', 'WW3','NDBC'],
    '海面高度': ['AVISO', 'HYCOM', 'ECCO2','SODA3'],
    '温度': ['REMESS', 'HYCOM', 'ECCO2','SODA3','OFES'],
    '盐度': ['SMOS', 'SMAP', 'HYCOM','ECCO2','SODA3'],
    '流场': ['HYCOM', 'ECCO2','SODA3'],
    '潮汐': ['同潮图', 'UHSLC'],
    '海冰': ['CICE', 'CDR', 'NSDIC', 'EUMETSAT', 'NCEP'],
    '热通量': ['SODA3', 'OFES']
}
app.layout = html.Div([
    html.Div([



     html.Div([
      dcc.RadioItems(
        id='countries-radio',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='温度'
       )
     ],
       style={'width': '49%', 'height':  '250px', 'float': 'center', 'display': 'inline-block'}
     ),


     html.Div([


      dcc.RadioItems(id='cities-radio')
     ],
      style={'width': '49%', 'float': 'right', 'display': 'inline-block'}
     ),

     html.Div([
      html.Hr(),

      html.Div(id='display-selected-values')

     ]),


     html.Div([
         dcc.Dropdown(
             id='demo-dropdown',
             options=[
                 {'label': 'New York City', 'value': 'NYC'},
                 {'label': 'Montreal', 'value': 'MTL'},
                 {'label': 'San Francisco', 'value': 'SF'}
             ],
             value='NYC'
         ),
         html.Div(id='dd-output-container')
]),

     html.Hr(),


     html.Div([
      dcc.Slider(
id='my-slider',
       min=0,
       max=9,
       marks={i: 'Label {}'.format(i) for i in range(10)},
       value=5,
),
html.Div(id='slider-output-container')
]),

     html.Hr(),

html.Div([

dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'SF'],
    labelStyle={'display': 'inline-block'}
)
]),

        html.Hr(),
html.Div([
dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=dt(1995, 8, 5),
        max_date_allowed=dt(2017, 9, 19),
        initial_visible_month=dt(2017, 8, 5),
        date=str(dt(2017, 8, 25, 23, 59, 59))
    ),
    html.Div(id='output-container-date-picker-single')

]),

        html.Hr(),
html.Div([
dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL',
    labelStyle={'display': 'inline-block'}
)


]),







    ])

])




@app.callback(
    Output('cities-radio', 'options'),
    [Input('countries-radio', 'value')])
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(
    Output('cities-radio', 'value'),
    [Input('cities-radio', 'options')])
def set_cities_value(available_options):
    return available_options[0]['value']

"""
@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-radio', 'value'),
     Input('cities-radio', 'value')])
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )
"""
@app.callback(
    Output('output-container-date-picker-single', 'children'),
    [Input('my-date-picker-single', 'date')])
def update_output(date):
    string_prefix = 'You have selected: '
    if date is not None:
        date = dt.strptime(re.split('T| ', date)[0], '%Y-%m-%d')
        date_string = date.strftime('%B %d, %Y')
        return string_prefix + date_string


@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)




if __name__ == '__main__':
    app.run_server(debug=True)
