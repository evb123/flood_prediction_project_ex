-- Creating location grid for 12 km grid from model projection
--
select
	'E'+x_coord+'N'+y_coord LocationID
	,x_coord
	,x_bnd_lower
	,x_bnd_upper
	,y_coord
	,y_bnd_lower
	,y_bnd_upper
	,grid_latitude
	,grid_longitude
into [dim].[projected_features_12km_grid_location]
from [stage].[projected_windspeed_12km_2020_2030]
where [Date] = '2020-12-01 12:00:00'