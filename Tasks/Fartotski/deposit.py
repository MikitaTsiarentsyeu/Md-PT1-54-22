from decimal import Decimal
money = Decimal(input("please, enter the deposit: \n"))
year = Decimal(input("please, enter the number of years: \n"))
interest = Decimal(input("please, enter the interest on the deposit: \n"))
capit = str(input("Do you want to count the monthly capitalization? Yes or No?: \n"))
i = 1
month = year * 12
if capit.upper()=="YES":
    while i <= month:
        money = money + ((money * interest * 30) / (100 * 365))
        money = money.quantize(Decimal("1.00"))
        i = i + 1
    print("You will have " + str(money))
else:
    money = money + (money * interest / 100) * year
    money = money.quantize(Decimal("1.00"))
    print("You will have " + str(money))

