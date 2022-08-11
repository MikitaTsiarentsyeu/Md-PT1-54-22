amount = float(input('Please enter amount of deposit, USD \n'))
term = float(input('Please enter term of deposit, years \n'))
interest = float(input('Please enter interest rate, % \n'))
cap = input('Do you want to turn on monthly capitalization? [yes/no] \n')
finalwocap = amount+(amount*term*interest)/100
finalcap = amount*((1+interest/12/100)**(term*12))
if cap=='yes':
    print('Estimated amount of deposit in the end of its term is equal to',round(finalcap,2),'USD')
elif cap=='no':
    print('Estimated amount of deposit in the end of its term is equal to',round(finalwocap,2),'USD')
else: print('Capitalization parameter was filled in incorrectly')