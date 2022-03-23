# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 20:47:53 2022

@author: negar
"""

#import dash
#import plotly 
import plotly.express as px
#import plotly.io as pio
import os
#import statsmodels.api as sm
#from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
#import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
#from dash import html
import pandas as pd
import pathlib
from app import app


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df= pd.read_excel(DATA_PATH.joinpath("last_Polishing_Conditions_TEMP.xlsx"))
#df = pd.read_excel(r'C:\Users\negar\Documents\ARACA Inc\my place\temp\last_Polishing_Conditions_TEMP.xlsx')
df.set_index('Test ID_test', inplace=True, drop=False)

test_names=[{'label': name , 'value': name} for name in df["Test ID_test"].unique()]
"""
test_dates=[{'label': date , 'value': date} for date in df["Test ID_Date"].unique()]
pad_manuf=[{'label': manuf , 'value': manuf} for manuf in df["Pad_Manufacturer"].unique()]
pad_model=[{'label': model , 'value': model} for model in df["Pad_Model (VP6000/vision pad 6000)"].unique()]
pressure_1=[{'label': pressure , 'value': pressure} for pressure in df["Polishing step 1_Polishing pressure (PSI) set point"].unique()]
wafer_RPM_1=[{'label': wafer_RPM  , 'value': wafer_RPM} for wafer_RPM  in df["Polishing step 1_Wafer rotation rate (RPM) set point"].unique()]
platen_RPM_1=[{'label': platen_RPM , 'value': platen_RPM} for platen_RPM in df["Polishing step 1_Platen rotation rate (RPM) set point"].unique()]
velocity_1=[{'label': veocity , 'value': veocity} for veocity in df["Polishing step 1_velocity (m/s)"].unique()]
time_1=[{'label': time , 'value': time} for time in df["Polishing step 1_Polishing time (s)"].unique()]


df1=df[['Test ID_test', 'Test ID_Date', 'Slurry 1_Model', 'Wafers_Condition (New or re-used)','Polishing step 1_Polishing pressure (PSI) set point',
       'Polishing step 1_Wafer rotation rate (RPM) set point',
       'Polishing step 1_Platen rotation rate (RPM) set point',
       'Polishing step 1_velocity (m/s)','Polishing step 1_Polishing time (s)','Related documents_.dat', 'Related documents_.xlsx']]

df1.columns=['Test ID', 'Test Date', 'Slurry', 'Wafer Condition','Pressure (PSI)', 'Wafer RPM', 'Platen RPM', 'Velocity (m/s)', "Polish Time","dat_link", "xlsx_link"]
"""

df1=df[['Test ID_test', 'Test ID_Date', 'Related documents_.dat', 'Related documents_.xlsx']]

df1.columns=['Test ID', 'Test Date', "dat_link", "xlsx_link"]



marker_size=[
    {'label': 'Marker Size -1' , 'value': 1},
    {'label': 'Marker Size, Defult' , 'value': 2},
    {'label': 'Marker Size +1' , 'value': 3},
    {'label': 'Marker Size +2' , 'value': 4},
    {'label': 'Marker Size +3' , 'value': 5},
    {'label': 'Marker Size +4' , 'value': 6},
    {'label': 'Marker Size +5' , 'value': 7},
    {'label': 'Marker Size +6' , 'value': 8},
    {'label': 'Marker Size +7' , 'value': 9},
    {'label': 'Marker Size +8' , 'value': 10},
    {'label': 'Marker Size +9' , 'value': 11},
    {'label': 'Marker Size +10' , 'value': 12}
    ]

#app=dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP #MINTY
 #                                            ], #meta_tags=[{'name': 'viewport',
#                             'content': 'width=device-width, initial-scale=1.0'}] ##, prevent_initial_callbacks=True)
  #              )# GOOD FOR MOBILE using meta_tags 



layout = dbc.Container([html.Div([
       
    dbc.Row([dbc.Col([html.Div([html.H5(['Selecting Test IDs Manually:'],className='text-left text-primary mt-5')]),]),]),
    dbc.Row([dbc.Col([#html.Div([html.Label(['Name:'],style={'font-weight': 'bold'})]),
        dcc.Dropdown(id='test_name',
                     options= test_names,
                     placeholder='Please select...',
                     multi=False,
                     searchable=True,
                     clearable=False,
                     style={'width':"100%"}, 
                     className='text-justify bg-light text-nowrap mr-4', 
                         # persistence=True,             #remembers dropdown value. Used with persistence_type
                         # persistence_type='memory'     #remembers dropdown value selected until...'memory'/'session'/'local' 
                    ),], 
        ),],className='mr-5'),
#     dbc.Row([
#         dbc.Col(html.Div([html.H6("Please select the averaging time interval:",   
#                         className='text-left text-primary mb-4'),html.Div(id='max_time')]),
#                 width=12)
#     ]), 
        
    dbc.Row([
        dbc.Col([dcc.Markdown(id="max_time",className="text-left text-success mt-5 border-bottom font-weight-bolder"),]),
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
    
    
    ###______ to ckeck outputs___________###   
    
#     dbc.Row([dbc.Col([html.Div([html.H6("INAAA", className="text-center bg-light text-nowrap text-primary border font-weight-bolder mt-5"),
#                                 #dcc.Markdown(id='out_var')],className="text-center"),]),
#                                 html.Div(id='out_var')])])
#             ]),

    
############Force_Chart_scattered
    dbc.Row([dbc.Col([html.Div([dcc.Graph(id='force_chart_2d')])])]),
    
    dbc.Row([dbc.Col([html.Div(html.Label(['Marker Size:'],style={'font-weight': 'bold'})),
                      #'margin-right':10, "text-align": "left"})),
                      dcc.Dropdown(id='marker_var',
                                   options=marker_size,
                                   value=2,
                                     #optionHeight=35,                    #height/space between dropdown options
                                   placeholder='Please select...',
                                   multi=False,
                                   searchable=True,
                                   clearable=False,
                                   style={'width':"70%"}, 
                                     #className='', 
                                     # persistence=True,             #remembers dropdown value. Used with persistence_type
                                     # persistence_type='memory'     #remembers dropdown value selected until...'memory'/'session'/'local' 
                                   )], width={'size':4},),
             dbc.Col([html.Div(html.Label(['X_min:'],
                                         style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                     dcc.Input(id="X_range_min", #id='my_{}'.format(x),     
                                  type='number',
                                  placeholder="insert a range",#"insert {}".format(x),  # A hint to the user of what can be entered in the control
                                  debounce=False,                      # Changes to input are sent to Dash server only on enter or losing focus
                                  min=-50, max=500, step=1,         # Ranges of numeric value. Step refers to increments
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
                          )],width={'size':2}),
             dbc.Col([html.Div(html.Label(['X_max:'],
                                         style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                     dcc.Input(id="X_range_max",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
                     dcc.Input(id="Y_range_min",     
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
                     dcc.Input(id="Y_range_max",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
             
            
    ]),
      
 ########LINE_CHART#####   
    
    dbc.Row([dbc.Col([html.Div([dcc.Graph(id='force_chart_2d_line')])])]),        
    dbc.Row([dbc.Col([html.Div(html.Label(['X_min:'],
                                         style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                     dcc.Input(id="X_range_min_line", #id='my_{}'.format(x),     
                                  type='number',
                                  placeholder="insert a range",#"insert {}".format(x),  # A hint to the user of what can be entered in the control
                                  debounce=False,                      # Changes to input are sent to Dash server only on enter or losing focus
                                  min=-50, max=500, step=1,         # Ranges of numeric value. Step refers to increments
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
                     dcc.Input(id="X_range_max_line",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
                     dcc.Input(id="Y_range_min_line",     
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
                     dcc.Input(id="Y_range_max_line",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
                          )],width={'size':2}),], #align="center")  # Vertical: start, center, end    #at the end of row, aligns different columns
           ),
 
    ###LINE ANIMATION ####
    
    dbc.Row([dbc.Col([html.Div([dcc.Graph(id='force_chart_2d_line_move')])])]),
    
    dbc.Row([#dbc.Col([html.Div(html.Label(['Marker Size:'],style={'font-weight': 'bold'})),#'margin-right':10, "text-align": "left"})),
#                      dcc.Dropdown(id='marker_var_line_move',
#                                   options=marker_size,
#                                   value=2,
#                                   #optionHeight=35,                    #height/space between dropdown options
#                                   placeholder='Please select...',
#                                   multi=False,
#                                   searchable=True,
#                                   clearable=False,
#                                   style={'width':"100%"}, 
#                                  #className='', 
#                                   persistence=True,             #remembers dropdown value. Used with persistence_type
#                                   persistence_type='memory'     #remembers dropdown value selected until...'memory'/'session'/'local' 
#                                            "'offset':1, 'order':1"
#                                  )], width={'size':2}),
        
        
             dbc.Col([html.Div(html.Label(['Time Interval_line:'],style={'font-weight': 'bold'})),#'margin-right':10, "text-align": "left"})),
                      dcc.Dropdown(id='time_inter_line',
                                   options=[
                                     {'label': '1 Sec' , 'value': "anim"},
                                     {'label': '0.5 Sec' , 'value': "anim_05"},  
                                     {'label': '0.1 Sec' , 'value': "anim_01"},
                                     {'label': '0.05 Sec' , 'value': "anim_005"},
                                     {'label': '0.01 Sec' , 'value': "anim_001"}, 
                                     {'label': '0.005 Sec' , 'value': "anim_0005"},
                                     {'label': '0.001 Sec' , 'value': "anim_0001"} 
                                     ],
                                value="anim_01",
                                 #optionHeight=35,                    #height/space between dropdown options
                                 placeholder='Please select...',
                                 multi=False,
                                 searchable=True,
                                 clearable=False,
                                 style={'width':"90%"}, 
                                 #className='', 
                                 # persistence=True,             #remembers dropdown value. Used with persistence_type
                                 # persistence_type='memory'     #remembers dropdown value selected until...'memory'/'session'/'local' 
                                )], width={'size':2,  #4 out of 12 columns,
                                           'offset':2, #'order':1"
                                          }),
              dbc.Col([html.Div(html.Label(['X_min:'],
                                         style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                     dcc.Input(id="X_range_min_line_move", #id='my_{}'.format(x),     
                                  type='number',
                                  placeholder="insert a range",#"insert {}".format(x),  # A hint to the user of what can be entered in the control
                                  debounce=False,                      # Changes to input are sent to Dash server only on enter or losing focus
                                  min=-50, max=500, step=1,         # Ranges of numeric value. Step refers to increments
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
                          )],width={'size':2}),
             dbc.Col([html.Div(html.Label(['X_max:'],
                                         style={'font-weight': 'bold'})),
                     dcc.Input(id="X_range_max_line_move",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
                     dcc.Input(id="Y_range_min_line_move",     
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
                     dcc.Input(id="Y_range_max_line_move",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=500, step=1,         
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
            ],),
#     ],fluid=False) #to delet margin: True    
#     ]),

    ]), ])

                                           
                                           
@app.callback(
    [#Output("out_var", "children"),
     Output("max_time", "children"),],
    [
     Input(component_id='test_name', component_property='value')]
)
    
def update_time(test_name):
    my_df1 = df1

    my_df = pd.read_csv(os.path.join("./datasets",my_df1.loc[test_name]['dat_link'].replace(".dat", ".csv")))
#    
    samp_rate=int(my_df['Sampling Rate'][1])
#     
    
    return["Please select the time frame (Maximum time= {} s):".format(len(my_df)/samp_rate)]
    




@app.callback(
    [#Output("out_var", "children"),
    # Output("max_time", "children"),
     Output(component_id='force_chart_2d', component_property='figure'),
     
# #      Output(component_id='force_chart_2d_move', component_property='figure'), #children'),
     Output(component_id='force_chart_2d_line', component_property='figure'),
     Output(component_id='force_chart_2d_line_move', component_property='figure'),#children')
    ],
    [
     Input(component_id='test_name', component_property='value'),
     Input(component_id='init_time', component_property='value'),
     Input(component_id='end_time', component_property='value'),
     Input(component_id='marker_var', component_property='value'),
     Input(component_id='X_range_min', component_property='value'),
     Input(component_id='X_range_max', component_property='value'),
     Input(component_id='Y_range_min', component_property='value'),
     Input(component_id='Y_range_max', component_property='value'),
# #      Input(component_id='marker_var_move', component_property='value'),
# #      Input(component_id='X_range_min_move', component_property='value'),
# #      Input(component_id='X_range_max_move', component_property='value'),
# #      Input(component_id='Y_range_min_move', component_property='value'),
# #      Input(component_id='Y_range_max_move', component_property='value'),
# #      Input(component_id='time_inter', component_property='value'),
# # #      #Input(component_id='marker_var', component_property='value'),
     Input(component_id='X_range_min_line', component_property='value'),
     Input(component_id='X_range_max_line', component_property='value'),
     Input(component_id='Y_range_min_line', component_property='value'),
     Input(component_id='Y_range_max_line', component_property='value'),
#    ###  Input(component_id='marker_var_line_move', component_property='value'),
     Input(component_id='X_range_min_line_move', component_property='value'),
     Input(component_id='X_range_max_line_move', component_property='value'),
     Input(component_id='Y_range_min_line_move', component_property='value'),
     Input(component_id='Y_range_max_line_move', component_property='value'),
     Input(component_id='time_inter_line', component_property='value')
    ]#,  
)

def update_bar(test_name, init, final,
               marker_value, x_range_min, x_range_max, y_range_min, y_range_max,
# #                marker_value_move, x_range_min_move, x_range_max_move, y_range_min_move, y_range_max_move, time_interval, 
               x_range_min_line, x_range_max_line, y_range_min_line, y_range_max_line, ###marker_var_line_move,
               x_range_min_line_move, x_range_max_line_move, y_range_min_line_move, y_range_max_line_move, 
               time_interval_line
             ):
     
    my_df1 = df1
    
    my_df = pd.read_csv(os.path.join("./datasets",my_df1.loc[test_name]['dat_link'].replace(".dat", ".csv")))
#       #  r'C:\Users\negar\Documents\ARACA Inc\my place\temp\APD800 RAW - Versum W CMP - Slurry DP1142-4\As deposited 60s\23_60s_Versum_300W_XIC1000XY-29_WFT300-N0520_DP1142-4-250_4P_69-67V_ex_as-depo_r01.csv')
    my_df["Time"]=round(my_df["Time"],3)
    bsline_num=int(my_df["Number of Baseline"][0])
    samp_rate=int(my_df['Sampling Rate'][1])
    my_df["Normal Force (lbf)"]=round(((my_df["Fz1"]+my_df["Fz2"]+my_df["Fz3"]+my_df["Fz4"])-my_df["Baseline Fz"][:bsline_num].mean()), 3)
    my_df["Shear Force (lbf)"]=round((my_df["Fy"]-my_df["Baseline Fy"][:bsline_num].mean()), 3)
    my_df["anim"]=my_df["Time"]//1  ##//0.1
    my_df["anim_05"]=my_df["Time"]//0.5 
    my_df["anim_01"]=my_df["Time"]//0.1
    my_df["anim_005"]=my_df["Time"]//0.05 
    my_df["anim_001"]=my_df["Time"]//0.01 
    my_df["anim_0005"]=my_df["Time"]//0.005
    my_df["anim_0001"]=my_df["Time"]//0.001  
    #my_df1["color_1"]=round((my_df["Time"]/0.04)%1, 1)
    my_df["Time Range"]=10-((my_df["Time"]*1000)%10)


    
#     if len(init)==0:
#         init=0
#     if len(final)==0:
#         final=len(my_df)-1
    my_dff=my_df.iloc[(init*samp_rate):(final*samp_rate)]
    
    
    force_chart_2d=px.scatter(
        data_frame=my_dff,
        x="Shear Force (lbf)",
        y="Normal Force (lbf)",
        range_x=[x_range_min, x_range_max], #[-60,150],
        range_y=[y_range_min, y_range_max],
        color="Time")
    force_chart_2d.update_traces(marker_size=marker_value)
    force_chart_2d.update_layout(yaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                          )))
    force_chart_2d.update_layout(xaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                          )))
    force_chart_2d.update_xaxes(tickwidth=2, #ticks="outside",  tickcolor='crimson', ticklen=10
                               #tickangle=45, 
                                tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                             ))
    force_chart_2d.update_yaxes(tickwidth=2,#ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1
                    tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                             ))
    
# # #     force_chart_2d_move=px.scatter(
# # #         data_frame=my_dff,
# # #         x="Shear Force (lbf)",
# # #         y="Normal Force (lbf)",
# # #        # markers=True,
# # #         color="Time",
# # #         animation_frame=time_interval,
# # #         range_x=[x_range_min_move, x_range_max_move],
# # #         range_y=[y_range_min_move, y_range_max_move])
    
# # #     force_chart_2d_move.update_traces(marker_size=marker_value_move)#, selector=dict(type='scatter'))
# # #     force_chart_2d_move.update_layout(yaxis=dict(titlefont=dict(size=22)))
# # #     force_chart_2d_move.update_layout(xaxis=dict(titlefont=dict(size=22)))
# # #     force_chart_2d_move.update_xaxes(tickwidth=2, tickfont=dict(size=16))
# # #     force_chart_2d_move.update_yaxes(tickwidth=2, tickfont=dict(size=16))
# # #     force_chart_2d_move.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
# # #     force_chart_2d_move.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500

      
    force_chart_2d_line=px.line(
        data_frame=my_dff,
        x="Shear Force (lbf)",
        y="Normal Force (lbf)",
        markers=False,
       # color="Time",
        range_x=[x_range_min_line, x_range_max_line], #[-60,150],
        range_y=[y_range_min_line, y_range_max_line],
    )
    force_chart_2d_line.update_layout(yaxis=dict(titlefont=dict(size=22)))
    force_chart_2d_line.update_layout(xaxis=dict(titlefont=dict(size=22)))
    force_chart_2d_line.update_xaxes(tickwidth=2, tickfont=dict(size=16))
    force_chart_2d_line.update_yaxes(tickwidth=2, tickfont=dict(size=16)),
    
    
    
    
    
    force_chart_2d_line_move=px.line(
        data_frame=my_dff,
        x="Shear Force (lbf)",
        y="Normal Force (lbf)",
        markers=True,
        animation_frame=time_interval_line,
        range_x=[x_range_min_line_move, x_range_max_line_move], #[-60,150],
        range_y=[y_range_min_line_move, y_range_max_line_move],
#        # color="Time Range",
#         #size="Time Range"
    )
###    force_chart_2d_line_move.update_traces(marker_size=marker_var_line_move)
    force_chart_2d_line_move.update_layout(yaxis=dict(titlefont=dict(size=22)))
    force_chart_2d_line_move.update_layout(xaxis=dict(titlefont=dict(size=22)))
    force_chart_2d_line_move.update_xaxes(tickwidth=2, tickfont=dict(size=16))
    force_chart_2d_line_move.update_yaxes(tickwidth=2, tickfont=dict(size=16))
    force_chart_2d_line_move.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000
    force_chart_2d_line_move.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 500
    
    
#     return[len(my_dff["Normal Force (lbf)"])]
    return [force_chart_2d, force_chart_2d_line, force_chart_2d_line_move]