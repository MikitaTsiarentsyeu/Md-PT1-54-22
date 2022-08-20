from decimal import Decimal

print('Hello, user!')

deposit = Decimal(input('Enter the deposit amount: '))

rate = Decimal(input('Enter the annual rate on the deposit: '))

term = int(input('Enter the deposit term (number of years): '))

option = input('Do you want to calculate income with capitalization? (yes or no): ')

if option == 'yes':
    income = round((deposit * (1 + rate/100/12) ** (term*12)))
else:
    income = round(deposit + (deposit*(rate/100)*term))

print(f'Income: {income}')



