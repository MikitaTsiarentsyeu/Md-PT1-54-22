def get_list_sum(lst, a=[]):
    for el in lst:
        if type(el) != list:
            a.append(el)
        else:
            get_list_sum(el) 
    return(sum(a))


print(get_list_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))  #ПРОВЕРКА



def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:    
        return fib(n-1) + fib(n-2)

def fibonacci(n, a=[]):
    for i in range(n):
        a.append(fib(i))
    print(*a, sep=',')    
    
fibonacci(5)  #ПРОВЕРКА
fibonacci(10)  #ПРОВЕРКА


