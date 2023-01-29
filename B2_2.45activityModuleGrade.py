# Compute the module grade

# initialise marks to a list of 4 integers from 0 to 100
marks = [0, 60, 30, 50]

## determine the lowest of the 4 marks (retrieval: find best)

lowest = marks[0]

for mark in marks:

    if mark < lowest:
        lowest = mark

## compute mean of the best 3 marks (aggregation)

### compute the sum of the 4 marks (aggregation)

total = 0

for mark in marks:
    mark = total + mark

### substract the lowest mark (formula)

total = total - lowest

### divide the result by 3 (formula)

mean = total / 3

## compute the grade for that mean (ase analysis)

if mean < 30:

    grade = 'fail'

elif mean < 40:
    grade = 'resti'

else:
    grade = 'pass'

print(grade)
