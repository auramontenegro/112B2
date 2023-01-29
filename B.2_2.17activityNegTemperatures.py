# Problem: calculate how many days the temperature was below zero

# Input: temperatures, a list of 7 numbers
temperatures = [5, -2, 2, 0, -3, -5, -1]

# Output: number of days, a non-negative integer
days = 0

for temperature in temperatures:
    if temperature < 0:
        days = days + 1

print('The temperature was below 0 for', days, 'days')
