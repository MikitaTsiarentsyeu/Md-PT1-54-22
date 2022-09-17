#1 Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре. check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'

def check_str(string):
    up = 0
    low = 0
    for i in string:
        if i.isupper():
            up += 1
        if i.islower():
            low += 1
    return f'{up} upper case, {low} lower case'

print(check_str('The quick Brown Fox'))

#2 Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.is_prime(787) -> True, is_prime(777) -> False

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(is_prime(777))

#3 Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков. get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10". get_ranges([4,7,10])  -> "4, 7, 10". get_ranges([2, 3, 8, 9])  -> "2-3, 8-9".

def get_ranges(list):
    res = str(list[0])
    for i in range(1, len(list)-1):
        if list[i] - list[i-1] == 1:
            if list[i+1] - list[i] != 1:
                res += '-' + str(list[i])
        elif list[i] - list[i-1] != 1:
            res += ', ' + str(list[i])
    if list[-1] - list[-2] != 1:
        res += ', ' + str(list[-1])
    else:
        res += '-' + str(list[-1])
    return res

print(get_ranges([4, 7, 10]))

