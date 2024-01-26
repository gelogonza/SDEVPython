#3.1
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour
print('This is how many seconds are in an hour!', seconds_per_hour)

#3.2 Assigned result to seconds_per_hour variable already

#3.3
hours_per_day = 24
seconds_per_day = hours_per_day * seconds_per_hour
print('This is how many seconds there are in a day!', seconds_per_day)

#3.4 Assigned the result to seconds_per_day already

#3.5
floating_point_division = seconds_per_day / seconds_per_hour
print('this is the result using floating point division!', floating_point_division)

#3.6
integer_division = seconds_per_day // seconds_per_hour
print('this is the result using integer division!', integer_division)