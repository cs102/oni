#file name generator
# date
# location
# word root

from datetime import datetime
import pytz

now = datetime.now()
#date_format = "%A, %B %d %Y, %H:%M:%S  %p %Z %z"
date_format ="%Y-%m-%d_%l:%M%p"
formatted_string = now.strftime(date_format)
print(formatted_string)

file_path = 'formatted_string'

print(str(formatted_string))

with open(file_path + ".txt", "w") as file:
    file.write("Your text goes here")
