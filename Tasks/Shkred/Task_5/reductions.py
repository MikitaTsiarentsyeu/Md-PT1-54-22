#Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
#отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.

def get_ranges(collection):
    value = 0
    length = len(collection)
    folded_string, temp_row = '', ''
    while length:
        if collection[value] == collection[-1]:
            temp_row += str(collection[value])
            folded_string += temp_row
            break   
        elif collection[value + 1] - collection[value] > 1:
            temp_row +=  str(collection[value]) + ', ' 
            folded_string += temp_row
            temp_row = ''
        else:  
            if len(temp_row) == 0:
                temp_row += str(collection[value]) + '-'       
        value += 1        
        length -= 1
    print(folded_string)
