# Problem: find a negative temperature during the week

# Input: temperatures, a list of 7 numbers
temperatures = [4, 5, -3, 1, 0, 3, -2]

# Output: a negative temperature, if it exists, or None
negative = None

for temperature in temperatures:
    if temperature < 0:
        negative = temperature

print(temperatures, 'has negative temperature', negative)
