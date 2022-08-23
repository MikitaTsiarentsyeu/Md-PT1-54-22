eq = input("Input your eq in like y=kx+b:\n")
x = int(input("Enter the x value:\n"))

eq = eq.lower().replace(" ", "").replace("y=", "")
# print(eq)

# coeff = eq.split('x')
# print(coeff)

# y = x * int(coeff[0]) + int(coeff[1])
# print(y)

i = eq.index('x')
print(i)

k = int(eq[:i])
b = int(eq[i+1:])

y = x*k + b
print(y)