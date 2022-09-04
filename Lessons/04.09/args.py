x, y = 2, 3

def test_sum(x, y):
    print(f"the x val is {x}, the y val is {y}")
    return x+y

test_sum('6', "test")
print(x, y)

def evaluate(val1=1, val2=2, val3=3):
    return val1+val2*val3

print(evaluate())
print(evaluate(1,2,3))
print(evaluate(val2=1, val3=2, val1=3))
print(evaluate(2, val3=3, val2=1))

def my_print(a, b, c, sep=',', end='.\n'):
    print(a, b, c, sep=sep, end=end)

my_print('one', 'two', 'three')
my_print('one', 'two', 'three', '_')
my_print('one', 'two', 'three', end=';\n')

def evaluate(a, b, action='+'):
    if action == '+':
        return a+b
    elif action == '*':
        return a*b
    elif action == '-':
        return a-b
    elif action == '/':
        return a/b

def print_coll(coll, reverse=False):
    coll = coll[::-1] if reverse else coll
    print(coll)

print_coll("test")
print_coll("test", True)

def sum(*args):
    print(args, type(args))
    res = 0
    for i in args:
        res += i
    return res

print(sum(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
print(sum(*[1,2,3,4,5,6,7,8,9,10]))

def my_print(*args, sep=',', end='.\n'):
    print(*args, sep=sep, end=end)

my_print(1,2,3,4,5,"test")

def name_pets(**kwargs):
    print(kwargs, type(kwargs))
    for k, v in kwargs.items():
        print(f"{k} the {v}")

d = {"zephirka":"dog", "simba":"cat"}
name_pets(zephirka='dog', simba='cat')
name_pets(**d)

def my_print(*args, **kwargs):
    if "sep" not in kwargs:
        kwargs['sep'] = ','
    if 'end' not in kwargs:
        kwargs['end'] = '.\n'
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,5,"test", sep=',', end='.\n')