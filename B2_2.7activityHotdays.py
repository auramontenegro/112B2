# Problem: construct a list of temperatures above 30 degrees celcius from
#a list of daily temperatures.

# Input: input_list, list of temperatures in degrees celcius interger
input_list = [28, 35, 33, 38, 25, 26, 22, 30, 31, 36, 32, 32, 26, 29, 30, 33]

# Input: position, represents position in the list
temperature = 0

# Input: input_value,
input_value = []

# Output: output_list, resulting list with temperatures above 30 degrees celcius
output_list = []

for position in range(0, len(input_list)):
    input_value = input_list[position]
    if input_value > 30:
        output_list = output_list + [input_value]
print(output_list)

