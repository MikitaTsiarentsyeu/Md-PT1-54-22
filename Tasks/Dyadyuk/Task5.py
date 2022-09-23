def check_str(test_string) :
    res1 = 0
    res2 = 0
    for i in test_string :
        if i.isupper() :
            res1 += 1    
        if i.islower() :
            res2 += 1   
    print(res1, 'upper case,', res2,'lower case')

check_str('jthgtrjghjDFDFDghghgFDFDF')
   

def is_prime(x) :
    i = 2
    while i <= x**(0.5) :
        if x % i == 0 :
            return False
        i += 1
    if x > 1 :
        return True
        
print(is_prime(149))


def get_ranges(l) :
    result = []
    a = 0
    for i in range(len(l)) :
        if i != len(l)-1 and l[i+1] - l[i] == 1 :
            a += 1
        elif a == 0 :
            result.append(str(l[i]))
        else :
            result.append(str(l[i-a]) + '-' + str(l[i]))
            a = 0
    b = str(", ".join(result))
    return b
        
print(get_ranges([1,2,3,4,6,10,11,12,15,17]))


