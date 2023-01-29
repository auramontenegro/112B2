# Problem: convert temperatures from Celcius to Fahrenheit

# Input: a possibly empty list of temperatures in Celcius
celcius_temperatures = [22, 30, 31, 36, 32, 32, 26, 29, 30, 33]

# Output: the list of temperatures converted to Fahrenheit
fahrenheit_temperatures = []

for temperature in celcius_temperatures:
    fahrenheit_value = temperature * 9/5 + 32
    fahrenheit_temperatures = fahrenheit_temperatures + [fahrenheit_value]

print ('Temperatures in Fahrenheit:', fahrenheit_temperatures)
