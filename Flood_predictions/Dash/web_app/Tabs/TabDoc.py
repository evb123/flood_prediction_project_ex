# Setting up page/layout of tab1

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from Base import app

# enter info for tab1
layout_tabdoc = html.Div([

    dcc.Markdown('''
    &nbsp;

    # Data Sources & Methodology

    This project was completed by Data Engineers at Kubrick Group between March 28th - 
    April 12th, 2019. 
     
    All code and data sources are posted on the git hub repository [The_Flood](https://github.com/ElWalkieTalkie/The_Flood).  
    
    This project would not have been possible without open data. Listed below are the citations for our data sources.
    
    ***
    
    ## Data Sources
    All Open Government Licences refer to: [http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)  
    
    #### Historical floods
    *England*: [https://data.gov.uk/dataset/16e32c53-35a6-4d54-a111-ca09031eaaaf/recorded-flood-outlines](https://data.gov.uk/dataset/16e32c53-35a6-4d54-a111-ca09031eaaaf/recorded-flood-outlines). 
    
    *Wales*: <http://lle.gov.wales/catalogue/item/HistoricFloodOutlines.json> 
    
    *Licence:* Open Government Licence
    
    #### Historical rainfall
    Met Office (2018): HadUK-Grid gridded and regional average climate observations for the UK. 04/04/19. <http://catalogue.ceda.ac.uk/uuid/4dc8450d889a491ebb20e724debe2dfb> 
    
    *Licence:* Open Government Licence
    
    #### Historical wind speed and air pressure  
    Met Office Hadley Centre (2018): UKCP18 Regional Projections on a 12km grid over the UK for 1980-2080. Centre for Environmental Data Analysis, 04/04/19. <http://catalogue.ceda.ac.uk/uuid/589211abeb844070a95d061c8cc7f604>  
    
    *Licence:* Open Government Licence 
    
    #### Projected rainfall, windspeed, and air pressure
    Met Office Hadley Centre (2018): UKCP18 Regional Projections on a 12km grid over the UK for 1980-2080. Centre for Environmental Data Analysis, 04/04/19. <http://catalogue.ceda.ac.uk/uuid/589211abeb844070a95d061c8cc7f604>  
    
    *Licence:* Open Government Licence 
    
    #### River Flow
    National River Flow Archive, 2018, <https://nrfa.ceh.ac.uk>, NERC CEH, Wallingford  
    
    *Licence:* <http://eidc.ceh.ac.uk/administration-folder/tools/ceh-standard-licence-texts/nrfa-data-terms-and-conditions-for-api-access-to-time-series-data-and-metadata/plain>
    
    #### Postcode centroids
    <https://data.gov.uk/dataset/db9345a0-42c7-4eae-832d-77d217a75efb/national-statistics-postcode-lookup-latest-centroids>, Published by: Office for National Statistics  
    
    *Licence:* Open Government Licence 
    
    #### Postcode elevation
    <https://www.getthedata.com/open-postcode-elevation>, Derived from OS Terrain 50. Each postcode is assigned an elevation based on the nearest point on a contour line from OS Terrain 50 to the approximate centre of the postcode  
    
    *Licence:* Open Government Licence 
    
    #### UK Elevation Data
    <https://www.freemaptools.com/elevation-finder.htm>  
    
    *Licence:* <https://www.openstreetmap.org/copyright>
    
    #### Geology data
    British Geological Survey (BGS) Geology 625k (DiGMapGB-625) dataset, <https://www.bgs.ac.uk/mineralsuk/maps/maps.html>  
    
    *Licence:* <https://www.bgs.ac.uk/mineralsuk/maps/licence.html>
    
    #### Flood defences
    England Flood Defence Lines:  <https://data.gov.uk/dataset/6884fcc7-4204-4028-b2fb-5059ea159f1c/spatial-flood-defences-including-standardised-attributes>, downloaded: 29/03/2019 
    
    Wales Flood Defence Lines: <https://data.gov.uk/dataset/8964d3f8-8273-4521-a4b9-3f0a268b6ecf/spatial-flood-defences-with-standardised-attributes>, downloaded: 29/03/2019 
    
    England Areas Benefiting From Flood defences: <https://environment.data.gov.uk/DefraDataDownload/?mapService=EA/FloodMapForPlanningRiversandSeaAreasBenefitingfromFloodDefences&Mode=spatial>, downloaded: 29/03/2019  
   
    Wales Areas Benefiting From Flood Defences: <https://data.gov.uk/dataset/0d8663ad-7d80-44d5-99db-58c91556e9d7/flood-map-areas-benefiting-from-flood-defences>, downloaded: 29/03/2019  
    
    *Licence:* Open Government Licence
    
    #### EU Land Classification Data
    EU land monitoring service _Copernicus_ (<https://land.copernicus.eu/>).  
    See a full list of files downloaded at : <https://github.com/ElWalkieTalkie/The_Flood/tree/master/EU%20Data%20Scripts_Imperviousness_ForestCover_Grassland_Wetness>  
    
    *Licence:* <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R1159>
    
    #### River outlines
    EU-Hydro River Network, from Copernicus (<https://land.copernicus.eu/>)  
    
    *Licence:* <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32013R1159>
    
    ***
    '''.replace('  ', ''), className='container',
                 containerProps={'style': {'maxWidth': '1000px'}}),

    dcc.Markdown('''
    ## Methodology Summary

    ### Data aquisition phase
    1. Data were collected from the sources listed above.
    2. Where necessary, data were extracted/processed using Python. Otherwise, they were imported directly to SQL database.
    
    ### Data engineering phase
    1. Data was cleaned/processed using SQL and various Python packages, most notably GeoPandas for working with spatial data.
    2. All cleaned data were stored in SQL under the clean schema.
    
    ### Modelling phase
    1. Models were built in Python using the Scikit-Learn package.
    
    ### Viz phase
    1. The dashboard application was built in Python using the Plotly/Dash framework.
    2. Data for the application was stored in JSON files and SQLite databases.
    
    '''.replace('  ', ''), className='container',
                 containerProps={'style': {'maxWidth': '1000px'}})
])
