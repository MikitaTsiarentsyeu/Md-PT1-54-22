def check_str(strng):
    l = list(strng)
    countlow = 0
    countup = 0
    for i in l:
        if i.isalpha() == True and i.islower() == True:
            countlow += 1
        if i.isalpha() == True and i.isupper() == True:
            countup += 1
    return print(f'{countup} upper case, {countlow} lower case')        

# s = input('Please enter your string\n')
# check_str(s) 

def is_prime(num):
    flag = True
    if num == 1:
        flag = False        
    for i in range(2,num):
        if num % i == 0:
            flag = False
            break
    return print(flag)

# n = int(input('Please enter the number\n'))    
# is_prime(n)

def get_ranges(l):
    lnew = []
    lsegm = []
    lsegm.append(l[0])
    for i in range(1, len(l)):
        if l[i] == lsegm[-1] + 1:
            lsegm.append(l[i])
            if i == len(l) - 1:
                lnew.append(lsegm)
                break
        else:
            lnew.append(lsegm)
            lsegm = []
            lsegm.append(l[i])
            if i == len(l) - 1:
                lnew.append(lsegm)
                break
    lstrgs = []        
    for k in range(len(lnew)):
        if len(lnew[k]) == 1:
            lstrgs.append(f'{lnew[k][0]}')
        else:
            lstrgs.append(f'{lnew[k][0]}-{lnew[k][-1]}') 
    return(print(*lstrgs, sep = ', '))      

    
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])