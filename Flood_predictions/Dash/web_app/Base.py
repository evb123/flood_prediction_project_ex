# Script created by Ev Byer on 12-04-2019
#----------------------------------------------------------------------------------------------------------------------

# Hacking Geopandas

import os
import dash

# os.environ['GDAL_DATA'] = r'C:\Users\EvelynByer\Anaconda3\envs\choro37\Library\share\gdal'

# Setting up base
import dash_core_components as dcc


# to specify style from outside template
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# creating app instance of class dash with different stylesheets
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app = dash.Dash(external_stylesheets=["https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap-grid.min.css"])
# app = dash.Dash(external_stylesheets=["https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/cosmo/bootstrap.min.css"]) #cosmo
# app = dash.Dash(external_stylesheets=["https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/minty/bootstrap.min.css"])
# app = dash.Dash(external_stylesheets=["https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/spacelab/bootstrap.min.css"])
app = dash.Dash(external_stylesheets=["https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/yeti/bootstrap.min.css"])


server = app.server
app.config.suppress_callback_exceptions = True

# Styling

tabs_styles = {
    'height': '44px',
    'color': 'black',
    'text-align': 'center',
    'vertical-align': 'middle'
}

tab_style = {
    # 'borderBottom': '1px solid #d6d6d6',
    'padding': '5px',
    #'fontWeight': 'bold',
    'text-align': 'center',
    'vertical-align': 'middle'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    # 'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'white',
    'color': 'black', #font color
    'padding': '5px', #spacing around text and border
    'fontWeight': 'bold'
}
