# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

def sum_elem(List):
    Sum = 0
    for i in List:
        if isinstance(i, list):
            Sum += sum_elem(i)
        else:
            Sum += i
    return Sum

# 2. Написать рекурсивную функцию для вычисления и вывода n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

def Fib(n, Answer = [0, 1]):
    if n == 1:
        return str(Answer[0])
    if n == 2:
        return str(Answer).replace('[','').replace(']','').replace(' ','')
    else:
        return Fib(n-1, Answer + [Answer[-1]+Answer[-2]])