import decimal
from decimal import Decimal
# We weren't supposed to use Decimal for this, just the basic data types.....
# But come on.
print('Welcome to the tip calculator')
bill = Decimal(input('What was the total bill? $'))
split = Decimal(input('How many people to split the bill? '))
percentage = Decimal(input('What percentage tip would you like to give? 10, 12, or 15? '))
individual_payment = (bill / split) + (bill / split * percentage / 100)
individual_payment = round(individual_payment,2)
print('Each person should pay: $' + str(individual_payment))