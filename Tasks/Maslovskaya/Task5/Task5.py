# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'

from turtle import st


def check_str(): 
    inp=input("Let's count the number of letters in uppercase and lowercase in you text.\nPlease, enter your text:\n")
    stroka = list(inp)
    u,l = 0,0
    if len(stroka)==0:
        print("You've entered nothing. Please, try again.")
        return check_str()
    else:
        for i in stroka:
            if i.isupper():   
                u+=1
            elif i.islower():
                l+=1
            else: 
                pass 
    print(f"There are {u} upper case and {l} lower case letters in your text.")


# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
# is_prime(787) -> True
# is_prime(777) -> False


def is_prime():
    chislo=input("Lets check if a number is prime ot not. Please, enter your number (use only positive numbers):\n")
    try: 
        chislo= int(chislo)
        if chislo==2 or chislo==3 or chislo==5 or chislo==7: 
            return True
        if chislo%2==0 or chislo<2: 
            return False
        for i in range(3, int(chislo**0.5)+1, 2):
            if chislo%i==0:
                return False
            else:
                return True
    except ValueError:
        print("Entered value isn't correct. Please, try again.")
        return is_prime()

# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"


def get_ranges(l):
    new_list = []
    counter = 0
    for i in range(len(l)):
        if i != len(l)-1 and l[i+1]-l[i] == 1:
            counter += 1
        elif counter == 0:
             new_list.append(str(l[i]))   
        else:
            new_list.append(f'{l[i-counter]}-{l[i]}')  
            counter = 0 
    string = f'"{", " .join(new_list)}"'
    return string



choice=input("Setect the function:\n 1) check_str()\n 2) is_prime()\n 3) get_ranges()\n")
if choice == '1':
    check_str()
elif choice == '2':
    a= is_prime()
    if a:
        print('The number is prime.')
    else:
        print('The number is not prime.')    
elif choice == '3':
    print("get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) is ", get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
    print("get_ranges([4,7,10]) is ", get_ranges([4,7,10]))  
    print("get_ranges([2, 3, 8, 9]) is", get_ranges([2, 3, 8, 9])) 
else:
    print('Bad choice. Restart the program.') 

    

    
 
        
   



 
