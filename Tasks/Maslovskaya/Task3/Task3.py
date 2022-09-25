# Реализовать:
# 1.текстовый вывод текущего времени
# 2.текстовый вывод времени, введённого с консоли (пользователь должен вводить данные в формате hh:mm).
# Дать пользователю возможность выбрать режим работы программы, время выводить числительными на русском языке.

# Для получения текущего времени использовать модуль datetime.

# min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
# min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
# min == 30: половина такого-то (15:30 - половина четвёртого)
# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
# min >= 45 без min такого-то (08:54 - без шести минут девять)

import datetime

minutes={1:"одна", 2:"две", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одиннадцать", 12:"двенадцать",
13:"тринадцать", 14:"четырнадцать", 15:"пятнадцать", 16:"шеснадцать", 17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать", 20:"двадцать", 30:"тридцать", 
40:"сорок", 50:"пятьдесят"}

hours_ogo={12:"первого", 1:"второго", 2:"третьего", 3:"четвертого", 4:"пятого", 5:"шестого", 6:"седьмого", 7:"восьмого", 8:"девятого", 9:"десятого", 
10:"одиннадцатого", 11:"двенадцатого"}

minutes_ti={59:"одной", 58:"двух", 57:"трех", 56:"четырех", 55:"пяти", 54:"шести", 53:"семи", 52:"восьми", 51:"девяти", 50:"десяти", 
49:"одиннадцати", 48:"двенадцати", 47:"тринадцати", 46:"четырнадцати", 45:"пятнадцати"}

hours={1:"час", 2:"два", 3:"три", 4:"четыре", 0:""}

addit={'h':"часов ровно",'m':"минут",'half':"половина", 'm_a':"а", 'm_i':"ы",'without':"без",'equivalent':"ровно",'h_a':"часа"}

m_a = [1,31,41,21]
m_i = [2,3,4,32,33,34,42,43,44,22,23,24]

def validation():
    entered_time = input("Please, enter your own time in the format 'hh:mm':\n")
    if len(entered_time)==5:
        if entered_time[2]==":":
            if entered_time[:2].isdigit() and entered_time[3:5].isdigit():
                if int(entered_time[0:2])<0 or int(entered_time[0:2])>23:
                    print("Hours range too big. Please, try again.")
                    return validation()
                elif int(entered_time[0:2])>=0 and int(entered_time[0:2])<=23:
                    if int(entered_time[3:5])<0 or int(entered_time[3:5])>60: 
                        print("Minutes range too big. Please, try again.")
                        return validation()
                    elif int(entered_time[3:4])>=0 and int(entered_time[3:4])<=60: 
                        return datetime.datetime.strptime(entered_time, "%H:%M").strftime("%I:%M").split(":")

    print("Entered value isn't correct. Let's try again.")
    return validation()

def customer_mode():
    mode = input("Please, make your choice. Enter 's' to show you system time or 'm' if you want to enter your own:\n")
    if mode == "s":
        entered_time = datetime.datetime.now().strftime("%I:%M").split(":")
        return entered_time
    elif mode == "m":
        entered_time = validation()
        return entered_time
    print("Entered value isn't correct. Let's try again.")
    return customer_mode()

def zero(*args):
    if entered_minutes==0:
        if entered_hours in hours:
            print(hours[entered_hours], addit['h_a'], addit['equivalent'])
        else:
            print(minutes[entered_hours], addit['h'])
   
def first_half(*args):      
    if entered_minutes in m_a:
        res=addit['m_a']
    elif entered_minutes in m_i:
        res=addit['m_i']
    else:
        res=""
    if 0 < entered_minutes <= 20:
        print(minutes[entered_minutes], addit['m']+res, hours_ogo[entered_hours])
    elif (20 < entered_minutes < 30) or (30 < entered_minutes < 45):
        print(minutes[entered_minutes//10*10], minutes[entered_minutes%10], addit['m']+res, hours_ogo[entered_hours])

def half(*args):     
    if entered_minutes==30:
        print(addit['half'], hours_ogo[entered_hours])

def second_half(*args):  
    if entered_minutes >= 45:
        if entered_hours==12:
            if entered_minutes==59:
                print(addit['without'], minutes_ti[entered_minutes], addit['m']+addit['m_i'],hours[1])
            else:    
                print(addit['without'], minutes_ti[entered_minutes], addit['m'],hours[1])
        elif entered_hours in hours:
            if entered_minutes==59:
                print(addit['without'], minutes_ti[entered_minutes], addit['m']+addit['m_i'],hours[entered_hours+1])
            else:    
                print(addit['without'], minutes_ti[entered_minutes], addit['m'],hours[entered_hours+1])
        else:
            if entered_minutes==59:
                print(addit['without'], minutes_ti[entered_minutes], addit['m']+addit['m_i'],minutes[entered_hours+1])
            else:       
                print(addit['without'], minutes_ti[entered_minutes], addit['m'],minutes[entered_hours+1])

print("Hello, I will show you time in russian language. You can choose system time or enter your own. Let's start!")

entered_time = []
entered_time = customer_mode()
entered_hours = int(entered_time[0])
entered_minutes = int(entered_time[1])

second_half(half(first_half(zero())))