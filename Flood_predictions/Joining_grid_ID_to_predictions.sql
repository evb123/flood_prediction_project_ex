-- joining GridID to predicted features
-- Author: Ev Byer
-- Date: 05-04-2019
use trs
go

--Select top 10
--	*
--from clean.grid5k --to check grid we're joining to 

-- cleaning up tables before creating new ones
if OBJECT_ID('clean.proj_rainfall_12km') is not null
	drop table clean.proj_rainfall_12km;

if OBJECT_ID('clean.proj_pressure_12km') is not null
	drop table clean.proj_pressure_12km;

if OBJECT_ID('clean.proj_windspeed_12km') is not null
	drop table clean.proj_windspeed_12km;
go
-- joining GridID to precipitation/rainfall

select
	GridID,
	left([Date],10) as dte,
	yr, 
	mnth, 
	rainfall_mm_day, 
	avg_mnth, min_mnth, 
	max_mnth, 
	cum_mnth, 
	avg_yr, 
	min_yr, 
	max_yr, 
	cum_yr
into clean.proj_rainfall_12km
from [clean].[projected_features_12km_grid_location] gg
left join [dim].[projected_pr_daily_12km_values_2020_2030_agg] vv
	on gg.LocationID = vv.LocationID
where [yr] between 2021 and 2025 -- for predicting 5 year interval


-- joining GridID to pressure
select
	GridID,
	left([Date],10) as dte, yr, mnth, pressure_sea_level_hPa, avg_mnth, min_mnth, max_mnth, avg_yr, min_yr, max_yr
into clean.proj_pressure_12km
from [clean].[projected_features_12km_grid_location] gg
left join [dim].[projected_psl_daily_12km_values_2020_2030_agg] vv
	on gg.LocationID = vv.LocationID
where [yr] between 2021 and 2025 -- for predicting 5 year interval


-- joining GridID to windspeed
select
	GridID,
	left([Date],10) as dte, yr, mnth, windspeed_m_s, avg_mnth, min_mnth, max_mnth, avg_yr, min_yr, max_yr
into clean.proj_windspeed_12km
from [clean].[projected_features_12km_grid_location] gg
left join [dim].[projected_windspeed_daily_12km_values_2020_2030_agg] vv
	on gg.LocationID = vv.LocationID
where [yr] between 2021 and 2025 -- for predicting 5 year interval
