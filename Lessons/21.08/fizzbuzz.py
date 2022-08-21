#Вывести все числа от 1 до 100
#Вместо чисел, кратных 3, выводить FIZZ
#Вместо чисел, кратных 5, выводить BUZZ
#Вместо чисел, кратных 3 и 5, выводить FIZZBUZZ


for i in range(1, 101):
    res = ""
    if i % 3 == 0:
        res += "FIZZ"
    if i % 5 == 0:
        res += "BUZZ"
    if res == "":
        res = i
    print(res)


print([("FIZZ"*(i % 3 == 0))+("BUZZ"*(i % 5 == 0)) or i for i in range(1, 101)])