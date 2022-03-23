# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:28:07 2022

@author: negar
"""
#import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
#import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import os
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df_t= pd.read_excel(DATA_PATH.joinpath("last_Polishing_Conditions_TEMP.xlsx"))
df_t.set_index('Test ID_test', inplace=True, drop=False)

test_names=[{'label': name , 'value': name} for name in df_t["Test ID_test"].unique()]




df1_t=df_t[['Test ID_test', 'Test ID_Date','Related documents_.dat', 'Related documents_.xlsx']]
df1_t.columns=['Test ID', 'Test Date', "dat_link", "xlsx_link"]

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

corr_trans=[
             {'label': 'Time (s)' , 'value': 'Time'},
             {'label': 'Shear Force (lbf)' , 'value': 'Shear Force'},
             {'label': 'Normal Force (lbf)' , 'value': 'Normal Force'},
             {'label': 'COF' , 'value': 'COF'},
             {'label': 'Pad Temperature (C)', 'value': 'Temperature'},
             {'label': '1/T (1/K)', 'value': '1/T (1/K)'},
             {'label': 'Pressure (Pa)' , 'value':'Pressure'},
             {'label': 'Velocity (m/s)', 'value': 'Velocity'},
             #{'label': "Pseudo-Sommerfeld number (m/(Pa.s))", 'value':""},
             {'label': 'P.V (Pa.m/s)', 'value': 'pv'},
             {'label': 'V/P (m/(Pa.s))', 'value': 'v/p'},
             {'label': "Power Density (m.Pa/s)", 'value':"Power Density"}
             ]


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
   
    ###______ to ckeck outputs___________###   
   
#   dbc.Row([dbc.Col([html.Div([html.H6("INAAA", className="text-center bg-light text-nowrap text-primary border font-weight-bolder mt-5"),
 #                              html.Div(id='out_var')])])
#           ]),

    
    dbc.Row([dbc.Col([html.Div([html.Label(['Select x:'],style={'font-weight': 'bold'})]),# "text-align": "left"
                      dcc.Dropdown(id='variables-1-x',
                                   options=corr_trans,
                                   value='Time (s)',
                                   multi=False,
                                   style={'width':"100%"},  
                                   clearable=False),]), #width={'size':6  #4 out of 12 columns,
                                           #"'offset':1, 'order':1"
                                      #    }),
             dbc.Col([html.Div([html.Label(['Select y:'],style={'font-weight': 'bold'})]),
                      dcc.Dropdown(id='variables-1',
                                   options=corr_trans,
                                   value='Shear Force (lbf)',
                                   multi=True,
                                   style={'width':"100%"},  
                                   clearable=False),]), #width={'size':6  #4 out of 12 columns,
                                           #"'offset':1, 'order':1"
                                        #  }),
            ]),
    dbc.Row(dbc.Col([html.Div([dcc.Graph(id='var-container-1')])])),
    dbc.Row([dbc.Col([html.Div(html.Label(['X_min:'],
                                         style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                      dcc.Input(id="X_range_min_1", #id='my_{}'.format(x),     
                                  type='number',
                                  placeholder="insert a range",#"insert {}".format(x),  # A hint to the user of what can be entered in the control
                                  debounce=False,                      # Changes to input are sent to Dash server only on enter or losing focus
                                  min=-50, max=150, step=1,         # Ranges of numeric value. Step refers to increments
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
                     dcc.Input(id="X_range_max_1",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=150, step=1,         
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
                     dcc.Input(id="Y_range_min_1",     
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=150, step=1,         
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
                     dcc.Input(id="Y_range_max_1",      
                                  type='number',
                                  placeholder="insert a range",
                                  debounce=False,                      
                                  min=-50, max=150, step=1,         
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
####      Second Graph #####
###-----------------------------------------------------------------------------------------------------------------------###    
    
#     dbc.Row([
#         dbc.Col(html.H1("Graph 2",
#                         className='text-left text-secondary mb-4 mt-5'),
#                 width=12)
#     ]),
    
    dbc.Row([dbc.Col([html.Div([html.Label(['Select x:'],style={'font-weight': 'bold'})]),# "text-align": "left"
                          dcc.Dropdown(id='variables-2-x',
                                       options=corr_trans,
                                       value='Time (s)',
                                       multi=False,
                                       style={'width':"100%"},  
                                       clearable=False),]), #width={'size':6  #4 out of 12 columns,
                                               #"'offset':1, 'order':1"
                                          #    }),
                 dbc.Col([html.Div([html.Label(['Select y:'],style={'font-weight': 'bold'})]),
                          dcc.Dropdown(id='variables-2',
                                       options=corr_trans,
                                       value='Shear Force (lbf)',
                                       multi=True,
                                       style={'width':"100%"},  
                                       clearable=False),]), #width={'size':6  #4 out of 12 columns,
                                               #"'offset':1, 'order':1"
                                            #  }),
                ]),
        dbc.Row(dbc.Col([html.Div([dcc.Graph(id='var-container-2')])])),
        dbc.Row([dbc.Col([html.Div(html.Label(['X_min:'],
                                             style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                          dcc.Input(id="X_range_min_2", #id='my_{}'.format(x),     
                                      type='number',
                                      placeholder="insert a range",#"insert {}".format(x),  # A hint to the user of what can be entered in the control
                                      debounce=False,                      # Changes to input are sent to Dash server only on enter or losing focus
                                      min=-50, max=150, step=1,         # Ranges of numeric value. Step refers to increments
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
                         dcc.Input(id="X_range_max_2",      
                                      type='number',
                                      placeholder="insert a range",
                                      debounce=False,                      
                                      min=-50, max=150, step=1,         
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
                         dcc.Input(id="Y_range_min_2",     
                                      type='number',
                                      placeholder="insert a range",
                                      debounce=False,                      
                                      min=-50, max=150, step=1,         
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
                         dcc.Input(id="Y_range_max_2",      
                                      type='number',
                                      placeholder="insert a range",
                                      debounce=False,                      
                                      min=-50, max=150, step=1,         
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

####      Third Graph #####
###-----------------------------------------------------------------------------------------------------------------------###    
#     dbc.Row([
#         dbc.Col(html.H1("Scatter Plot",
#                         className='text-left text-secondary mb-4 mt-5'),
#                 width=12)
#     ]),
    dbc.Row([dbc.Col([html.Div([html.Label(['Select x:'],style={'font-weight': 'bold'})]),# "text-align": "left"
                          dcc.Dropdown(id='variables-3-x',
                                       options=corr_trans,
                                       value='Time (s)',
                                       multi=False,
                                       style={'width':"100%"},  
                                       clearable=False),]), #width={'size':6  #4 out of 12 columns,
                                               #"'offset':1, 'order':1"
                                          #    }),
                 dbc.Col([html.Div([html.Label(['Select y:'],style={'font-weight': 'bold'})]),
                          dcc.Dropdown(id='variables-3',
                                       options=corr_trans,
                                       value='Shear Force (lbf)',
                                       multi=True,
                                       style={'width':"100%"},  
                                       clearable=False),]), #width={'size':6  #4 out of 12 columns,
                                               #"'offset':1, 'order':1"
                                            #  }),
                ]),
        dbc.Row(dbc.Col([html.Div([dcc.Graph(id='var-container-3')])])),
        dbc.Row([dbc.Col([html.Div(html.Label(['Marker Size:'],style={'font-weight': 'bold'})),#'margin-right':10, "text-align": "left"})),
                          dcc.Dropdown(id='marker_var',
                                       options=[
                                         {'label': 'Marker Size -1' , 'value': 1},
                                         {'label': 'Marker Size, Defult' , 'value': 2},
                                         {'label': 'Marker Size +1' , 'value': 3},
                                         {'label': 'Marker Size +2' , 'value': 4},
                                         {'label': 'Marker Size +3' , 'value': 5},
                                         {'label': 'Marker Size +4' , 'value': 6},
                                         {'label': 'Marker Size +5' , 'value': 7},
                                         {'label': 'Marker Size +6' , 'value': 8},
                                         {'label': 'Marker Size +7' , 'value': 9}
                                         ],
                                    value=2,
                                     #optionHeight=35,                    #height/space between dropdown options
                                     placeholder='Please select...',
                                     multi=False,
                                     searchable=True,
                                     clearable=False,
                                     style={'width':"100%"}, 
                                     #className='', 
                                     # persistence=True,             #remembers dropdown value. Used with persistence_type
                                     # persistence_type='memory'     #remembers dropdown value selected until...'memory'/'session'/'local' 
                                               #"'offset':1, 'order':1"
                                      )], width={'size':2}),
                 
                 dbc.Col([html.Div(html.Label(['X_min:'],
                                             style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                          dcc.Input(id="X_range_min_3", #id='my_{}'.format(x),     
                                      type='number',
                                      placeholder="insert a range",#"insert {}".format(x),  # A hint to the user of what can be entered in the control
                                      debounce=False,                      # Changes to input are sent to Dash server only on enter or losing focus
                                      min=-50, max=150, step=1,         # Ranges of numeric value. Step refers to increments
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
                              )],width={'size':2, "offset":2}),
                 dbc.Col([html.Div(html.Label(['X_max:'],
                                             style={'font-weight': 'bold'})),# 'margin-right':10, 'display':'inline-block'})),
                         dcc.Input(id="X_range_max_3",      
                                      type='number',
                                      placeholder="insert a range",
                                      debounce=False,                      
                                      min=-50, max=150, step=1,         
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
                                      min=-50, max=150, step=1,         
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
                                      min=-50, max=150, step=1,         
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
        ]),
    ])
@app.callback(
    [#Output("out_var", "children"),
     Output(component_id='var-container-1', component_property="figure"),
    ],
    
    [
     Input(component_id='test_name', component_property='value'),
     Input(component_id='variables-1-x', component_property='value'),
     Input(component_id='variables-1', component_property='value'),
     Input(component_id='X_range_min_1', component_property='value'),
     Input(component_id='X_range_max_1', component_property='value'),
     Input(component_id='Y_range_min_1', component_property='value'),
     Input(component_id='Y_range_max_1', component_property='value'),
    ]
)
   

def update_bar(test_name, selected_val_1_x, selected_val_1, X_range_min_1, X_range_max_1, Y_range_min_1, Y_range_max_1,
              ):
    my_df_t = df1_t
    
    my_df = pd.read_csv(os.path.join(r"C:\Users\negar\Documents\ARACA Inc\Herokou_3p\datasets",my_df_t.loc[test_name]['dat_link'].replace(".dat", ".csv")))
    

        
    line_chart_1=px.line(
       data_frame=my_df,
       x=selected_val_1_x,
       y=selected_val_1,
       range_x=[X_range_min_1, X_range_max_1], #[-60,150],
       range_y=[Y_range_min_1, Y_range_max_1]
     )
    
    if len(selected_val_1)==1:
        line_chart_1.update_layout(yaxis_title=str(selected_val_1).split("'")[1])
    line_chart_1.update_layout(yaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                         )))
    line_chart_1.update_layout(xaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                         )))
    line_chart_1.update_xaxes(tickwidth=2, #ticks="outside",  tickcolor='crimson', ticklen=10
                              #tickangle=45, 
                               tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                            ))
    line_chart_1.update_yaxes(tickwidth=2,#ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1
                   tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                            ))
    return [line_chart_1]

@app.callback(
    [
     Output(component_id='var-container-2', component_property='figure'),
    ],
    
    [
     Input(component_id='test_name', component_property='value'),
     Input(component_id='variables-2-x', component_property='value'),
     Input(component_id='variables-2', component_property='value'),
     Input(component_id='X_range_min_2', component_property='value'),
     Input(component_id='X_range_max_2', component_property='value'),
     Input(component_id='Y_range_min_2', component_property='value'),
     Input(component_id='Y_range_max_2', component_property='value'),
    ]
)
   

def update_bar(test_name, #selected_val_1_x, selected_val_1, X_range_min_1, X_range_max_1, Y_range_min_1, Y_range_max_1,
               selected_val_2_x, selected_val_2, X_range_min_2, X_range_max_2, Y_range_min_2, Y_range_max_2,
               #selected_val_3_x, selected_val_3, marker_value, X_range_min_3, X_range_max_3, Y_range_min_3, Y_range_max_3
              ):
    my_df_t = df1_t
    
    my_df = pd.read_csv(os.path.join(r"C:\Users\negar\Documents\ARACA Inc\Herokou_3p\datasets",my_df_t.loc[test_name]['dat_link'].replace(".dat", ".csv")))
    

          
   
    line_chart_2=px.line(
       data_frame=my_df,
       x=selected_val_2_x,
       y=selected_val_2,
       range_x=[X_range_min_2, X_range_max_2], #[-60,150],
       range_y=[Y_range_min_2, Y_range_max_2]
     )
    

    if len(selected_val_2)==1:
        line_chart_2.update_layout(yaxis_title=str(selected_val_2).split("'")[1])
    line_chart_2.update_layout(yaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                         )))
    line_chart_2.update_layout(xaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                         )))
    line_chart_2.update_xaxes(tickwidth=2, #ticks="outside",  tickcolor='crimson', ticklen=10
                              #tickangle=45, 
                               tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                            ))
    line_chart_2.update_yaxes(tickwidth=2,#ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1
                   tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                            ))
    return [line_chart_2]
    
@app.callback(
    [
      Output(component_id='var-container-3', component_property='figure'),
    ],
    
    [
     Input(component_id='test_name', component_property='value'),
     Input(component_id='variables-3-x', component_property='value'),
     Input(component_id='variables-3', component_property='value'),
     Input(component_id='marker_var', component_property='value'),  
     Input(component_id='X_range_min_3', component_property='value'),
     Input(component_id='X_range_max_3', component_property='value'),
     Input(component_id='Y_range_min_3', component_property='value'),
     Input(component_id='Y_range_max_3', component_property='value'),
    ]
)
   

def update_bar(test_name, #selected_val_1_x, selected_val_1, X_range_min_1, X_range_max_1, Y_range_min_1, Y_range_max_1,
#                selected_val_2_x, selected_val_2, X_range_min_2, X_range_max_2, Y_range_min_2, Y_range_max_2,
               selected_val_3_x, selected_val_3, marker_value, 
               X_range_min_3, X_range_max_3, Y_range_min_3, Y_range_max_3
              ):
    my_df_t = df1_t
    
    my_df = pd.read_csv(os.path.join(r"C:\Users\negar\Documents\ARACA Inc\Herokou_3p\datasets",my_df_t.loc[test_name]['dat_link'].replace(".dat", ".csv")))
    

    scatter_chart=px.scatter(
       data_frame=my_df,
       x=selected_val_3_x,
       y=selected_val_3,
       range_x=[X_range_min_3, X_range_max_3], #[-60,150],
       range_y=[Y_range_min_3, Y_range_max_3],
     )
    if len(selected_val_3)==1:
        scatter_chart.update_layout(yaxis_title=str(selected_val_3).split("'")[1])
    scatter_chart.update_traces(marker_size=marker_value)
    scatter_chart.update_layout(yaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                         )))
    scatter_chart.update_layout(xaxis=dict(titlefont=dict(size=22 #, family='Courier', color='crimson'
                                                         )))
    scatter_chart.update_xaxes(tickwidth=2, #ticks="outside",  tickcolor='crimson', ticklen=10
                              #tickangle=45, 
                               tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                            ))
    scatter_chart.update_yaxes(tickwidth=2,#ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1
                   tickfont=dict(size=16,#family='Rockwell', color='crimson'
                                            ))
    return [scatter_chart]