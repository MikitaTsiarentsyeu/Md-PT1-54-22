def check_str(x):
    lower_counter = 0
    upper_counter = 0
    for i in x:
        if i.isalpha() and i.islower():
            lower_counter += 1
        elif i.isalpha() and i.isupper():
            upper_counter += 1
        else:
            continue
    print(f'{upper_counter} upper case, {lower_counter} lower case')


def is_prime(x):
    for i in range(2, x):
        if x % i == 0 and x > 0:
            return False
    return True


def get_ranges(lst):
    if len(lst) == 1:
        with open('list.txt', 'a+') as f:
            f.write(f'{lst[0]}')
            return
    for j in range(1, len(lst)):
        if lst[j] - lst[j - 1] == 1 and len(lst) > 2:
            continue
        else:
            with open('list.txt', 'a+') as f:
                f.write(f'{lst[0]}-{lst[j - 1]}' if lst[0]!=lst[j - 1] else f'{lst[0]}')
                f.write(', ')
            return get_ranges1(lst[j:])
    """why don't work the following code?"""
    # with open('list.txt', 'a+') as f:
    #     f.seek(0)
    #     print(f.read())


def get_ranges1(x):
    end_lst = []
    i = 1
    while len(x) != 1:
        if x[i] - x[i-1] == 1 and len(x[i:]) >=2:
            i += 1
        elif x[i] - x[i-1] != 1 and len(x[i:]) >=2:
            if x[0] != x[i-1]:
                end_lst.append(f'{x[0]} - {x[i-1]}')
            else:
                end_lst.append(f'{x[0]}')
            x = x[i:]
            i = 1
        elif x[i] - x[i - 1] == 1 and len(x[i:]) == 1:
            end_lst.append(f'{x[0]} - {x[i]}')
            break
        elif x[i] - x[i - 1] != 1 and len(x[i:]) == 1:
            end_lst.append(str(x[0]))
            end_lst.append(str(x[1]))
            break
    res_line = ', '.join(end_lst)




