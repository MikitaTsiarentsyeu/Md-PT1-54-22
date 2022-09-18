def check_str(s):
   counter_upper=0
   counter_lower=0
   for i in s:
       if i.isupper():
           counter_upper+=1
       if i.islower():
           counter_lower+=1
   print(f"{counter_upper} upper case, {counter_lower} lower case")

check_str("The quick Brown Fox")

def is_prime(x):
    counter = 0
    for i in range(2, x):
        if (x % i == 0):
            counter+=1
    if (counter <= 0):
        print("True")
    else:
        print("False")

is_prime(787)
is_prime(777)


def get_ranges(list):
    listLength = len(list)
    rangeLength = 1
    new_list = []

    for i in range(1, listLength + 1):
        if (i == listLength or list[i] - list[i - 1] != 1):

            if (rangeLength == 1):
                new_list.append(f'{list[i - rangeLength]}')
            else:
                temp = (f'{list[i - rangeLength]}-{list[i - 1]}')
                new_list.append(temp)

            rangeLength = 1

        else:
            rangeLength += 1

    return print(new_list)


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])