def check_str(string):
    low_case = 0
    upper_case = 0
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i] == string[i].lower():
                low_case += 1
            else:
                upper_case += 1
    return print(f'{upper_case} upper case, {low_case} lower case')



def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



def get_ranges(list):
    final_list = []
    min = list[0]
    max = 0
    for i in range(len(list)):
        if list[i] == list[-1]:
            max = list[-1]
            if list[-1] - 1 == list[-2]:
                final_list.append(f'{min}-{max}')
            else:
                final_list.append(max)
        else:
            if list[i] + 1 == list[i+1]:
                max = list[i+1]
            else:
                if max == 0:
                    final_list.append(min)
                    min = list[i + 1]
                else:
                    final_list.append(f'{min}-{max}')
                    min = list[i+1]
                    max = 0
    return final_list



check_str(input('Enter a string to count amount of low and upper cases:\n'))
print(is_prime(int(input('Enter a number:\n'))))
print(*get_ranges([0, 1, 2, 3, 4, 7, 8, 10]), sep=', ')
print(*get_ranges([4, 7, 10]), sep=', ')
print(*get_ranges([2, 3, 8, 9]), sep=', ')

