def check_str(s):
    Ucounter = 0
    Lcounter = 0
    for i in s:
        if i.islower() and i.isalpha():
            Lcounter += 1
        if i.isupper() and i.isalpha():
            Ucounter += 1
    return '{0} upper case, {1} lower case'.format(Ucounter, Lcounter)



def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True



def get_ranges(List):
    String = str(List[0])
    for i in range(1, len(List)-1):
        if List[i]-List[i-1] == 1 and List[i+1]-List[i] != 1:
            String += "-" + str(List[i]) 
        if List[i]-List[i-1] != 1:
            String += ", " + str(List[i])
    if List[-1]-List[-2] == 1:
        return String + "-" + str(List[-1])
    else:
        return String + ", " + str(List[-1])




    
    
