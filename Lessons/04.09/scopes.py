# for i in range(10):
#     i+=1

# [i for i in range(10)]

# print(i)

def test_global_value():
    print(x)

def test_local_value():
    x = "local x value"
    print(x)

def test_global_list():
    # l = [10]
    l[0] += 2

def test_arg(x):
    print(x)
    x = "test local value"

x = 'global x value'
l = [1]

test_global_value()
test_local_value()
print(x)

test_global_list()
print(l)

test_arg(10)
print(x)