from enum import Enum

# Lookml types
class LookerMeasureType(str, Enum):
    number = 'number'
    string = 'string'
    average = 'average'
    average_distinct = 'average_distinct'
    count = 'count'
    count_distinct = 'count_distinct'
    list = 'list'
    max = 'max'
    median = 'median'
    median_distinct = 'median_distinct'
    min = 'min'
    sum = 'sum'
    sum_distinct = 'sum_distinct'

class LookerValueFormatName(str, Enum):
    decimal_0 = 'decimal_0'
    decimal_1 = 'decimal_1'
    decimal_2 = 'decimal_2'
    decimal_3 = 'decimal_3'
    decimal_4 = 'decimal_4'
    usd_0 = 'usd_0'
    usd = 'usd'
    gbp_0 = 'gbp_0'
    gbp = 'gbp'
    eur_0 = 'eur_0'
    eur = 'eur'
    id = 'id'
    percent_0 = 'percent_0'
    percent_1 = 'percent_1'
    percent_2 = 'percent_2'
    percent_3 = 'percent_3'
    percent_4 = 'percent_4'

class LookerTimeFrame(str, Enum):
    date = 'date'
    day_of_month = 'day_of_month'
    day_of_week = 'day_of_week'
    day_of_week_index = 'day_of_week_index'
    day_of_year = 'day_of_year'
    fiscal_month_num = 'fiscal_month_num'
    fiscal_quarter = 'fiscal_quarter'
    fiscal_quarter_of_year  = 'fiscal_quarter_of_year'
    fiscal_year = 'fiscal_year'
    hour = 'hour'
    hour2 = 'hour2'
    hour3 = 'hour3'
    hour4 = 'hour4'
    hour6 = 'hour6'
    hour8 = 'hour8'
    hour12 = 'hour12'
    hour_of_day = 'hour_of_day'
    microsecond = 'microsecond'
    millisecond = 'millisecond'
    millisecond2 = 'millisecond2'
    millisecond4 = 'millisecond4'
    millisecond5 = 'millisecond5'
    millisecond8 = 'millisecond8'
    millisecond10 = 'millisecond10'
    millisecond20 = 'millisecond20'
    millisecond25 = 'millisecond25'
    millisecond40 = 'millisecond40'
    millisecond50 = 'millisecond50'
    millisecond100 = 'millisecond100'
    millisecond125 = 'millisecond125'
    millisecond200 = 'millisecond200'
    millisecond250 = 'millisecond250'
    millisecond500 = 'millisecond500'
    minute = 'minute'
    minute2 = 'minute2'
    minute3 = 'minute3'
    minute4 = 'minute4'
    minute5 = 'minute5'
    minute6 = 'minute6'
    minute10 = 'minute10'
    minute12 = 'minute12'
    minute15 = 'minute15'
    minute20 = 'minute20'
    minute30 = 'minute30'
    month = 'month'
    month_name = 'month_name'
    month_num = 'month_num'
    quarter = 'quarter'
    quarter_of_year = 'quarter_of_year'
    raw = 'raw'
    second = 'second'
    time = 'time'
    time_of_day = 'time_of_day'
    week = 'week'
    week_of_year = 'week_of_year'
    year = 'year'
    yesno = 'yesno'