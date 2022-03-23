# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 18:43:41 2022

@author: negar
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
#from dash import html
import pandas as pd
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df_select= pd.read_excel(DATA_PATH.joinpath("last_Polishing_Conditions_TEMP.xlsx"))
#df = pd.read_excel(r'C:\Users\negar\Documents\ARACA Inc\my place\temp\last_Polishing_Conditions_TEMP.xlsx')
df_select.set_index('Test ID_test', inplace=True, drop=False)

df_select["test_date"]=df_select["Test ID_Date"].dt.date
df1_select=df_select[['Test ID_test', 'test_date', 'Slurry 1_Model', 'Wafers_Condition (New or re-used)','Polishing step 1_Polishing pressure (PSI) set point',
       'Polishing step 1_Wafer rotation rate (RPM) set point',
       'Polishing step 1_Platen rotation rate (RPM) set point',
       'Polishing step 1_velocity (m/s)','Polishing step 1_Polishing time (s)','Related documents_.dat', 'Related documents_.xlsx']]

df1_select.columns=['Test ID', 'Test Date', 'Slurry', 'Wafer Condition','Pressure (PSI)', 'Wafer RPM', 'Platen RPM', 'Velocity (m/s)', "Polish Time","dat_link", "xlsx_link"]


layout = dbc.Container([html.Div([
    dbc.Row([dbc.Col([html.Div([html.H5(['Filtering Available Data'],className='text-left text-primary mt-5')]),]),]),
    
    dbc.Row([
        dbc.Col([html.Div([
            dash_table.DataTable(
                id='datatable-interactivity',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": False, "hideable": False}
                    for i in df1_select.columns[:-2]
                    ],
              
                data=df1_select.to_dict('records'),  # the contents of the table
                editable=True,              # allow editing of data inside all cells
                filter_action="native",     # allow filtering of data by user ('native') or not ('none')
                sort_action="native",       # enables data to be sorted per-column by user or not ('none')
                sort_mode="multi",         # sort across 'multi' or 'single' columns
                column_selectable="multi",  # allow users to select 'multi' or 'single' columns or 'none'
                row_selectable="multi",     # allow users to select 'multi' or 'single' rows or 'none'
                row_deletable=True,         # choose if user can delete a row (True) or not (False)
                selected_columns=[],        # ids of columns that user selects
                selected_rows=[],           # indices of rows that user selects
                page_action="native",       # all data is passed to the table up-front or not ('none')
                page_current=0,             # page number that user is on
                page_size=12,                # number of rows visible per page
                # page_action='none',
                 style_cell={'font-size': '16px',
                   # 'fontWeight': 'bold'
                # 'whiteSpace': 'normal', 'minWidth': 95, 'maxWidth': 95, 'width': 95  
                 },                        # ensure adequate header width when text is shorter than cell's text
                style_header=[{'backgroundColor': 'rgb(210, 210, 210)',
                    'fontWeight': 'bold',
                    "lineWrapping":True,
                    "whiteSpace":"normal"
                    }],
        style_header_conditional=[{"lineWrapping":True,'textAlign': 'center',
                    "whiteSpace":"normal"}],
                
        style_cell_conditional=[    # align text columns to left. By default they are aligned to right
                    {'textAlign': 'center', "lineWrapping":True}],
                
        style_data={                # overflow cells' content into multiple lines
                   # 'whiteSpace': 'normal',
                    'height': 'auto',
                    'font_size': '16px',
                    }
    ),
        ]),]),],className='mt-5 mr-5'),
    ]),])

    
    
   