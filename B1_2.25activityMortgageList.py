# Problem: generate the monthly outstanding mortgage

# Input: annual loan interest rate, a floating-point percentage rate = 0.05
rate = 0.05

# Input: monthly payment, a positive integer in a currency payment = 200
payment = 200

# input: mortgage, a positive number, same currency mortgage = 1000
mortgage = 1000

# Output: list of monthly outstanding mortgage amounts
outstanding = []

outstanding = outstanding + [mortgage]
while mortgage > 0:
    interest = mortgage * rate / 12
    mortgage = mortgage + interest - payment
    outstanding = outstanding + [mortgage]

print('Outstanding mortgage, month by month:', outstanding)
