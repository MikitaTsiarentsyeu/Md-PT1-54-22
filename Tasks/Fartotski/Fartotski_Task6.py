sumNumber=0
def sumItems(newlist):
    for i in newlist:
        if isinstance(i,list):
            sumItems(i)
        else:
            global sumNumber
            sumNumber=sumNumber+i
    return sumNumber

print(sumItems([1, 2, [2, 4, [[7, 8], 4, 6]]]))


def fib(n):
    fib_list = []
    for i in range(n):
        if i==0:
            fib_list.append(i)
        else:
            if i==1:
                fib_list.append(i)
            else:
                fib_list.append(fib_list[i-1]+fib_list[i-2])
    print(fib_list)

fib(5)
fib(10)