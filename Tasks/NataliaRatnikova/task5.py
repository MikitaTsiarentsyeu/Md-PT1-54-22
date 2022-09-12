def check_str(str):
    counter_up = 0
    counter_low = 0
    for i in str:
        if i == i.upper() and i != ' ':
            counter_up += 1
            print(counter_up)
        if i == i.lower() and i != ' ':
            counter_low += 1
    return(f'{counter_up} upper case, {counter_low} lower case')
   
print(check_str('Bla Bla bLa'))


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(25))


def get_ranges(l):
    final_list = str(l[0])
    for i in range(1, len(l)-1):  
        if l[i] - l[i-1] == 1:
            if l[i+1] - l[i] != 1:
               final_list += '-' + str(l[i]) 
        if l[i] - l[i-1] != 1:
            final_list += ', ' + str(l[i])
    if l[-1] - l[-2] != 1:
         final_list += ', ' + str(l[-1])
    else:
         final_list += '-' + str(l[-1])    
    return(final_list)

print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))