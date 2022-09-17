def fib(n, output = True):
    if n in range (0,2):
        return n
    f1 = fib(n-1, output)
    if output:
        print(f1)
    return f1 + fib(n-2, False)
          