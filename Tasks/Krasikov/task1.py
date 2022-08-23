from decimal import *
print('Welcome to BlaBlaBank!')
invest = Decimal(input('Please enter the amount of your starting capital(USD): \n'))
term = Decimal(input('What is the capitalization period in years: \n'))
perc = Decimal(input('We have several interest rates, which one did you choose: \n'))
print('We can offer you the option of monthly interest capitalization.\n')
guess = input("If you're interested, please enter 'Y', otherwise press 'Enter' on ur keyboard: \n")
k = perc/100
amount = 0
if guess == 'Y':
    amount = invest*((1 + k/12))**(12*term)
    print('Your monthly capitalization from ',round(term),' year amounted:', amount.quantize(Decimal('0.01'), rounding=ROUND_UP),' USD')
    print('Thanks for using our service!')
else:
    amount = (invest*k*term)+invest
    print('Your standard capitalization from ',round(term),' year amounted:', amount.quantize(Decimal('0.01'), rounding=ROUND_UP),' USD')
    print('Thanks for using our service!')

    
    
