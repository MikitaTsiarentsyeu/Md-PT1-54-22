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