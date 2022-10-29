def func_sum(n, res=0):
    
    if isinstance(n, list):

        for i in n:
            if isinstance(i, int):
                res += i
            else: res += func_sum(i)
    return res

print(func_sum([1, 2, [2, 4, [[7, 8], 4, 6]]]))


# def fib(n):
#     def fib_range(a):
#         if a <= 1:
#             return a
#         else: return fib_range(a-1) + fib_range(a-2)
    
#     for i in range(n):
#         if i != n-1:
#             print(fib_range(i), end=',')
#         else: print(fib_range(i), end='')
    
# #fib(5)
# fib(10)
    


