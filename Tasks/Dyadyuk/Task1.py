import decimal

A = decimal.Decimal(input('Please, enter initial amount :\n'))
B = decimal.Decimal(input('Please, enter number of years :\n'))
C = decimal.Decimal(input('Please, enter annual interest rate :\n'))

W = A * ((1 + (C/100)/12)**(B*12))
Q = A * ((1 + (C/100))**B)

answer = input('Do you want to include monthly capitalization? Enter "yes" or "no" :\n ')

if answer.upper() == 'YES' :
    print('Your deposit will become', round(W, 2))
else :
    print('Your deposit will become', round(Q, 2))



