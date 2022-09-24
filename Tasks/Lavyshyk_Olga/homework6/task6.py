a = [1, 2, [2, 4, [[7, 8], 4, 6]]]

def rec(spisok):
    summ = 0
    for i in spisok:

        if type(i) != list:
            summ = i + summ
        else:
            summ = summ + rec(i)

    return summ
summ = rec(a)
print(f"Cумма элементов - {summ}")



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

n = int(input('Enter a number: '))

fibo_series = []

for i in range(0, n):
    fibo_series.append(fibonacci(i))

print(*fibo_series, sep=",")

fibonacci(n)