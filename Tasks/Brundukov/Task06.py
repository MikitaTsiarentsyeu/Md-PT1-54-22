def sum_digits(l) :
    res = 0
    for i in l :
        if not isinstance(i, list) :
            res += i 
        else :
            res += sum_digits(i)
    return res

print(sum_digits([1,[[2],5],5,[7,5,15,10,[20,[100]]]]))



def fib(n) : 
    result = []  
    def fib1(n) :
        if n == 1 :
            return 0
        if n == 2 :
            return 1
        else :
            return fib1(n - 1) + fib1(n - 2)
    for i in range(1, n + 1) :
        result.append(fib1(i))
    return str(result).strip('[]') 

print(fib(12))
