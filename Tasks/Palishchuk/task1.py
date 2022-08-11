import decimal

deposit = decimal.Decimal(input("Enter the deposit amount:\n"))
term = int(input("Enter the term of your deposit (in years):\n"))
percent = decimal.Decimal("0.15")
amount = deposit
capitalization = 12
period = term * capitalization
text = input("Do you want to enable monthly capitalizaion of your deposit (Yes or No)?\n")
count = 1

if text == "Yes":
    while (count <= period):
        deposit = deposit + (deposit*percent/capitalization)
        count += 1
else:
    deposit = deposit + ((deposit*percent)*term)

print("Your deposit was:", round(amount, 2))
print("Term:", term, "year")
print("Your amount at the end of the term will be:", round(deposit, 2))
print("Your income will be:", round(deposit - amount, 2))