from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M")
print("Current Time =", current_time)
if("10:05" > current_time):
    print("Eorng")
else:
    print("right")