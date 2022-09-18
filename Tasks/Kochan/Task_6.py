def fib(n):
    lst = []

    def fib_print(n):
        while n > 0:
            if n == 1:
                return 0
            if n == 2:
                return 1
            else:
                return fib_print(n - 1) + fib_print(n - 2)
    for i in range(1, n + 1):
        lst.append(fib_print(i))
    print(','.join(map(str, lst)))


def sum_list(lst):
    end_sum = 0
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            end_sum += sum_list(lst[i])
            i += 1
        else:
            end_sum += lst[i]
            i += 1
    return end_sum



