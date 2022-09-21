# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков. 

# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

def sum_list(list):
    return sum(i if isinstance(i, int) else sum_list(i) for i in list)

print(sum_list([1, 2, [2, 4, [[7, 8], 4, 6]]]))

#2. Написать рекурсивную функцию для вычисления и вывода n первых чисел Фибоначчи.

# fib(5) -> 0, 1, 1, 2, 3
# fib(10) -> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def fib(n, list=[0, 1]):
    if n == 0:
        return ", ".join(str(i) for i in list)
    if len(list) == 2:
        return fib(n-3, list + [1])
    else:
        return fib(n-1, list + [list[-1] + list[-2]])
        
print(fib(10))