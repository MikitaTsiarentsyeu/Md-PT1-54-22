def listsum(l):
    total = 0
    for i in l:
        if isinstance(i, list):
            total += listsum(i)            
        elif isinstance(i, int):
            total += i
    return total        
     
# l = [1, 2, [2, 4, [[7, 8], 4, 6]]]
# print(listsum(l)) 

def fib(n,a=0,b=1,l=[0]):
    if n == 1:
        return l        
    else:
        l.append(a+b)
        return fib(n-1,a+b,a,l)
        
print(*fib(10), sep = ', ')






  