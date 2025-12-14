from datetime import datetime 
import pytz # timezone module
# check python native zoneinfo module added on 3.9 
# cheatsheet https://strftime.org/
# VIM - folds Zf Zo open folds Zc close folds
date = datetime.now()
print(date)
print("year = ", date.year)
print("month = ", date.month)
print("day =  ", date.day)
print("Weekday in Numbers = ", date.weekday()) # monday is 0
print("hour = ", date.hour)
print("minute =  ", date.minute)
print("seconds = ", date.timestamp())

print("\n" + "###")
now = datetime.now()
# Format the date into "Weekday, Month Day, Year AM/PM"
# date_format set once and use as standard output
date_format = "%A, %B %d %Y, %H:%M:%S  %p %Z %z"
formatted_string = now.strftime(date_format)
print(formatted_string)
#print('Commonly used time-zones-set:',
#      pytz.common_timezones_set, '\n')

utc = pytz.utc
eastern = pytz.timezone('US/Eastern')
central = pytz.timezone('US/Central')
au_tz = pytz.timezone('Australia/Sydney')
pacific_auckland = pytz.timezone('Pacific/Auckland')
now_utc = datetime.now(utc)

print('UTC :', now_utc)

now_central = now_utc.astimezone(central)
print('US/Central : ', now_central)
central_date = now_utc.astimezone(central)
print('US/Central : ', central_date)
eastern_time = now_utc.astimezone(eastern)
print('US/Eastern : ', eastern_time)
australia_time = now_utc.astimezone(au_tz)
print('Australia :', australia_time)
nz_auckland = now_utc.astimezone(pacific_auckland).strftime(date_format)
print('NZ Auckland :', nz_auckland)
