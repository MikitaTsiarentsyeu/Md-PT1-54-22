#Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True,
#если число является простым, и False, если нет.
 
def is_prime(number):
    if number == 1:
        return False
    divider = 2
    while divider < number // 2 + 1:
        if number % divider == 0:
            return False
        divider += 1    
    return True        
    