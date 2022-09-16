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



        
