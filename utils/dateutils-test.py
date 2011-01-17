from dateutils import sql_datetime_to_human_date, sql_datetime_to_12hr_time
from datetime import datetime

def sql_datetime_to_human_date_current_year_test():
	current_year = datetime.now().year
	human = sql_datetime_to_human_date('%s-01-01 10:30:15' % current_year)
	assert(human == 'Jan 01')

def sql_datetime_to_human_date_test():
	human = sql_datetime_to_human_date('2009-01-01 10:30:15')
	assert(human == 'Jan 01, 2009')
	
def sql_datetime_to_12hr_time_test():
	hr_time = sql_datetime_to_12hr_time('2010-11-29 01:40:15')
	assert(hr_time == '1:40 PM')