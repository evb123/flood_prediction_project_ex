# Script created by Ev Byer on 12-04-2019
#----------------------------------------------------------------------------------------------------------------------

import dash_core_components as dcc
import dash_html_components as html

from Base import app

import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np

import pandas as pd
import pyodbc
import sqlite3

# For importing files in the future----------------------------------------------------------------------------------------
# image_filename = './Hist_floods.png'  # replace with your own image
# encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode('utf-8')
# html.Img(src='data:image/png;base64,{}'.format(encoded_image))


# # Begin Scatter Matrix preprocessing----------------------------------------------------------------------------------
# cnxn = pyodbc.connect(UID='rightside',
#                       PWD='c6Rn0H',
#                       driver='{SQL Server}',
#                       server='192.168.101.109',
#                       database='trs')
#
# sql = "Select * from model_out.scatter_map"
# data = pd.read_sql(sql, cnxn)
# data = data.rename({'IsFlood': 'IsFlood', 'air_pressure_min_mnth': 'Min. Monthly Air Press.', 'avg_elevation':'Avg. Elevation', 'numf_pre_2010':'# Floods b.2010'}, axis='columns')
# data['IsFlood'] = data['IsFlood'].replace({0: 'No Flood', 1: 'Flood'})
#
# conn = sqlite3.connect('rightside2.db')
# data.to_sql('scatter_matrix', con=conn, if_exists='replace', index=False)


cnx = sqlite3.connect('rightside2.db')
dataframe = pd.read_sql_query("SELECT * FROM scatter_matrix", cnx)

# keep this below, edit above, must import dataframe as 'dataframe'
fig = ff.create_scatterplotmatrix(dataframe, index='IsFlood', diag='histogram',
                                  colormap=['#b08ca4', '#70818b'],
                                  colormap_type='seq',
                                  height=800, width=800,
                                  size=5, marker=dict(symbol='o', showscale=False, opacity=1),
                                  text=dataframe['IsFlood'],# fill=True,
                                  hovertext=dataframe['IsFlood'],
                                  hoverinfo=dataframe['IsFlood']
                                  )
# Confusion Matrix Setup-----------------------------------------------------------------------------------------------


# cnxn = pyodbc.connect(UID='rightside',
#                       PWD='c6Rn0H',
#                       driver='{SQL Server}',
#                       server='192.168.101.109',
#                       database='trs')
#
# sql = "Select * from [model_out].[flood_corr]"
# data = pd.read_sql(sql, cnxn)
#
# conn = sqlite3.connect('rightside2.db')
# data.to_sql('corr_matrix', con=conn, if_exists='replace', index=False)  # to put in a sql lite database

cnx = sqlite3.connect('rightside2.db')
df_corr = pd.read_sql_query("SELECT * FROM corr_matrix", cnx)

x_corr = df_corr['Name']
y_corr = df_corr['Name']
z_corr = df_corr[['rain_avg_mnth', 'imp', 'air_pressure_min_mnth', 'lu15_2xx',
          'rain_max_mnth', 'total_river_length', 'avg_elevation',
          'rain_max_five_day_sum', 'wind_min_mnth', 'air_pressure_max_mnth',
          'forest', 'area_overlapped_m2', 'air_pressure_avg_mnth',
          'numf_pre_2010', 'pct_area_overlapped', 'lu15_230', 'lu15_1xx']]
z_corr = z_corr.values.tolist()

x_con = ['Positive', 'Negative']
y_con = ['Positive', 'Negative']
z_con = list([[203, 120], [31, 956]])


## Setup for gauge chart

base_chart = {
    "values": [40, 10, 10, 10, 10, 10, 10],
    "labels": [" ", "0", ".20", ".40", ".60", ".80", "1"],
    "domain": {"x": [0, 1]},
    "marker": {
        "colors": [
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)'
        ],
        "line": {
            "width": 2
        }
    },
    "name": "Gauge",
    "hole": .4,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 108,
    "showlegend": False,
    "hoverinfo": "none",
    "textinfo": "label",
    "textposition": "outside"
}

meter_chart = {
    "values": [50, 10, 10, 10, 10, 10],
    "labels": [" ", "Terrible", "Bad", "OK", "Good", "Excellent"],  # first label is little title
    "marker": {
        'colors': [
            'rgb(255, 255, 255)',
            'rgb(232,226,202)',
            'rgb(226,210,172)',
            'rgb(223,189,139)',
            'rgb(223,162,103)',
            'rgb(226,126,64)'
        ]
    },
    "domain": {"x": [0, 1]},  # 0.48
    "name": "Gauge",
    "hole": .3,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 90,
    "showlegend": False,
    "textinfo": "label",
    "textposition": "inside",
    "hoverinfo": "none"
}

# Gauge 1
layout1 = {
    'title': 'Precision',  # Rename title obviously
    'xaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'shapes': [
        # controls for arrow
        {
            'type': 'path',
            'path': 'M 0.495 0.5 L 0.60 0.73776 L 0.505 0.5 Z',  # .5 is center, must change depending on actual value
            'fillcolor': 'rgb(42, 45, 51)', #rgba(44, 160, 101, 0.5)
            'line': {
                'width': 0.5
            },
            'xref': 'paper',
            'yref': 'paper'
        }
    ],
    'annotations': [
        {
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 0.45,
            'text': '0.63',
            'showarrow': False  # should be False
        }
    ]
}

# Gauge 2
layout2 = {
    'title': 'Recall',  # Rename title obviously
    'xaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'shapes': [
        # controls for arrow
        {
            'type': 'path',
            'path': 'M 0.495 0.5 L 0.68 0.59 L 0.505 0.5 Z',  # .5 is center, must change depending on actual value
            'fillcolor': 'rgb(42, 45, 51)',
            'line': {
                'width': 0.5
            },
            'xref': 'paper',  # paper
            'yref': 'paper'
        }
    ],
    'annotations': [
        {
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 0.45,
            'text': '0.87',
            'showarrow': False  # should be False
        }
    ]
}

# Gauge 3
layout3 = {
    'title': 'F1 Score',  # Rename title obviously
    'xaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'shapes': [
        # controls for arrow
        {
            'type': 'path',
            'path': 'M 0.495 0.5 L 0.61 0.69 L 0.505 0.5 Z',  # .5 is center, must change depending on actual value
            'fillcolor': 'rgb(42, 45, 51)',
            'line': {
                'width': 0.5
            },
            'xref': 'paper',
            'yref': 'paper'
        }
    ],
    'annotations': [
        {
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 0.45,
            'text': '0.73',
            'showarrow': False  # should be False
        }
    ]
}

# Gauge 4
layout4 = {
    'title': 'Balance Accuracy',  # Rename title obviously
    'xaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'shapes': [
        # controls for arrow
        {
            'type': 'path',
            'path': 'M 0.495 0.5 L 0.68 0.59 L 0.505 0.5 Z',  # .5 is center, must change depending on actual value
            'fillcolor': 'rgb(42, 45, 51)',
            'line': {
                'width': 0.5
            },
            'xref': 'paper',
            'yref': 'paper'
        }
    ],
    'annotations': [
        {
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.5,
            'y': 0.45,
            'text': '0.88',
            'showarrow': False  # should be False
        }
    ]
}

# we don't want the boundary now
base_chart['marker']['line']['width'] = 0
fig_gauge1 = {"data": [base_chart, meter_chart], "layout": layout1}
fig_gauge2 = {"data": [base_chart, meter_chart], "layout": layout2}
fig_gauge3 = {"data": [base_chart, meter_chart], "layout": layout3}
fig_gauge4 = {"data": [base_chart, meter_chart], "layout": layout4}

# Tab Layout
layout_tabz = html.Div([
    # Title of Tab2 Page
    # html.H3('Tab content 2'),
    html.Div([
        dcc.Markdown('''

        &nbsp;
        ***
        &nbsp;
           
        ## Features 
        Features have been categorised into two types; static and dynamic. Static features are features which are stable 
        in the short term (e.g. land types, elevation,river locations etc). Dynamic features are features which are 
        volatile in the short term such as rainfall, air pressure and windspeed.
        
        Both static features and dynamic features have been assigned to a 5km x 5km grid system as a means of 
        simplifying the model. The dynamic features have also been aggregated to a 5-yearly level.
        
        From a total 64 features, 17 have been selected to go into the final model. Selections were made using 
        forward subset selection, as well as some manual selection based on model outputs of feature importance. 

        &nbsp;
           ***
           &nbsp;
        
           ## Feature correlation
           An overview of the relationships between three features, chosen by top variable importance in the model can 
           be seen below in a scatter matrix. 
           
           A coefficient heat map has also been created for all 17 features used.
           '''.replace('  ', ''), className='container',
                     containerProps={'style': {'maxWidth': '1000px'}})
    ]),
    html.Div([
        dcc.Graph(
            id='my-graph',
            figure=fig,
        )], style={'marginLeft': 600, 'marginRight': 600, 'marginBottom': 30}
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id='correlation-heatmap',
                figure={
                    'data': [
                        go.Heatmap(
                            x=x_corr,
                            y=y_corr,
                            z=z_corr,
                            # The 'colorscale' property is a colorscale and may be
                            #     specified as:
                            #       - A list of 2-element lists where the first element is the
                            #         normalized color level value (starting at 0 and ending at 1),
                            #         and the second item is a valid color string.
                            #         (e.g. [[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']])
                            #       - One of the following named colorscales:
                            #             ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                            #             'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                            #             'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']
                            colorscale='Bluered',
                            colorbar={"title": "Correlation Coef."},
                            showscale=True

                        )
                    ],
                    'layout': go.Layout(
                        title='Feature Correlation Heatmap',
                        hovermode='closest',
                        plot_bgcolor='rgba(240,240,240,0.95)',
                        autosize=True

                    )
                },

            )
        ],
            style={'width': '100%', 'align': 'center', 'height': '100%', 'display': 'inline-block', 'marginLeft': 40}
            # , 'display': 'inline-block'
        ),

        html.Div([
            dcc.Markdown('''
                      ***
                      &nbsp;
                      ### Features

                      ##### Summary of findings
                      Correlation coefficients were calculated for all 17 features used in the model to explore variable
                      correlation. Red corresponds to a strong positive correlation, purple corresponds to weak correlation,
                      and blue corresponds to a negative correlation.

                      ##### Observed patterns in model features
                      - Max rainfall per month was strongly correlated with average elevation (0.72).
                      - Variables aggregated from a single variable are strongly correlated (ie rain_max variables).
                      - 'Imp' (covering of ground by an impermeable material) and 'lu15_230' (% of the grid square 
                      covered by urban fabric) are 
                      highly positively correlated (0.99).
                      - 'Imp' (covering of ground by an impermeable material) and 'lu15_1xx' (The % of the grid square 
                      covered by pastures) are 
                      negatively correlated (-0.63).
                    
                      '''.replace('  ', ''))], style={'marginLeft': 70})
        # inline block transfers gauge graph to below above graph
    ], style={'columnCount': 2, 'align-items': 'center', 'justify-items': 'center'}
    ),

    html.Div([
        dcc.Markdown('''
          ***
          ## The Model

          The aim of the model is to predict whether over a 5 year period a flood will occur in a given grid square.
          The model is trained based on records of where previous floods have occurred and predicted probabilities are
          obtained to give a quantitative value of flood risk. 
          
          A random forest classifier was selected based on high-level testing and also because it is a flexible but powerful
          algorithm. Since floods are rare events, stratified sampling was used to split the data into test and training
          sets, and the training set was upsampled to increase the proportion of datapoints corresponding to floods.
          This drastically improved the ability of the model to identify flood events.


          #### Model Accuracy
          
          As the intended use of the model is for use by an insurance company, the model has been built to minimise the 
          number of flood outcomes which are not predicted - it is more damaging to  underestimate the flood risk. 
          To do this the focus of model accuracy was on maximising recall score, although precision score and balanced 
          accuracy were also taken into consideration.
          
          Outputs from the test and training set have been plotted below. As you can see:
          * from the recall score, 86% of floods in the test set were correctly predicted
          * from the precision score, 63% of predicted floods correspond to floods in the test set
          
          '''.replace('  ', ''), className='container',
                     containerProps={'style': {'maxWidth': '1000px'}})

    ]),

    html.Div([
        html.Div([
            dcc.Graph(
                id='gauge-chart1',
                figure=fig_gauge2
            ),
            dcc.Graph(
                id='gauge-chart2',
                figure=fig_gauge4
            )
        ], style={'width': '100%', 'align': 'center', 'vertical-align': 'middle', 'overflow': 'hidden',
                  'height': '100%'}
        ),
        html.Div([
            dcc.Graph(
                id='gauge-chart3',
                figure=fig_gauge1
            ),
            dcc.Graph(
                id='gauge-chart4',
                figure=fig_gauge3
            )
        ], style={'width': '100%', 'align': 'center', 'vertical-align': 'middle', 'overflow': 'hidden',
                  'height': '100%'}
        )

    ], style={'columnCount': 2, 'width': '70%', 'marginLeft': 300, 'marginRight': 300,
              'align': 'center'}
    ),

    html.Div([
        html.Div([
            dcc.Graph(
                id='confusion-matrix',
                figure={
                    'data': [go.Heatmap(
                        x=x_con,
                        y=y_con,
                        z=z_con,
                        colorscale='Cividis',  # 'Blues',

                        #             One of the following named colorscales:
                        #             ['Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 'RdBu',
                        #             'Reds', 'Blues', 'Picnic', 'Rainbow', 'Portland', 'Jet',
                        #             'Hot', 'Blackbody', 'Earth', 'Electric', 'Viridis', 'Cividis']

                        showscale=False)]
                    ,
                    'layout': go.Layout(
                        title='Confusion Matrix',
                        xaxis={'fixedrange': True,
                               'title': 'Predicted'
                               },
                        yaxis={'fixedrange': True,
                               'autorange': 'reversed',
                               'title': 'True'},
                        autosize=True,
                        annotations=[{'x': 'Positive', 'y': 'Positive', 'showarrow': False, 'text': z_con[0][0],
                                      'xref': 'x',
                                      'yref': 'y', 'font': {'size': 20, 'color': '#ffffff'}},
                                     {'x': 'Positive', 'y': 'Negative',
                                      'showarrow': False, 'text': z_con[0][1], 'xref': 'x',
                                      'yref': 'y', 'font': {'size': 20, 'color': '#ffffff'}},
                                     {'x': 'Negative', 'y': 'Positive',
                                      'showarrow': False, 'text': z_con[1][0], 'xref': 'x',
                                      'yref': 'y', 'font': {'size': 20, 'color': '#ffffff'}},
                                     {'x': 'Negative', 'y': 'Negative',
                                      'showarrow': False, 'text': z_con[1][1], 'xref': 'x',
                                      'yref': 'y', 'font': {'size': 20, 'color': '#3f454f'}}]
                    )
                }
            )
        ], style={'width': '100%', 'text-align': 'center', 'display': 'inline-block', 'marginLeft': 20}),

        html.Div([
            dcc.Markdown('''
         ***
            &nbsp;
         ### False Negatives vs. False Positives
         &nbsp;

         As mentioned above, the aim of the model was to minimize the number of false negative predictions - where 
         probability of flood risk has been underpredicted. 
         
         Having a low number of false positives was the next aim, this is where it predicted a higher probability 
         of a flood when it should have been low. 
         
         The confusion matrix on the left displays how the model performed against the test set.
         '''.replace('  ', ''), className='container'
                         # , containerProps={'style': {'maxWidth': '650px'}}
                         )
        ]),
    ], style={'columnCount': 2}),
    html.Div([ # to put images
        ])
])

if __name__ == '__main__':
    print("Great job :)")
    app.layout = layout_tabz
    app.run_server(debug=True)
