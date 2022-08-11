sum1 = int(input("Enter deposit amount = "))
y = int(input("Enter number of years = "))
N = float(input("Annual interest = "))
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
