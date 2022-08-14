t = (1,2,3,4,5,"test",[])
print(type(t), t)

t = ()
print(type(t), t)

t = (1,)
print(type(t), t)

t = (1,2,3,4,5,"test",[])

print(t[0], t[1], t[2], t[:5:2])

# t[0] = 1.0
# t.append(1.0)

print(((1,2,3)+(4,5,6))*10)

print(len(t))
print(t.index("test"))

del t