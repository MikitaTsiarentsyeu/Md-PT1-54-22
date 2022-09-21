# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
def sum(data):
    counter = 0
    for i in data:
        if isinstance(i, list):
            counter += sum(i)
        else:
            counter += i
    return counter     
print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))

# 2. Написать рекурсивную функцию для вычисления и вывода n первых чисел Фибоначчи.
def fibonacci(n):
    if n < 2:
         return n
    else:    
        return fibonacci(n-1) + fibonacci(n-2)
def fib(n):
    list = []
    for i in range(n):
        list.append(fibonacci(i))
    print(*list, sep=',')    
print(fib(5))
print(fib(10))