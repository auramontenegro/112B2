# initialise the input
#temperatures = get_input()
temperatures = [5, 4, 3, 2, -1, 0]

# initialise outside_range list
outside_range = []

# determine lenght of temperatures list
length_temperatures = len(temperatures)


# check each temperature in the list is in the range 0 to 5 inclusive
for temperature in temperatures:
    if temperature > 5 or temperature < 0:
        outside_range = outside_range + [temperature]


# determine lenght of out_of_range list
length_outside_range = len(outside_range)

# calculate percentage of temperatures out of range 0 to 5
percentage_outside_range = length_outside_range / length_temperatures * 100

print(int(percentage_outside_range),'% of values are outside the range')
