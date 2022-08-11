x = True
y = False

j = True

print(x, y, j, type(j))

print(id(x), id(y), id(j))

print(x == y)

print(1 == True)
print(8+True)
# print(8/False)

print(not True)
print(not False)

print(not not False)

print(not not 3)
print(not not '3')
print(not not [3])

print(not not 0)
print(not not '')
print(not not [])

x = print("test print")
print(x, type(x))
print(not not x)

x = True
y = False
j = True

print(x and y or j)
print(x and (y or j))
print((2+4)-2)

print(x and j or y)
print(x and (j or y))
print((2+4)-2)

print("test" and True)
print("test" and False)
print(bool("test"))
print(True and "True string")
print(True and 58)
print(3 or False)

print(3 or False or 5)

print(0 and 1)

print(bool(print("left") and print("right")))
print(bool(not print("left") and print("right")))