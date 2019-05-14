# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:19:49 2019

@author: MeganDuffy
"""

# %-------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------%
from netCDF4 import Dataset, num2date
import pandas as pd
import os 
#%%

file= r"C:\Users\EvelynByer\Documents\Flook Risk\windspeed\sfcWind_rcp85_land-rcm_uk_12km_15_day_20201201-20301130.nc"

dataset = Dataset(file,'r')
      
dataset.variables

#%%
rootdir = r"C:\Users\EvelynByer\Documents\Flook Risk\windspeed"


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))
        #%-------------------------------------------------------------------
        # File read- iterate through all files in root directory
        # ---------------------------------------------------------------------%
        file_path = os.path.join(subdir, file)
        dataset = Dataset(file_path,'r')
    
        # %-------------------------------------------------------------------
        # Extract data from netCD4 dataset object
        # ---------------------------------------------------------------------%    
        windspeed_m_s = dataset.variables['sfcWind'][:]
        latitude = pd.DataFrame(dataset.variables['grid_latitude'][:])
        longitude = pd.DataFrame(dataset.variables['grid_longitude'][:])
        x_coord = pd.Series(dataset.variables['projection_x_coordinate'][:])
        y_coord = pd.Series(dataset.variables['projection_y_coordinate'][:])
        x_bnds = pd.DataFrame(dataset.variables['projection_x_coordinate_bnds'][:])
        y_bnds = pd.DataFrame(dataset.variables['projection_y_coordinate_bnds'][:])
        time_unit =dataset.variables['time'].units
        time = pd.Series(num2date(dataset.variables['time'][:],time_unit, calendar='360_day'))   
        
        # %-------------------------------------------------------------------
        # Create dataframe Rainfinal containing all geographical data
        # ---------------------------------------------------------------------%
        rows_list = []
        for i in range(0,len(time)):
            rainfall2 = pd.DataFrame(windspeed_m_s[0,i,:,:])
            for n in range(0,rainfall2.shape[0]):
                for m in range(0,rainfall2.shape[1]):
                    dict1 = {'grid_latitude':latitude.loc[n,m],
                             'grid_longitude':longitude.loc[n,m],
                             'x_coord':x_coord.loc[m],
                             'y_coord':y_coord.loc[n],
                             'x_bnd_upper':x_bnds.loc[m,1],
                             'y_bnd_upper':y_bnds.loc[n,1],
                             'x_bnd_lower':x_bnds.loc[m,0],
                             'y_bnd_lower':y_bnds.loc[n,0],
                             'Date':time[i],
                             'windspeed_m_s':rainfall2.loc[n,m]}
                    rows_list.append(dict1)
wind = pd.DataFrame(rows_list)
wind.to_csv(r"C:\Users\EvelynByer\Documents\Flook Risk\projected_windspeed_12km.csv", encoding='utf-8', index=False)