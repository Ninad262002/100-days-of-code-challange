import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)


if timestamp >= "05" and timestamp < "12":
    print("Good Morning!")
elif timestamp >= "12" and timestamp < "18":
    print("Good Afternoon!")
else:
    print("Good Evening!")




# A batter appraoch 
print("-----------------------------------------------")

timestamp = time.strftime('%H')
hour = int(timestamp)

if hour >= 5 and hour < 12:
    print("Good Morning!")
elif hour >= 12 and hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")