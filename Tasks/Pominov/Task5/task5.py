############################################################################################
# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'

# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False

# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел,
# отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
############################################################################################


def check_str(string):
    upper_case, lower_case = 0, 0
    for i in string:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    print(f"{upper_case} upper case, {lower_case} lower case")


check_str('The quick Brown Fox')  # -> '3 upper case, 13 lower case'


def is_prime(nmbr):
    div_num = 0
    if nmbr < 2:
        return False
    elif nmbr == 2:
        return True
    else:
        for i in range(3, round(nmbr**0.5) + 1, 2):
            if div_num == 0:
                if nmbr % i == 0:
                    div_num += 1
        return (div_num == 0)


print(is_prime(787))  # -> True
print(is_prime(777))  # -> False


def get_ranges(lst):
    res = []
    pair = [lst[0], lst[0]]
    for i in lst[1:]:
        if i - pair[1] == 1:
            pair[1] = i
        else:
            res.append(pair)
            pair = [i, i]
    res.append(pair)
    res = list(
        map(lambda x: f"{x[0]}-{x[1]}" if x[0] != x[1] else f"{x[0]}", res))
    res = ", ".join(res)
    return res


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  # ->  "0-4, 7-8, 10"
print(get_ranges([4, 7, 10]))  # -> "4, 7, 10"
print(get_ranges([2, 3, 8, 9]))  # -> "2-3, 8-9"
