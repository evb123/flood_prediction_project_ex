# Script created by Ev Byer on 12-04-2019
#----------------------------------------------------------------------------------------------------------------------

from dash.dependencies import Input, Output

from Tabs import *
from Base import *
#from PlottingRiskShapes import *
from updated_pycharm_project.updated_pycharm_project.FeaturesGraphs.Tab1_FINAL import *
from updated_pycharm_project import *




# defining app layout
app.layout = html.Div([
    # html.Div(style={'background-color: #2AA9E0'}),

    html.H1('Predicting the Probability of Future Flooding in England and Wales',
            style={'text-align': 'center', 'vertical-align': 'middle', 'color': 'black', 'background-color': 'white'
            }
    ),
    html.H2('Using Machine Learning',
            style={'text-align': 'center', 'vertical-align': 'middle', 'color': 'black', 'background-color': 'white'
            }
    ),
    # creating and id-ing Tabs, default tab to tab1
    dcc.Tabs(id="tabs-example", value='tab-a-example', children=[
        dcc.Tab(label='Introduction', value='tab-a-example', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Background', value='tab-1-example', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Feature & Model Evaluation', value='tab-2-example', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='User Interface', value='tab-3-example', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Documentation', value='tab-4-example', style=tab_style, selected_style=tab_selected_style)
    ], style=tabs_styles
    # content_style= {dict} to specify styles to tab content of the selected tab
    ),
    html.Div(id='tabs-content-example', style={'background-color': 'white'}),

])

# callback enables data to load (output) as new tab is pressed (input)
@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-a-example':
        return layout_taba
    elif tab == 'tab-1-example':
        return layout_background2
    elif tab == 'tab-2-example':
        return layout_tabz  # should say layout_tab2
    elif tab == 'tab-3-example':
        return layout_megan_final
    elif tab == 'tab-4-example':
        return layout_tabdoc


if __name__ == '__main__':
    app.run_server(debug=True)
