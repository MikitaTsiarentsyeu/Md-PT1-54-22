import decimal
quantize(Decimal("1.00"))
# decimal.getcontext().prec = 2

deposit_summ = decimal.Decimal(input("Please enter the summ of your deposit:\n"))
deposit_term = decimal.Decimal(input("Please enter the term of your deposit(years):\n"))
deposit_percent = decimal.Decimal(input("Please enter the percent of your deposit(for 1 year):\n"))
capitalazation = str(input("Would you like to have capitalization each months?(enter yes or no):\n")) 
if capitalazation == "yes" or capitalazation == "Yes" or capitalazation == "Y" or capitalazation == "y":
    print("The final summ of your deposit is", (deposit_summ*(1+deposit_percent/100/12)**(deposit_term*12)))   
else:
    print("The final summ of your deposit is", (deposit_summ+deposit_summ*deposit_percent/100*deposit_term))

