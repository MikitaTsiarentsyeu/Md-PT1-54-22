#Реализовать функцию check_str которая получает на вход непустую строку 
# и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
#check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'

def check_str(row):
    upper_counter = 0
    lower_counter = 0
    for item in range(len(row)):
        if ord(row[item]) in range(97, 123):
            lower_counter += 1
        elif ord(row[item]) in range(65, 91):
            upper_counter += 1
        else:
            pass        
    print(f'{upper_counter} upper case, {lower_counter} lower case')        
