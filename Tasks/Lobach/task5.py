def check_str(a):
    x = 0
    y = 0
    for i in a:
        if i.isupper():
            x += 1
        elif i.islower():
           y += 1      
    print(f'{x} upper case, {y} lower case')

check_str('The quick Brown Fox')

def is_prime(a):
    flag = True
    for i in range(2,a):
        if a % i == 0:
            flag = False
    print(flag)

is_prime(787)
is_prime(777)

def get_ranges(a):
    l = []
    my_list = []
    new_list = []
    string = ''
    
    for i in range(len(a)-1):
        
        if a[i+1] - a[i] >= 2:
            my_list.append(a[i+1]) #  my_list contains 'stairs': 7 and 10

    for j in my_list:
        x = a.index(j)
        l.append(x) #  l contains indices of 'stairs': 5 and 7 
    
    for s in range(0,len(l)+1):                               

        if s == 0:
            p = a[s:l[s]]
        if s == len(l):
            p = a[l[s-1]:a[-1]]        
        if s != 0 and s != len(l):
            p = a[l[s-1]:l[s]]
       
        new_list.append(p)

    for y in new_list:

        if y == new_list[-1] and len(y) > 1:
            string += f'{y[0]}-{y[-1]}'
        elif y == new_list[-1] and len(y) == 1:
            string += f'{y[0]}'
        elif len(y) == 1:
            string += f'{y[0]}, '
        else: string += f'{y[0]}-{y[-1]}, '

    print(string)

get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])

