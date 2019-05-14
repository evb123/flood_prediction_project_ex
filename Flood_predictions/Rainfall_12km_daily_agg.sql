use trs
go

-- to observe the data
select top 10
*
from [stage].[projected_pr_daily_12km_2020_2030]

---------------------------------------------------------------
-- to create new table with aggregates over month and year into schema 'dim'
-- Location ID links to table
Select
*
,avg(cast([rainfall_mm_day] as float)) over (partition by mnth,yr,LocationID) avg_mnth
,min(cast([rainfall_mm_day] as float)) over (partition by mnth,yr,LocationID) min_mnth
,max(cast([rainfall_mm_day] as float)) over (partition by mnth,yr,LocationID) max_mnth
,sum(cast([rainfall_mm_day] as float)) over (partition by mnth,yr,LocationID) cum_mnth
,avg(cast([rainfall_mm_day] as float)) over (partition by yr,LocationID) avg_yr
,min(cast([rainfall_mm_day] as float)) over (partition by yr,LocationID) min_yr
,max(cast([rainfall_mm_day] as float)) over (partition by yr,LocationID) max_yr
,sum(cast([rainfall_mm_day] as float)) over (partition by yr,LocationID) cum_yr
into dim.projected_pr_daily_12km_values_2020_2030_agg
from
(
select
	'E'+x_coord+'N'+y_coord LocationID
	,[Date]
	,left([Date],4) yr
	,substring([Date],6,2) mnth
	,cast([Rainfall (mm) day] as float) rainfall_mm_day
from [stage].[projected_pr_daily_12km_2020_2030]
--where x_coord = '42000.0' --for testing arithmetic so less than 33 mill rows are loaded
)t
