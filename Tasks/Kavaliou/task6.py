#сума элементаў спісу
def listssum(list):
    result = 0
    for i in list:
        if isinstance(i, int):
            result += i
        else:
            result += listssum(i)
    return result

print(listssum([1, 2, [2, 4, [[7, 8], 4, 6]]]))

#Фібаначы
def fibbonachi(num):
    while num > 0:
        if num == 1:
            return [0]
        elif num == 2:
            return [0, 1]
        list = fibbonachi(num-1)
        list.append(list[-1] + list[-2])
        return list

print(fibbonachi(5))
