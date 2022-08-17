import decimal

p = 1
while p <2:
    x = input("Please, enter the amount of money:\n")
    try:
        check = float(x)
    except ValueError:
        print("Please, enter the amount of money in a numerical value")
    else:
        p = 2
x = decimal.Decimal(x)
x = round(x, 2)
p = 1
while p <2:
    y = input("Please, enter the deposit's term (Years):\n")   
    try:
        check = float(y)
    except ValueError:
        print("Please, enter the deposit's term in a numerical value")
    else:
        p = 2
y = decimal.Decimal(y)
y = round(y, 0)
p = 1
while p <2:
    z = input("Please, enter the annual percentage:\n")   
    try:
        check = float(y)
    except ValueError:
        print("Please, enter the annual percentage in a numerical value")
    else:
        p = 2
z = decimal.Decimal(z)
z = round(z, 2)
o = 1
while o < 2:
    q = input("Do you want to include monthly capitalization? (Y/N)\n")   
    if q == "N":
        s = round(x/100*y*z+x, 2)
        print("You will resive", s, "after", y, "years without monthly capitalization")
        o = 2
    elif q == "Y":
        s = round(((1+((z/100)/12))**(y*12))*x, 2)
        print("You will resive", s, "after", y, "years with monthly capitalization")
        o = 2
    else:
        print("Please, enter only Y or N")