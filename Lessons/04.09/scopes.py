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

def test_global_operator():
    global x
    print(x)
    x = 'new global value from test_global_operator'
    print(x)

def test_global_value_creation():
    global new_global_variable
    new_global_variable = "new_global_variable"


x = 'global x value'
l = [1]

test_global_value()
test_local_value()
print(x)

test_global_list()
print(l)

test_arg(10)
print(x)

test_global_operator()
print(x)

test_global_value_creation()
print(new_global_variable)


def outer_func():
    x = "outer_func_value"
    def inner_func():
        nonlocal x
        x = "inner_func_value"
        print(x)
    inner_func()
    print(x)

outer_func()



