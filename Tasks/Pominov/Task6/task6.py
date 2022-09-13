########################################################################################
# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

# 2. Написать рекурсивную функцию для вычисления и вывода n первых чисел Фибоначчи.
# Примеры вызова:
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34
########################################################################################


def list_sum(lst):
    return sum(map(lambda x: list_sum(x) if type(x) == list else x, lst))


print(list_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))  # -> 34


def fib(n):

    def fib_number(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib_number(n - 1) + fib_number(n - 2)

    print(*[fib_number(i) for i in range(n)], sep=",")


fib(5)  # -> 0,1,1,2,3
fib(10)  # -> 0,1,1,2,3,5,8,13,21,34


# quick fibonacci list without recursion
def quick_fib(n, lst=[]):
    for i in range(n):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        else:
            lst.append(lst[i - 1] + lst[i - 2])
    print(*lst, sep=",")


quick_fib(200)
