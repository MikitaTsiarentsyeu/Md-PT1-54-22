# l = []
# for i in range(10):
#     if i%2==0:
#         if i%4==0:
#             l.append(i)

# print(l)

l = [i*i for i in range(10)]
print(l)

l = [i*i for i in range(10) if i%2==0]
print(l)

l = [i*i for i in range(10) if i%2==0 if i%4==0]
print(l)

l = [i*i for i in range(10) if i%2==0 and i%4==0]
print(l)

d = {str(i):i*i for i in range(10)}
print(d)

l = [[1,2,3], [4,5,6], [7,8,9]]

for x in l:
    print(x)
    for y in x:
        print(y)

print([y for x in l for y in x], l)