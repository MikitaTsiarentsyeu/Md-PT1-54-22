import decimal

print('Values deposit: initial amount - 20000 BYN; Term - 5 years; Annual interest- 15%;')

amount = decimal.Decimal(
    input('Please, enter the initial deposit amount, BYN: \n'))
term = decimal.Decimal(input('Please, enter the deposit term, years: \n'))
rate = decimal.Decimal(input('Please, enter the annual interest rate, % \n'))
cap = int(input('Choose a way to capitalize: \n Monthly - 1 \n Annualy - 2 \n'))

if cap == 1:
    month = term * 12
    total = amount * (1 + rate/100/12) ** month
    print(f'Monthly capitalization total: {total:.2f} BYN')
elif cap == 2:
    total = amount * (1 + rate/100*term)
    print(f'Annualy capitalization total: {total:.2f} BYN')
else:
    print('Incorrectly entered data! Try again!')
