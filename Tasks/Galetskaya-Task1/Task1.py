from decimal import ROUND_CEILING, Decimal


print('Please, enter your deposit amount.')
deposit = Decimal(input())
print('Please, enter the term of the deposit in years.')
year = int(input())
print('Please, enter the annual percentage in numbers.')
percent = int(input())
print('Do you want to enable monthly capitalization? Please, type YES or NO.')
capitalization = input().upper()

if capitalization == 'YES':
    first_deposit = deposit
    deposit = deposit * (1 + Decimal(percent / 100 / 12)) ** (year * 12)  #increase deposit body every month
    deposit = deposit.quantize(Decimal('1.00'), ROUND_CEILING)
    print(f'Amount on deposit: {deposit}')
elif capitalization == 'NO':
    deposit = (deposit + Decimal((deposit * percent / 100)) * year)
    deposit = deposit.quantize(Decimal('1.00'), ROUND_CEILING)
    print(f'Amount on deposit: {deposit}')
else:
    print('Uncorrect enter. Please, try again.')
    