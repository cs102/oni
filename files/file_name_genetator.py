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

# the pulga factor concatenation
date = formatted_string
location = "_MA"
word = "_word_of_the_day"
print(formatted_string)

with open(date+ location + word + ".txt", "w") as file:
    file.write("array/json/ or tuple of  with words will go here")
