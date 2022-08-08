print('Welcome to BlaBlaBank!')
invest = float(input('Please enter the amount of your starting capital(USD): \n'))
term = float(input('What is the capitalization period in years: \n'))
perc = float(input('We have several interest rates, which one did you choose: \n'))
print('We can offer you the option of monthly interest capitalization.\n')
guess = input("If you're interested, please enter 'Y', otherwise press 'Enter': \n")
k = perc/100
amount = 0
if guess == 'Y':
    amount = invest*((1 + k/12))**(12*term)
    print('Your monthly capitalization from ',round(term),' year amounted:', round(amount, 2),' USD')
else:
    amount = (invest*k*term)+invest
    print('Your standard capitalization from ',round(term),' year amounted:', round(amount, 2),' USD')


    
    
