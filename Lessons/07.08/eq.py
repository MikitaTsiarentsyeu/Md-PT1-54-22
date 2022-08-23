# a, b, c = 3, -14, -5

# D = b**2-4*a*c

# print(D)

# x1 = (-b+D**0.5)/(2*a)
# x2 = (-b-D**0.5)/(2*a)

# print(x1, x2)

a, b, c = float(input("the a value:\n")), float(input("the b value:\n")), float(input("the c value:\n"))

D = b**2-4*a*c

if D > 0:
    print("the first root is", (-b+D**0.5)/(2*a))
    print("the second root is", (-b-D**0.5)/(2*a))
elif D == 0:
    print("the root is", -b/(2*a))
else:
    print("there are no roots")