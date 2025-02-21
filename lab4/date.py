#1
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()
# Subtract 5 days
five_days_ago = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("5 days ago:", five_days_ago.strftime("%Y-%m-%d"))

#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3
from datetime import datetime

current_datetime = datetime.now()
no_microseconds = current_datetime.replace(microsecond=0)

print("With microseconds:", current_datetime)
print("Without microseconds:", no_microseconds)

#4
from datetime import datetime

date1 = datetime(2025, 2, 20, 15, 30, 0)
date2 = datetime(2025, 2, 21, 17, 0, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Time difference:", difference)
print("Difference in seconds:", int(seconds))