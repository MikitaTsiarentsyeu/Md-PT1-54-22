def sum(l):
    counter = 0
    for i in l:
        if isinstance(i, list):
            counter += sum(i)
        else:
            counter += i
    return counter     
 


def fib(n, i=0, j=1, b=True):
    if b == True:
        if n == 0:
            print("None")
        elif n == 1: 
            print(str(i)) 
        else:    
            print(str(i) + ',' + fib(n-1, j, i+j, False)) 
    else: 
        if n == 1:  
           return str(i) 
        return str(i) + ',' + fib(n-1, j, i+j, False)

print(sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))    
fib(5)
fib(10)






