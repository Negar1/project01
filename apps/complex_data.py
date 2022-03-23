# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:09:47 2022

@author: negar
"""

import pandas as pd
import numpy as np
#from datetime import datetime
#from datetime import date
import os

#import dash
import plotly.express as px
#from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

dfc= pd.read_excel(DATA_PATH.joinpath("last_Polishing_Conditions_TEMP.xlsx"))

#dfc = pd.read_excel(r'C:\Users\negar\Documents\ARACA Inc\my place\temp\last_Polishing_Conditions_TEMP.xlsx')
dfc.set_index('Test ID_test', inplace=True, drop=False)

#df11 = pd.read_excel(r'C:\Users\negar\Documents\ARACA Inc\my place\temp\last_Polishing_Conditions_TEMP.xlsx')
df11=pd.read_excel(DATA_PATH.joinpath("last_Polishing_Conditions_TEMP.xlsx"))
df11.set_index('Test ID_test', inplace=True, drop=False)

test_names=[{'label': name , 'value': name} for name in dfc["Test ID_test"].unique()]
test_dates=[{'label': date , 'value': date} for date in dfc["Test ID_Date"].unique()]
pad_manuf=[{'label': manuf , 'value': manuf} for manuf in dfc["Pad_Manufacturer"].unique()]
pad_model=[{'label': model , 'value': model} for model in dfc["Pad_Model (VP6000/vision pad 6000)"].unique()]
pressure_1=[{'label': pressure , 'value': pressure} for pressure in dfc["Polishing step 1_Polishing pressure (PSI) set point"].unique()]
wafer_RPM_1=[{'label': wafer_RPM  , 'value': wafer_RPM} for wafer_RPM  in dfc["Polishing step 1_Wafer rotation rate (RPM) set point"].unique()]
platen_RPM_1=[{'label': platen_RPM , 'value': platen_RPM} for platen_RPM in dfc["Polishing step 1_Platen rotation rate (RPM) set point"].unique()]
velocity_1=[{'label': veocity , 'value': veocity} for veocity in dfc["Polishing step 1_velocity (m/s)"].unique()]
time_1=[{'label': time , 'value': time} for time in dfc["Polishing step 1_Polishing time (s)"].unique()]

dfc1=dfc[['Test ID_test', 'Test ID_Date', 'Polishing step 1_Polishing pressure (PSI) set point',
       'Polishing step 1_Wafer rotation rate (RPM) set point',
       'Polishing step 1_Platen rotation rate (RPM) set point',
       'Polishing step 1_velocity (m/s)','Polishing step 1_Polishing time (s)','Related documents_.dat', 'Related documents_.xlsx']]
dfc1.columns=['Test ID', 'Test Date', 'Pressure (PSI)', 'Wafer RPM', 'Platen RPM', 'Velocity (m/s)', "Polish Time","dat_link", "xlsx_link"]

axis_select=[{'label': 'COF' , 'value': "Mean COF"},
             {'label': 'Average Pad Temperature (C)', 'value': "Mean Pad Temp (C)"},
             {'label': 'P.V (Pa.m/s)', 'value': 'P.V (Pa.m/s)'},
             {'label': "Pseudo-Sommerfeld number (m/(Pa.s))", 'value':"Pseudo-Sommerfeld number (m/Pa.s)"},
             {'label': "Power Density (m.Pa/s)", 'value':"Power Density (Pa.m/s)"},
             {'label': 'Amount Removed (A)' , 'value': 'Amount Removed (A)'},
             {'label': 'WIWNU (%)' , 'value': 'WIWNU (%)'},
             {'label': 'Directivity' , 'value': 'Directivity'},
             {'label': 'Pressure (PSI)' , 'value':'Pressure (PSI)'},
             {'label': 'Velocity (m/s)', 'value': 'Velocity (m/s)'},
             {'label': 'Wafer RPM' , 'value':'Wafer RPM'},
             {'label': 'Platen RPM', 'value': 'Platen RPM'},
             {'label': '1/T (1/K)' , 'value':'1/T (1/K)'},
             {'label':"RR (A/min)", 'value': "Mean Removal Rate (A/min)"},
             {'label': 'ln(RR) (m/s)', 'value': 'ln(RR)'},
                           ]

color_select=[
             {'label': 'Pressure (PSI)' , 'value':'Pressure (PSI)'},
             {'label': 'Velocity (m/s)', 'value': 'Velocity (m/s)'},
             {'label': 'Wafer RPM' , 'value':'Wafer RPM'},
             {'label': 'Platen RPM', 'value': 'Platen RPM'},
                           ]

df_complex=pd.DataFrame([[np.nan]*20]*1 ,columns=["Test_ID", "Pressure (PSI)", "Velocity (m/s)", "Mean COF", "Shear Force Variance",
                                "Normal Force Variance", "Mean Pad Temp (C)", "Mean Removal Rate (A/min)", "WIWNU (%)",
                                "Directivity", "Normal Force", "Shear Force", 'P.V (Pa.m/s)', "Pseudo-Sommerfeld number (m/Pa.s)",
                                "Power Density (Pa.m/s)", 'Amount Removed (A)', 'Wafer RPM', 'Platen RPM','1/T (1/K)', 'ln(RR)'])

#app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP #MINTY
 #                                            ], meta_tags=[{'name': 'viewport',
  #                          'content': 'width=device-width, initial-scale=1.0'}])
#

layout = dbc.Container([html.Div([
     dbc.Row([
        dbc.Col(html.H2("Averages:",
                        className='text-left text-secondary mb-4'),
                width=12)
    ]),    
    dbc.Row([
        dbc.Col(html.H4("Please select the averaging time interval:",
                        className='text-left text-danger mb-4'),
                width=12)
    ]),    
    dbc.Row([dbc.Col([html.Div([html.Label(['Initial Time (s):'],style={'font-weight': 'bold'})]),# "text-align": "left"
                          dcc.Input(id='init_time',
                                    type='number',
                                    placeholder="Please Insert a Range",
                                    debounce=False,                      
                                    min=0, max=70, step=0.001,         
                                    #minLength=0, maxLength=50,          
                                    autoComplete='on',
                                    disabled=False,                     
                                    readOnly=False,                     
                                    required=True,                     
                                    size="40",                          
                                    style={'width':"60%"},            
                                   # className='',                     
                                    persistence='True',
                                    persistence_type='memory',  
                                )],width={'size':6}),
                 dbc.Col([html.Div([html.Label(['End Time (s):'],style={'font-weight': 'bold'})]),
                          dcc.Input(id='end_time',
                                    type='number',
                                    placeholder="Please Insert a Range",
                                    debounce=False,                      
                                    min=0, max=70, step=0.001,         
                                    #minLength=0, maxLength=50,          
                                    autoComplete='on',
                                    disabled=False,                     
                                    readOnly=False,                     
                                    required=True,                     
                                    size="40",                          
                                    style={'width':"60%"},            
                                   # className='',                     
                                    persistence='True',
                                    persistence_type='memory',  
                                )],width={'size':6})
            ],className='mr-5'),
    
    
    
    dbc.Row([dbc.Col([html.Div([html.H5(['Selecting Test IDs Manually:'],className='text-left text-primary mt-5')]),]),]),
    dbc.Row([dbc.Col([#html.Div([html.Label(['Name:'],style={'font-weight': 'bold'})]),
                     dcc.Dropdown(id='test_name',
                                   options= test_names,
                                   #value="Cu_001_01",
                                     #optionHeight=35,                    #height/space between dropdown options
                                   placeholder='Please select...',
                                   multi=True,
                                   searchable=True,
                                   clearable=False,
                                   style={'width':"100%"}, 
                                   className='text-justify bg-light text-nowrap mr-4', 
                                     # persistence=True,             #remembers dropdown value. Used with persistence_type
                                     # persistence_type='memory'     #remembers dropdown value selected until...'memory'/'session'/'local' 
                                   ),], 
                    ),],className='mr-5' ),
    dbc.Row([
        dbc.Col([html.Div([
            dash_table.DataTable(
                id='adding-rows-table',
                columns=[{
                    'name': '{}'.format(i),
                    'id': '{}'.format(i),
                    'deletable': False,
                    'renamable': False
                } for i in df_complex.columns[:-10]],
                data=[
         ###            {'{}'.format(i): dcc.Markdown(id="var_{}".format(i)) for i in df_complex.columns}
                ],
                editable=True,
                row_deletable=False,
                style_cell={'font-size': '16px'},                        # ensure adequate header width when text is shorter than cell's text
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
    
###______ to ckeck outputs___________###   
    
  #  dbc.Row([dbc.Col([html.Div([html.H6("INAAA", className="text-center bg-light text-nowrap text-primary border font-weight-bolder mt-5"),
#                                 #dcc.Markdown(id='out_var')],className="text-center"),]),
    #                             html.Div(id='out_var')])])
   #         ]),
    dbc.Row([dbc.Col([html.Div([html.Label(['Select x:'],style={'font-weight': 'bold'})]),# "text-align": "left"
                      dcc.Dropdown(id='variables-3-x',
                                   options=axis_select,
                                   value='P.V (Pa.m/s)',
                                   multi=False,
                                   style={'width':"100%"},  
                                   clearable=False),]), #width={'size':6  #4 out of 12 columns,
                                           #"'offset':1, 'order':1"
                                      #    }),
             dbc.Col([html.Div([html.Label(['Select y:'],style={'font-weight': 'bold'})]),
                      dcc.Dropdown(id='variables-3-y',
                                   options=axis_select,
                                   value='Mean COF',
                                   multi=False,
                                   style={'width':"100%"},  
                                   clearable=False),]),
             dbc.Col([html.Div([html.Label(['Select Constants:'],style={'font-weight': 'bold'})]),
                      dcc.Dropdown(id='variables-3-color',
                                   options=color_select,
                                   value='Pressure (PSI)',
                                   multi=False,
                                   style={'width':"100%"},  
                                   clearable=False),]),
            ],className='text-justify bg-light text-nowrap mt-5'),
    
    dbc.Row(dbc.Col([html.Div([dcc.Graph(id='var-container-3')])], width={'size':6,  "offset":3})),#className='mh-100'),
    dbc.Row([dbc.Col([html.Div(html.Label(['X_min:'],
                                         style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                      dcc.Input(id="X_range_min_3", #id='my_{}'.format(x),     
                                  type='number',
                                  placeholder="insert a range",#"insert {}".format(x),  # A hint to the user of what can be entered in the control
                                  debounce=False,                      # Changes to input are sent to Dash server only on enter or losing focus
                                  min=-50, max=40000, step=0.00001,         # Ranges of numeric value. Step refers to increments
                                #minLength=0, maxLength=50,          # Ranges for character length inside input box
                                  autoComplete='on',
                                  disabled=False,                     # Disable input box
                                  readOnly=False,                     # Make input box read only
                                  required=False,                     # Require user to insert something into input box
                                  size="40",                          # Number of characters that will be visible inside box
                                  style={'width':"60%"},            # Define styles for dropdown (Dropdown video: 13:05)
                               # className='',                     # Define style from separate CSS document (Dropdown video: 13:05)
                                  persistence='True',                   # Stores user's dropdown changes in memory (Dropdown video: 16:20)
                                  persistence_type='memory',              # Stores user's dropdown changes in memory (Dropdown video: 16:20)
                          )],width={'size':2, "offset":4}),
             dbc.Col([html.Div(html.Label(['X_max:'],
                                         style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                     dcc.Input(id="X_range_max_3",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=40000, step=0.00001,         
                                #minLength=0, maxLength=50,         
                                  autoComplete='on',
                                  disabled=False,                     
                                  readOnly=False,                     
                                  required=False,                     
                                  size="40",                          
                                  style={'width':"60%"},            
                               # className='',                     
                                  persistence='True',                   
                                  persistence_type='memory',              
                          )],width={'size':2}),
             dbc.Col([html.Div(html.Label(['Y_min:'],
                                         style={'font-weight': 'bold'})),
                     dcc.Input(id="Y_range_min_3",     
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=40000, step=0.00001,         
                                #minLength=0, maxLength=50,          
                                  autoComplete='on',
                                  disabled=False,                     
                                  readOnly=False,                     
                                  required=False,                     
                                  size="40",                          
                                  style={'width':"60%"},            
                               # className='',                     
                                  persistence='True',                   
                                  persistence_type='memory',              
                          )],width={'size':2}),
             dbc.Col([html.Div(html.Label(['Y_max:'],
                                         style={'font-weight': 'bold'})), 
                     dcc.Input(id="Y_range_max_3",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=40000, step=0.00001,         
                                #minLength=0, maxLength=50,          
                                  autoComplete='on',
                                  disabled=False,                     
                                  readOnly=False,                     
                                  required=False,                     
                                  size="40",                          
                                  style={'width':"60%"},            
                                  #className='',                     
                                  persistence='True',                   
                                  persistence_type='memory',        
                          )],width={'size':2}),], #align="center")  # Vertical: start, center, end    #at the end of row, aligns different columns
           ),
    
 ]), ])   
   

@app.callback(
    [
    Output('adding-rows-table', 'data'),
    #Output("out_var", "children"),
    Output("var-container-3", "figure"),
    ],
    
    [#Input('store-data', 'data'),
     #Input(component_id='test_date', component_property="value"),   
     Input(component_id='test_name', component_property="value"),
     Input(component_id='init_time', component_property='value'),
     Input(component_id='end_time', component_property='value'),
     Input(component_id='variables-3-x', component_property='value'),
     Input(component_id='variables-3-y', component_property='value'),
     Input(component_id='variables-3-color', component_property='value'),   
     ###Input(component_id='marker_var', component_property='value'),  
     Input(component_id='X_range_min_3', component_property='value'),
     Input(component_id='X_range_max_3', component_property='value'),
     Input(component_id='Y_range_min_3', component_property='value'),
     Input(component_id='Y_range_max_3', component_property='value'),
    ],
   
    State('adding-rows-table', 'data'),
)

def add_row(ids2, init, final, 
            selected_val_3_x,selected_val_3_y,selected_3_color, X_range_min_3, X_range_max_3, Y_range_min_3, Y_range_max_3,
           rows):#, columns):
#     
   
    my_dff1 = dfc1
    my_dff11=df11
    
   
    


    ids=ids2
    
    if len(ids) > 0:
        rows=[]
        for id_ in ids:
            temp_df=pd.read_csv(os.path.join(".\datasets",my_dff1.loc[id_]['dat_link'].replace(".dat", ".csv")))
            samp_rate=int(temp_df['Sampling Rate'][1])
        
            
            
            rows.append({c: [id_, my_dff1.loc[id_]['Pressure (PSI)'], 
                             my_dff1.loc[id_]['Velocity (m/s)'],
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["COF"].mean(), 3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Shear Force"].std()**2, 3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Normal Force"].std()**2, 3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Temperature"].mean(), 3),
                             round(my_dff11.loc[id_]['Amount Removed (A)']/(my_dff1.loc[id_]['Polish Time']/60),3), 
                             round(my_dff11.loc[id_]['WIWNU (%)'], 3),
                             round(((temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Shear Force"].std()**2)/(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Normal Force"].std()**2)),3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Shear Force"].mean(),3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Normal Force"].mean(),3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]['pv'].mean(),3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]['v/p'].mean(),8),
                           # ### round(my_dff1.loc[id_]['Velocity (m/s)']/(my_dff1.loc[id_]['Pressure (PSI)']*6894.75729),8),
                            #### round(my_dff1.loc[id_]['Pressure (PSI)']*my_dff1.loc[id_]['Velocity (m/s)']*6894.75729*(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["COF"].mean()),3),
                             round(temp_df.iloc[(init*samp_rate):(final*samp_rate)]['Power Density'].mean(),3),
                             my_dff11.loc[id_]['Amount Removed (A)'],
                             my_dff1.loc[id_]['Wafer RPM'],
                             my_dff1.loc[id_]['Platen RPM'],
                             round((1/(temp_df.iloc[(init*samp_rate):(final*samp_rate)]["Temperature"].mean()+273.16)), 7),
                             round(np.log(my_dff11.loc[id_]['Amount Removed (A)']*0.0000000001/my_dff1.loc[id_]['Polish Time']),3)
                            ][j] for j, c in enumerate(df_complex.columns)})
            
                 
            new_df=pd.DataFrame(rows)#.iloc[0][1]
    
            

    line_chart_3=px.line(#scatter(#line(
        data_frame= new_df,
        x=selected_val_3_x,
        y=selected_val_3_y,
#         x="Mean COF",
#         y="Directivity",
        range_x=[X_range_min_3, X_range_max_3], #[-60,150],
        range_y=[Y_range_min_3, Y_range_max_3],
        markers=True,
        symbol = new_df[selected_3_color],
        symbol_sequence= ['circle-open', 'circle', 'triangle-up-open', 'square-open'],
        color=selected_3_color)
        # #     if len(selected_val_3_y)==1:
        # #         line_chart_3.update_layout(yaxis_title=str(selected_val_2).split("'")[1])
    line_chart_3.update_layout(yaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                          )))
    line_chart_3.update_layout(xaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                          )))
    line_chart_3.update_xaxes(tickwidth=2, #ticks="outside",  tickcolor='crimson', ticklen=10
                               #tickangle=45, 
                                tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                             ))
    line_chart_3.update_yaxes(tickwidth=2,#ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1
                    tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                             ))
    line_chart_3.update_traces(marker_size=10)

    #return rows,  str(123)#line_chart_3
    return rows, line_chart_3#, str(ids)]