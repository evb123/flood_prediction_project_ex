use trs
go
-------------------------------------------------------------------
select top 10
*
from
[stage].[projected_windspeed_12km_2020_2030]
------------------------------------------------------------

---------------------------------------------------------------

Select
*
,avg(cast([windspeed_m_s] as float)) over (partition by mnth,yr,LocationID) avg_mnth
,min(cast([windspeed_m_s] as float)) over (partition by mnth,yr,LocationID) min_mnth
,max(cast([windspeed_m_s] as float)) over (partition by mnth,yr,LocationID) max_mnth

,avg(cast(windspeed_m_s as float)) over (partition by yr,LocationID) avg_yr
,min(cast(windspeed_m_s as float)) over (partition by yr,LocationID) min_yr
,max(cast(windspeed_m_s as float)) over (partition by yr,LocationID) max_yr
into [dim].[projected_windspeed_daily_12km_values_2020_2030_agg]
from
(
select
	'E'+x_coord+'N'+y_coord LocationID
	,[Date]
	,left([Date],4) yr
	,substring([Date],6,2) mnth
	,cast([windspeed_m_s] as float) [windspeed_m_s]
from [stage].[projected_windspeed_12km_2020_2030]
--where x_coord = '42000.0' --for testing arithmetic so less than 33 mill rows are loaded
)t
