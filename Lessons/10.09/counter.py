
# def counter(n): DEPENDENT COUNTERS
#     global counter_base
#     counter_base = n
#     def inner():
#         global counter_base
#         counter_base += 1
#         return counter_base
#     return inner

def counter(n):
    def inner():
        nonlocal n
        n += 1
        return n
    return inner

from_10 = counter(10)
from_100 = counter(100)

print(from_10())
print(from_10())
print(from_10())
print(from_100())
print(from_100())
print(from_100())