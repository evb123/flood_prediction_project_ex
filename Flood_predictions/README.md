# Predicted Dynamic Data (Rainfall (mm/day), Windspeed (m/s), Air Pressure at Sea Level (hPa))

Author: Evelyn Byer
Date started: 29/03/19
Date finished: 03/04/19
Edited 12/04/19 by Jacob Morl

# Data sources
Predicted data is taken from the Met Office's climate projection UKCP18. This is displayed in a 12km grid for the UK. 
It assumes emissions scenario RCP8.5.

Downloaded on 01/04/19 from CEDA website:
http://data.ceda.ac.uk/badc/ukcp18/data/land-rcm/uk/12km/rcp85/15/

### The specific download page is:
#### For rainfall(pr):
http://data.ceda.ac.uk/badc/ukcp18/data/land-rcm/uk/12km/rcp85/15/pr/day/latest/

#### For pressure at sea level (psl):
http://data.ceda.ac.uk/badc/ukcp18/data/land-rcm/uk/12km/rcp85/15/psl/day/latest/

#### For windspeed (sfcWind):
http://data.ceda.ac.uk/badc/ukcp18/data/land-rcm/uk/12km/rcp85/15/psl/day/latest/

### Date range:
2020-2030 (in file name)

### Description/documentation of data:
https://www.metoffice.gov.uk/binaries/content/assets/mohippo/pdf/ukcp18/data-availability-access-and-formats-.pdf

# Data processing

## Python
Data is provided as netCDF4 files (.nc file extension).
The data were extracted, inserted into a pandas dataframes, and exported to csv to be loaded in an MSSQL table using python scripts. 
Python scripts: import_psl.py, import_rainfall.py, import_winsdpeed.py
Before running the script install the netCDF4 python package (conda install netCDF4).
**note: these files will create dataframes with 33M rows and take approx. 2.5 hours to run.

## MSSQL tables
Tables were manually inserted into trs database using csv ouputs from above under schema 'stage.'
- [stage].[projected_pr_daily_12km_2020_2030]
- [stage].[projected_psl_12km_2020_2030]
- [stage].[projected_windspeed_12km_2020_2030]

One table was created for each variable (including locationID and monthly/yearly aggregations) + one table linking locationID with grid values under schema 'dim.'
- Locations: [dim].[projected_features_12km_grid_location]
- Rainfall: [dim].[projected_pr_daily_12km_values_2020_2030_agg]
- PSL: [dim].[projected_psl_daily_12km_values_2020_2030_agg]
- Windspeed: [dim].[projected_windspeed_daily_12km_values_2020_2030_agg]

The code to create these tables is located in files: 
- Rainfall_12km_daily_agg.sql
- PSL_12km_daily_agg.sql
- Windspeed_12km_daily_agg.sql
- Location_grid_12km.sql

These tables are then joined with the clean 5km grid IDs to run the model:
- Joining_grid_ID_to_predictions.sql

Seven day moving sum is then calculated for the projected rainfall by:
- proj_seven_day_sum_calculation.sql