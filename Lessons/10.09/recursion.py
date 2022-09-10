def level1():
    print("level 1 is starting")
    level2()
    print("level 1 is done")

def level2():
    print("level 2 is starting")
    level3()
    print("level 2 is done")

def level3():
    print("level 3 is starting")
    level4()
    print("level 3 is done")

def level4():
    print("level 4 is starting")
    # level1()
    print("level 4 is done")

# level1()

def left():
    print("left")
    right()

def right():
    print("right")
    left()

# left()

# n = 0
# while True:
#     if n == 11:
#         break
#     n += 1
#     print(n)

def print_10_times(n=0):
    if n == 10:
        return
    n += 1
    print(n)
    print_10_times(n)

# print_10_times()

# 1! = 1
# 2! = 1*2
# 3! = 1*2*3
# 4! = 1*2*3*4
# 5! = 1*2*3*4*5

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(5))


def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n//10)

print(digit_sum(12345))

def digit_sum(n, i=0, res=0):
    n = str(n) if isinstance(n, int) else n
    if i == len(n):
        return res
    # res += int(n[i])
    return digit_sum(n, i+1, res+int(n[i]))

print(digit_sum(12345))
