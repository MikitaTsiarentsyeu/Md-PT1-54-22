string = 'The quick Brown Fox'
def check_str(string):       
    counter1 = 0
    counter2 = 0
    for i in string:
        if i.isupper():
            counter1 += 1
        elif i.islower():
            counter2 += 1
        else: 
            pass
    print('Upper symbols:', counter1, 'Lower symbols:',counter2)


def is_prime(n):
    counter = 0
    d = n // 2 + 1 
    for i in range(2, d):
        if n % i == 0:
            counter +=1
    if counter <= 0:
        print('True. The number is prime.')
    else:
        print('False. The number is NOT prime.')


def get_ranges(l):
    new_list = []
    counter = 0
    for i in range(len(l)):
        if i != len(l)-1 and l[i+1]-l[i] == 1:
            counter += 1
        elif counter == 0:
             new_list.append(str(l[i]))   
        else:
            new_list.append(f'{l[i-counter]}-{l[i]}')  
            counter = 0 
    string = f'"{", " .join(new_list)}"'
    return string



            