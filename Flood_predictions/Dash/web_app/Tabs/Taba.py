# Setting up page/layout of tab1

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from Base import app
# enter info for tab1
layout_taba = html.Div([

    dcc.Markdown('''
    &nbsp;
    
    ## Team name: The Rightside

    This project was carried out by Data Engineers at Kubrick Group between March 28th - April 12th, 2019.
    
    ## Team members:
    * Amrick Bharj
    * Ben Mackley
    * Charlie Perera
    * Evelyn Byer
    * Jacob Morl
    * Max Coussens
    * Megan Duffy
    * Nil Bozkurt

    ***
    '''.replace('  ', ''), className='container',
        containerProps={'style': {'maxWidth': '1000px'}}),

    dcc.Markdown('''
    ## Aim
    The aim of this project was to predict the risk of flooding in the UK using open data sources and machine learning
    techniques. The output is an interactive web app created using plotly Dash.
    
    ***
    
    ## Table of Contents

    In this report you can switch between tabs:
    - Background: What features affect floods? Explore the features we used to build our model.
    - Model Evaluation: How well does the model work?
    - User interface: Explore the probability of flood on our interactive map, and what flood risk exists in the next 
    five years in your area?
    - Documentation: List of data sources and methodology summary.
    '''.replace('  ', ''), className='container',
        containerProps={'style': {'maxWidth': '1000px'}})
])
