import decimal
depo, period, percent, cap = decimal.Decimal(input('Enter start depo amount:\n')), int(input('Enter period (years):\n')), decimal.Decimal(input('Enter percentage in a year:\n')), input('Do you want monthly capitalization? (Yes/No)\n')
if cap == 'No':
    for i in range(period):
        depo = depo + depo*(percent/100)
elif cap == 'Yes':
    for i in range(period*12):
        depo = depo + depo*(percent/100/12)
print('Your depo will be:', round(depo, 2))