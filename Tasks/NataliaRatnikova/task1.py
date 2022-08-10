import decimal

deposit_sum = decimal.Decimal(input("Please enter the sum of your deposit:\n"))
deposit_term = decimal.Decimal(input("Please enter the term of your deposit(years):\n"))
deposit_percent = decimal.Decimal(input("Please enter the percent of your deposit(for 1 year):\n"))
capitalazation = str(input("Would you like to have monthly capitalization?(enter yes or no):\n")) 
if capitalazation == "yes" or capitalazation == "Yes" or capitalazation == "Y" or capitalazation == "y":
    final_sum = deposit_sum*(1+deposit_percent/100/12)**(deposit_term*12)
    print("The final sum of your deposit is", final_sum.quantize(decimal.Decimal("1.00")))   
else:
    final_sum = deposit_sum+deposit_sum*deposit_percent/100*deposit_term
    print("The final sum of your deposit is", final_sum)

