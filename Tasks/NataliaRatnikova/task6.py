def sum(l):
     i = 0
     final_sum = 0
     while i < len(l):
        if isinstance(l[i], list):
            final_sum += sum(l[i])
            i += 1
        else:
            final_sum += l[i]
            i += 1
     return final_sum

print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(n):
    if n == 0 or n == 1:
         return n
    else:    
        return fib(n-1) + fib(n-2)

def fib_list(n):
    l = []
    for i in range(n):
        l.append(fib(i))
    print(*l, sep=',')    

print(fib_list(5))

