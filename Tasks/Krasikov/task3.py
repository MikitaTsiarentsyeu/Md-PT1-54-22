
import datetime


d = {0:"двенадцать", 1:"один", 2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь",
    8:"восемь", 9:"девять", 10:"десять", 11:"одиннадцать", 12:"двенадцать"}
frst = {1:"одна", 2:"две", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одиннадцать", 12:"двенадцать", 13:"тринадцать", 14:"четырнадцать", 15:"пятнадцать", 16:"шестнадцать", 17:"семнадцать", 18:"восемнадцать", 19:"девятнадцать", 20:"двадцать", 21:"двадцать одна", 22:"двадцать две", 23:"двадцать три", 24:"двадцать четыре", 25:"двадцатьпять", 26:"двадцать шесть", 27:"двадцать семь",  28:"двадцать восемь", 29:"двадцать девять"}
sec = {31:"тридцать одна", 32:"тридцать две", 33:"тридцать три", 34:"тридцать четыре", 35:"тридцать пять", 36:"тридцать шесть", 37:"тридцать семь", 38:"тридцать восемь", 39:"тридцать девять", 40:"сорок", 41:"сорок одна", 42:"сорок две", 43:"сорок три", 44:"сорок четыре"} 
half = {1:"первого", 2:"второго", 3:"третьего", 4:"четвертого", 5:"пятого",
    6:"шестого", 7:"седьмого", 8:"восьмого", 9:"девятого",
    10:"десятого", 11:"одиннадцатого", 12:"двенадцатого"}
bez={1:"одной", 2:"двух", 3:"трёх", 4:"четырёх", 5:"пяти", 6:"шести", 7:"семи", 8:"восьми", 9:"девяти", 10:"десяти", 11:"одиннадцати", 12:"двенадцати", 13:"тринадцати", 14:"четырнадцати", 15:"пятнадцати"}




guess= input('Do you wanna watch online time or enter your time? Press Y, if - online time, and N, if your time: \n')
if guess == 'Y':
    time = datetime.datetime.now()
    time = time. strftime("%H:%M")
    print("Real time is", time)
    time = time.split(":") 
    hour = int(time[0])
    minute = int(time[1])
    if hour > 11:
        hour -= 12
        if minute == 0 and hour > 4:
            print(f'{d[(hour)]} часов ровно')
        elif minute == 0 and hour == 0:
            print(f'{d[(hour)]} часов ровно')
        elif minute == 0 and 1 < hour <= 4:
            print(f'{d[(hour)]} часа ровно')
        elif minute == 0 and hour == 1:
            print('Один час ровно')
        elif 4 < minute <= 20 or 24 < minute < 30 :
            print(f'{frst[minute]} минут {half[hour + 1]} часа')
        elif  1 < minute < 5 or 21 < minute < 25:
            print(f'{frst[minute]} минуты {half[hour + 1]} часа')
        elif minute == 1 or minute == 21:
            print(f'{frst[minute]} минута {half[hour+1]} часа')
        elif minute == 2 or minute == 3 or minute == 4:
            print(f'{frst[minute]} минуты {half[hour + 1]} часа')
        elif minute == 30:
            print(f'Половина {half[hour+1]} часа')
        elif minute == 31 and minute == 41:
            print(f'{sec[minute]} минута {half[hour + 1]} часа')
        elif 32 <= minute <= 34 or 42 <= minute <= 44:
            print(f'{sec[minute]} минуты {half[hour + 1]} часа')
        elif minute == 35 or minute == 40:
            print(f'{sec[minute]} минут {half[hour + 1]} часа')
        elif minute == 59:
            print(f'Без одной минуты {half[hour + 1]} часа')
        elif 45 <= minute < 59:
            minute = 60 - minute
            print(f'Без {bez[minute]} минут {half[hour + 1]} часа')            
    else:
        if minute == 0 and hour > 4:
                print(f'{d[(hour)]} часов ровно')
        elif minute == 0 and hour == 0:
            print(f'{d[(hour)]} часов ровно')
        elif minute == 0 and 1 < hour <= 4:
            print(f'{d[(hour)]} часа ровно')
        elif minute == 0 and hour == 1:
            print('Один час ровно')
        elif 4 < minute <= 20 or 24 < minute < 30 :
            print(f'{frst[minute]} минут {half[hour + 1]} часа')
        elif  1 < minute < 5 or 21 < minute < 25:
            print(f'{frst[minute]} минуты {half[hour + 1]} часа')
        elif minute == 1 or minute == 21:
            print(f'{frst[minute]} минута {half[hour+1]} часа')
        elif minute == 2 or minute == 3 or minute == 4:
            print(f'{frst[minute]} минуты {half[hour + 1]} часа')
        elif minute == 30:
            print(f'Половина {half[hour+1]} часа')
        elif minute == 31 and minute == 41:
            print(f'{sec[minute]} минута {half[hour + 1]} часа')
        elif 32 <= minute <= 34 or 42 <= minute <= 44:
            print(f'{sec[minute]} минуты {half[hour + 1]} часа')
        elif minute == 35 or minute == 40:
            print(f'{sec[minute]} минут {half[hour + 1]} часа')
        elif minute == 59:
            print(f'Без одной минуты {half[hour + 1]} часа')
        elif 45 <= minute < 59:
            minute = 60 - minute
            print(f'Без {bez[minute]} минут {half[hour + 1]} часа')            
elif guess == "N":
    time = input('Please enter your time in "HH:MM" format:\n')
    if time[2]!=":" or len(time) !=5:
        print('Validation error, follow default format of time')
    else:
        time = time.split(':')
        if not time[0].isdigit() or not time[1].isdigit():
            print('Try again, your enter isnt consist of digits')
        hour = int(time[0])
        minute = int(time[1])
        if hour > 24 or minute > 60:
            print('Validation error, max hour - 24 , max minutes - 60.')
        if hour > 11:
            hour -= 12
            if minute == 0 and hour > 4:
                print(f'{d[(hour)]} часов ровно')
            elif minute == 0 and hour == 0:
                print(f'{d[(hour)]} часов ровно')
            elif minute == 0 and 1 < hour <= 4:
                print(f'{d[(hour)]} часа ровно')
            elif minute == 0 and hour == 1:
                print('Один час ровно')
            elif 4 < minute <= 20 or 24 < minute < 30 :
                print(f'{frst[minute]} минут {half[hour + 1]} часа')
            elif  1 < minute < 5 or 21 < minute < 25:
                print(f'{frst[minute]} минуты {half[hour + 1]} часа')
            elif minute == 1 or minute == 21:
                print(f'{frst[minute]} минута {half[hour+1]} часа')
            elif minute == 2 or minute == 3 or minute == 4:
                print(f'{frst[minute]} минуты {half[hour + 1]} часа')
            elif minute == 30:
                print(f'Половина {half[hour+1]} часа')
            elif minute == 31 and minute == 41:
                print(f'{sec[minute]} минута {half[hour + 1]} часа')
            elif 32 <= minute <= 34 or 42 <= minute <= 44:
                print(f'{sec[minute]} минуты {half[hour + 1]} часа')
            elif minute == 35 or minute == 40:
                print(f'{sec[minute]} минут {half[hour + 1]} часа')
            elif minute == 59:
                print(f'Без одной минуты {half[hour + 1]} часа')
            elif 45 <= minute < 59:
                minute = 60 - minute
                print(f'Без {bez[minute]} минут {half[hour + 1]} часа')   
        else:
            if minute == 0 and hour > 4:
                print(f'{d[(hour)]} часов ровно')
            elif minute == 0 and hour == 0:
                print(f'{d[(hour)]} часов ровно')
            elif minute == 0 and 1 < hour <= 4:
                print(f'{d[(hour)]} часа ровно')
            elif minute == 0 and hour == 1:
                print('Один час ровно')
            elif 4 < minute <= 20 or 24 < minute < 30 :
                print(f'{frst[minute]} минут {half[hour + 1]} часа')
            elif  1 < minute < 5 or 21 < minute < 25:
                print(f'{frst[minute]} минуты {half[hour + 1]} часа')
            elif minute == 1 or minute == 21:
                print(f'{frst[minute]} минута {half[hour+1]} часа')
            elif minute == 2 or minute == 3 or minute == 4:
                print(f'{frst[minute]} минуты {half[hour + 1]} часа')
            elif minute == 30:
                print(f'Половина {half[hour+1]} часа')
            elif minute == 31 and minute == 41:
                print(f'{sec[minute]} минута {half[hour + 1]} часа')
            elif 32 <= minute <= 34 or 42 <= minute <= 44:
                print(f'{sec[minute]} минуты {half[hour + 1]} часа')
            elif minute == 35 or minute == 40:
                print(f'{sec[minute]} минут {half[hour + 1]} часа')
            elif minute == 59:
                print(f'Без одной минуты {half[hour + 1]} часа')
            elif 45 <= minute < 59:
                minute = 60 - minute
                print(f'Без {bez[minute]} минут {half[hour + 1]} часа')      
else:
    print('Please enter just "Y" or "N".')


