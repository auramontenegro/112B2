# Problem: compute the length of a list

# Input: a possibly empty list of items
items = [5, -8, 3, 1, 90]

# Output: the length of list, i.w. how many items it has
length = 0

for item in items:
    length = length + 1

print('The length of', items, 'is', length)
