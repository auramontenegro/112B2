# Problem: obtain temperatures above a threshold

# Input: a possibly empty list of temperatures in Celcius
daily_temperatures = [28, 35, 33, 38, 25, 26, 22, 30, 31, 36, 32, 32, 26, 29, 30, 33]

# Output: the list of temperatures above 30
hot_days = []

for temperature in daily_temperatures:
    if temperature > 30:
        hot_days = hot_days + [temperature]

print ('The hot days had temperatures', hot_days)
