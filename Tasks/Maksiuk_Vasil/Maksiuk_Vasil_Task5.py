#1
def check_str(x):
    s = len((str(x)).replace(' ', ''))
    Up = (sum(i.isupper() for i in x))
    low = s - Up
    print(f"{Up} upper case, {low} lower case")
    return

check_str('The quick Brown Fox')


#2
def is_prime(x):
    k = 0
    for i in range(2, x):    
        if (x % i == 0):
            k = k+1
    if (k == 0):
        print(True)
    else:
        print(False) 
    return

is_prime(787)
is_prime(777)


#3
def get_ranges(x):
    l = str(x[0])
    for i in range(1, len(x)-1):
        if x[i]-x[i-1] != 1:
            l += ", " + str(x[i])
        elif x[i]-x[i-1] == 1 and x[i+1]-x[i] > 1:
            l += "-" + str(x[i])
        else: 
            False 
    if x[-1] - x[-2] > 1:
        l += ", " + str(x[-1])
    else:
        l += "-" + str(x[-1])       
    return print(l)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) # ->  "0-4, 7-8, 10"
get_ranges([4,7,10]) # -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  # -> "2-3, 8-9"
