""" Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening.
 Your program should use time module to get the current hour."""


import time

# 1. Get the current local time structure
current_struct = time.localtime()

# 2. Format it into a 24-hour string (Hour:Minute:Second)
time_24hr = time.strftime("%H:%M", current_struct)

print(time_24hr)
# Example Output: 21:41:25

if time_24hr >= "05:00" and time_24hr < "12:00":
    print("Good Morning!")
elif time_24hr > "12:00" and time_24hr < "18:00":
    print("Good Afternoon!")
else:
    print("Good Evening!")
