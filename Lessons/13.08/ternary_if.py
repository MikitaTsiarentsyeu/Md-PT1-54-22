print("it's true") if False else print("it's not")

x = "it's true" if False else "it's not"
print(x)

x = 0

if x == 0:
    print("it's zero")
elif x > 0:
    print("it's positive")
else:
    print("it's negative")

print("it's zero") if x == 0 else ...
print("it's positive") if x > 0 else print("it's negative")