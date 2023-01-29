# initialise the input with a non-empty list - Do NOT change the next line
temperatures = [4.7, 3, 4.8]
# set best_position to 0
max_temperature = temperatures[0]
best_position = 0
# for each position from 1 to length of list – 1:
for temperature in temperatures[1:]:
    
  
    # if the item at position is better than the item at best_position: 
    if temperature > max_temperature:
        # set best_position to position
        best_position = temperatures.index(temperature)
# print best_position
print( best_position,': 00')
