def sum_digits(l) :
    res = 0
    for i in l :
        if not isinstance(i, list) :
            res += i 
        else :
            res += sum_digits(i)
    return res

print(sum_digits([1,[[2],5],5,[7,5,15,10,[20,[100]]]]))




