# 1. Написать рекурсивную функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34

def sum_of_list_elements(l):
    i=0
    itog_sum=0
    while i < len(l):
        if isinstance(l[i], list):
            itog_sum += sum_of_list_elements(l[i])
            i+=1
        else:
            itog_sum += l[i]
            i+=1
    return itog_sum

print(sum_of_list_elements([1, 2, [2, 4, [[7, 8], 4, 6]]]))  

# 2. Написать рекурсивную функцию для вычисления и вывода n первых чисел Фибоначчи.
# Примеры вызова: 
# fib(5) -> 0,1,1,2,3
# fib(10) -> 0,1,1,2,3,5,8,13,21,34

def num_fibannachi(num):
    if num in (0, 1):
        return num    
    else:
        return num_fibannachi(num - 1) + num_fibannachi(num - 2)

def fibannachi(num):
    print(*[num_fibannachi(i) for i in range(num)], sep=",")

fibannachi(5)  
fibannachi(10)  
