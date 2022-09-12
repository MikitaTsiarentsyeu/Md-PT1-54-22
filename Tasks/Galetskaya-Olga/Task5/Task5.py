def check_str(line):
    upper_count = 0
    lower_count = 0
    for el in line:
        if el.isalpha():
            if el.istitle():
                upper_count += 1
            else:
                lower_count += 1
    return f'{upper_count} upper case, {lower_count} lower case' 

print(check_str('The quick Brown Fox'))  #Проверка


def is_prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, num // 2 + 1):
            if num % i == 0:        
                return False
        return True

print(is_prime(787), is_prime(777))  #Проверка


def get_ranges(lst):
    result = []
    start = lst[0]
    for i in range(1, len(lst)):
        if lst[i] - 1 != lst[i - 1]:
            end = lst[i - 1]
            if end != start:
                result.append(f'{start}-{end}')
            else:
                result.append(str(end))
            start = lst[i]
        end = lst[i]
    if end != start:
        result.append(f'{start}-{end}')
    else:
        result.append(str(end))            
    result = ', '.join(result)
    
    return result         

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))  #Проверка
print(get_ranges([4,7,10]))
print(get_ranges([2, 3, 8, 9]))

