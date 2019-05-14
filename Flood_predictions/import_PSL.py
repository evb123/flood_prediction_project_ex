# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:49:02 2019

@author: EvelynByer
"""

# %-------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------%
from netCDF4 import Dataset, num2date
import pandas as pd
 
#%%
file = r"C:\Users\EvelynByer\Documents\Flook Risk\projected_pressure_SL\psl_rcp85_land-rcm_uk_12km_15_day_20201201-20301130.nc"

dataset = Dataset(file,'r')

dataset.variables # will show dict-like object containing variables and metadata
#%% 
# %-------------------------------------------------------------------
# Create initial dataframes
# ---------------------------------------------------------------------%    
my_var = dataset.variables['psl'][:] #must change depending on variable!!!
grid_latitude = pd.DataFrame(dataset.variables['grid_latitude'][:])
grid_longitude = pd.DataFrame(dataset.variables['grid_longitude'][:])
x_coord = pd.Series(dataset.variables['projection_x_coordinate'][:])
y_coord = pd.Series(dataset.variables['projection_y_coordinate'][:])
x_bnds = pd.DataFrame(dataset.variables['projection_x_coordinate_bnds'][:])
y_bnds = pd.DataFrame(dataset.variables['projection_y_coordinate_bnds'][:])
time_unit =dataset.variables['time'].units
time = pd.Series(num2date(dataset.variables['time'][:],time_unit, calendar='360_day'))   
#%%
# %-------------------------------------------------------------------
# Create final dataframe
# ---------------------------------------------------------------------%    
rows_list = []
for i in range(0,len(time)):
    rainfall2 = pd.DataFrame(my_var[0,i,:,:]) #4-D (vertical/time/spatial/spatial)
    for n in range(0,rainfall2.shape[0]):
        for m in range(0,rainfall2.shape[1]):
            dict1 = {'Latitude':grid_latitude.loc[n,m],
                     'Longitude':grid_longitude.loc[n,m],
                     'x_coord':x_coord.loc[m],
                     'y_coord':y_coord.loc[n],
                     'x_bnd_upper':x_bnds.loc[m,1],
                     'y_bnd_upper':y_bnds.loc[n,1],
                     'x_bnd_lower':x_bnds.loc[m,0],
                     'y_bnd_lower':y_bnds.loc[n,0],
                     'Date':time[i],
                     'windspeed_m_s':rainfall2.loc[n,m]}
            rows_list.append(dict1)
final = pd.DataFrame(rows_list)

#export to csv to be loaded into SQL
final.to_csv(r"C:\Users\EvelynByer\Documents\Flook Risk\projected_sql_PSL.csv", encoding='utf-8', index=False)
