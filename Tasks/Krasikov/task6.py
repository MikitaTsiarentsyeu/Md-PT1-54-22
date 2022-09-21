def sum1(lst):
    total = 0
    for elem in lst:
        if (type(elem) == type([])):
            total += sum1(elem)
        else:
            total += elem
    return total

print(sum1([[1, 2], [3, 4]]))

def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    li = fib(n-1)
    li.append(li[-1] + li[-2])
    return li

print(fib(5))




