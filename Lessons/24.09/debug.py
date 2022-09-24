import time

def debug_info(f):
    def wrapper(*args, **kwargs):
        print(f.__name__)
        print(f"args: {','.join([f'{x}:{type(x)}' for x in args])}")
        print(f"kwargs: {','.join([f'{k}:{w}' for k, w in kwargs.items()])}")
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time() - start
        print(f"the result is {type(res)}:{res}")
        print(f"the execution took {end} seconds")
        return res, end
    return wrapper

@debug_info
def sum(a,b,c):
    return a+b+c

@debug_info
def double(*args, **kwargs):
    return [x*2 for x in args], [x*2 for x in kwargs.values()]

print(sum(2, 3, 4))
print(double(2,3,4,arg=5))