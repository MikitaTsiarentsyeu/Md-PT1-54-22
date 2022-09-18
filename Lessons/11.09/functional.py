from functools import reduce

def apply(l, f, i=0):
    if i == len(l):
        return
    f(l[i])
    apply(l, f, i+1)

l = [1,2,3,4,5,6,7,8]

apply(l, print)

def print_sq(num):
    print(num*num)

print_sq = lambda x: print(x*x)
print_sq(10000000)

apply(l, lambda x: print(x*x))

# def sum(x, y):
#     return x+y

lambda x, y: x+y
lambda x: print(x**2 + 10)


test_str = "Abc Aac aaa test kit kot"
print(sorted(test_str.split()))
print(sorted([x.upper() for x in test_str.split()]))
print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

l = [("one", 1), ("two", 2), ("three", 3)]
print(sorted(l))
print(sorted(l, key=lambda x: x[1]))

d = {"one":1, "two":2, "three":3}
print(sorted(d))
print(sorted(d.items(), key=lambda x: x[1]))

l = [-1,0,1,2,3,4,5,6,7,8,9,10]
map_obj = map(print, l)
print(map_obj, type(map_obj))
# for i in map_obj:
#     pass

# print(list(map(lambda x: chr(x*10), l)))
print(list(map(str, l)))

print(list(filter(lambda x: x>4, l)))
print(list(filter(lambda x: x, l)))

print(list(map(lambda x: chr(x*10), filter(lambda x: x>0, l))))

# print(sum(map(int, str(12345))))

new_l = []

for i in l:
    if i > 0:
        new_l.append(chr(i*10))

print(new_l)

print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: x+y, [1,2,3,4,5]))
print(reduce(lambda x, y: f"{x}-{y}", [1,2,3,4,5]))
print(reduce(lambda x, y: x if x>=y else y, l))

l = ['1', '11', '12', '22', '2', '13', '30', '33'] 

print(sorted(filter(lambda x: int(x) % 2 == 0, l), key=int))