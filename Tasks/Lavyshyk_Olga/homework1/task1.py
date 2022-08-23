import decimal
sum1 = decimal.Decimal(input("Enter deposit amount = "))
y = decimal.Decimal(input("Enter number of years = "))
N = decimal.Decimal(input("Annual interest = "))
t = input("Include monthly capitalization answer yes or no -> ").lower()
i = y*12
if t == "yes":
    var1 = round(sum1*((N/100/12+1)**i))
    print("Your account, taking into account the monthly capitalization, will be", var1)
elif t == "no":
    var2 = round(sum1 * N / 100 * y + sum1)
    print("Your account with excluding monthly capitalization will be", var2)
else:
    print("You entered an invalid value, try again")