from datetime import datetime 
import pytz # timezone module
# check python native zoneinfo module added on 3.9 

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
# Format the date into "Weekday, Month Day, Year"
formatted_string = now.strftime("%A, %B %d, %Y")
print(formatted_string)
#print('Commonly used time-zones-set:',
#      pytz.common_timezones_set, '\n')

utc = pytz.utc
eastern = pytz.timezone('US/Eastern')
central = pytz.timezone('US/Central')
au_tz = pytz.timezone('Australia/Sydney')
pacific_auckland = pytz.timezone('Pacific/Auckland')
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
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
nz_auckland = now_utc.astimezone(pacific_auckland)
print('NZ Auckland :', nz_auckland)
