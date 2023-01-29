# Problem: compute the sum of a list of numbers

# Input: numbers, a possibly empty list of numbers
numbers = [4, -1]

# Output: total, a non-negative integer
total = 0

for number in numbers:
    total = total + number

print('The sum of', numbers, 'is', total)
