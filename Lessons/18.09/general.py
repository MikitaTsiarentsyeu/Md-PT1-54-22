# import additional as addtnl
# from additional import global_value as gv, print_global_value

x = "very important value"

print(x)

from additional import *

print(x)

# additional = "some additional value"

# print(additional)

print(global_value)

global_value.append(10)

print_global_value()