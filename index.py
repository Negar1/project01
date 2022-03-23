# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 21:01:13 2022

@author: negar
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Connect to main app.py file
from app import app
#from app import server

# Connect to your app pages
from apps import filtering, Fy_Fz_2D,  complex_data#vs_time,

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Filtering Data ,', href='/apps/filtering'),
        dcc.Link('Force Plots ,', href='/apps/Fy_Fz_2D'),
        #dcc.Link('Raw Plots ,', href='/apps/vs-time'),
        dcc.Link('Average Data', href='/apps/complex_data'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/filtering':
        return [filtering.layout]
    if pathname == '/apps/Fy_Fz_2D':
        return [Fy_Fz_2D.layout]
    #if pathname == '/apps/vs-time':
     #   return [vs_time.layout]
    if pathname == '/apps/complex_data':
        return [complex_data.layout]
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)