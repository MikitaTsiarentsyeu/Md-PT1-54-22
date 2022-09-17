def elements_sum(lists):
    summ = 0
    for i in lists:
        if type(i) is list:
            summ += elements_sum(i)
        else:
            summ += i
    return summ        
