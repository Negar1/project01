# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 17:30:05 2022

@author: negar
"""

import dash
import dash_bootstrap_components as dbc


app=dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP #MINTY
                                             ], meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
                                                            
# meta_tags are required for the app layout to be mobile responsive

server = app.server