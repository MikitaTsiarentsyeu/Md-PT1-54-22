
from datetime import datetime

def show_info(f):
    def wrapper():
        print("the function was started")
        f()
        print("the function was finished")
    return wrapper

def do_twice(f):
    def wrapper():
        f()
        f()
    return wrapper

@do_twice
@show_info
def print_hello():
    print("hello!")

@show_info
@do_twice
def show_time():
    print(datetime.now())

# print_hello = show_info(print_hello)
# print_hello()

# show_time()
# show_time = show_info(show_time)
show_time()