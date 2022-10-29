# Task 5.1
your_text = 'The quick Brown Fox'

def check_str(your_text):
    upper_case, lower_case = 0, 0

    for character in your_text:
        if characte r.isupper():
            upper_case+=1
        elif character.islower():
            lower_case+=1
    print(f'{upper_case} upper case, {lower_case} lower case')

check_str(your_text)

# Task 5.2

your_number = int(input('write a number: '))

def is_prime():
    number = 2
    if your_number > 1:
        while number < your_number:
            if your_number%number == 0:
                return False
            number+=1
        return True
    else:
        return False

print(is_prime())


# Task 5.3

def get_ranges(sort):
    i=0
    ll = []
    current_number = sort[i]

    while i < len(sort):
        if sort[i] == current_number:
           ll.append(current_number)
           i+=1
           current_number += 1
        else:
            ll.append('-')
            while sort[i] != current_number:
                current_number += 1

    sort.clear()
    i = 0
    stop = 0
    step = 0

    while i < len(ll):
        if ll[i] != len(ll):
            if ll[i] == '-':
                if ll[stop] == ll[i-1]:
                    sort.append(f'{ll[stop]}')
                    step = 0
                else:
                    sort.append(f'{ll[stop]} - {ll[i-1]}')
                stop = i+1
            elif ll[i] == ll[-1]:
                if step < 2:
                    sort.append(f'{ll[i]}')
                else:
                    sort.append(f'{ll[stop]} - {ll[i]}')
                stop = i+1
            step+=1
        else:
            sort.append(ll[i])

        i+=1

    i = 0
    out_string = ''

    for p in sort:
        if i != len(sort)-1:
            out_string += str(p) + ', '
        else:
            out_string += str(p)
        i += 1

    print(out_string)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) # 0 - 4, 7 - 8, 10
get_ranges([4,7,10]) # 4, 7, 10
get_ranges([2, 3, 8, 9]) # 2 - 3, 8 - 9