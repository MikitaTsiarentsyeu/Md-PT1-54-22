def simpliest_func():
    print("I'm very simple")

simpliest_func()
simpliest_func()
simpliest_func()
simpliest_func()
simpliest_func()

def sum(a, b, c):
    return a+b+c

print(sum(2, 3, 5))
print(sum(20, 33, 55))

print(type(sum), sum)

def test_args(arg1, arg2):
    print(f"the arg1 value is {arg1}, the arg2 value is {arg2}")

test_args(2,3)
test_args(3,2)

def test_int(x):
    print(id(x))
    x += 2
    print(id(x))

x_val = 3
print(id(x_val))
test_int(x_val)
print(id(x_val))

def test_list(x):
    print(id(x))
    x[0] += 2
    print(id(x))

x_val = [3]
print(id(x_val))
test_list(x_val)
print(id(x_val))
print(x_val)

def test_return(x):
    if x:
        return True
    else:
        return False
    print("after return")

test_return("")
x = simpliest_func()
print(x, type(x))
