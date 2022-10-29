# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

    


# 2. Написать рекурсивную функцию для вычисления и вывода n первых чисел Фибоначчи.
# Примеры вызова:


def fib_rec(number):
    if number == 0 or number == 1:
        return number
    else:
        return fib_rec(number - 1) + fib_rec(number - 2)


def fib(number):
    row = []
    for n in range(number):
        row.append(str(fib_rec(n)))
        row.append(', ')

    row[:] = row[:-1]
    print(''.join(row[:]))


fib(5)  # 0,1,1,2,3
fib(10)  # 0,1,1,2,3,5,8,13,21,34
