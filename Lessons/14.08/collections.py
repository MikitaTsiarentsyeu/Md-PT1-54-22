l = []
print(type(l))

l = [1,2,3,4,5,6,7,8,"test",[1,2,3]]
print(l)

print([1,2,3]+[4,5,6])
print([0]*5)
print(len(l))
print(l[0], l[1], l[2], l[3])
print(l[2:9:2])
print(l[-1][0])

l[0] = 1.0
print(l)

# l[999] = 1000 error

l.append("new last elem")
print(l)

l.extend([1,2,3,4])
print(l)

l.insert(0, "new first elem")
print(l)

l.insert(9, "new middle elem")
print(l)

l.remove('test')
print(l)

l.remove(2)
print(l)

print(2 in l)

del l[0]
print(l)

del l[0:9]
print(l)

x = l.pop()
print(x, l)
x = l.pop()
print(x, l)
x = l.pop()
print(x, l)
x = l.pop()
print(x, l)

x = l.pop(0)
print(x, l)

l.clear()
print(l)

del l
print(l)