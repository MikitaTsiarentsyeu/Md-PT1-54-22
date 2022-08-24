from datetime import datetime

Base = {1: ('один', 'первого', 'одна', 'одной'), 2: ('два', 'второго', 'две', 'двух'), 3: ('три', 'третьего', 'трёх', 'трёх'), 4: ('четыре', 'четвертого', 'четырёх', 'четырёх'),
 5: ('пять', 'пятого', 'пяти'), 6: ('шесть', 'шестого', 'шести'), 7: ('семь', 'седьмого', 'семи'), 8: ('восемь', 'восьмого', 'восьми'), 9: ('девять', 'девятого', 'девяти'),
  10: ('десять', 'десятого', 'десяти'), 11: ('одиннадцать', 'одиннадцатого', 'одиннадцати'), 12: ('двенадцать', 'двенадцатого', 'двенадцати') , 13: ('тринадцать', '', 'тринадцати'),
   14: ('четырнадцать', '', 'четырнадцати'), 15: ('пятнадцать', '', 'пятнадцати'), 16: ('шестнадцать', 'шестнадцати'), 17: ('семнадцать', 'семнадцати'), 18: ('восемнадцать', 'восемнадцати'), 19: ('девятнадцать', 'девятнадцати'), 20: ('двадцать', 'двадцати'), 30: ('тридцать', 'тридцати'), 
   40: ('сорок', 'сорока'), 50: ('пятьдесят', 'пятидесяти')}

while True:
    user_value = input('Вы хотите 1:узнать текущее время или 2:проверить часы? Введите 1 или 2.\n')

    if user_value == '1':
        usertime = str(datetime.now().strftime("%H:%M"))
        print(usertime)
        break            
    if user_value == '2':
        usertime = input('Введите текущее время в формате чч:мм\n')

        if len(usertime) != 5 or usertime[2] != ':':
            print('Вы ввели время неверно, введите еще раз.\n')
            continue
        
        failed = False
        for el in usertime.split(':'):
            if  not el.isdigit():
                failed = True
            break
        if failed:
            print('Вы ввели время неверно, введите еще раз.\n')
            continue

        if int(usertime[:2]) > 24 or int(usertime[3:]) > 59:
            print('Вы ввели время неверно, введите еще раз.\n')
            continue
        
    elif user_value !='1' or user_value !='2':
        print('Вы сделали неверный выбор. Попробуйте ещё раз.\n')
        continue
    break

tup_hours = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
hours, minutes = usertime.split(':')
if int(hours) > 12: 
    hours = int(hours) - 12
else:
    hours = int(hours)    
minutes = int(minutes) 

if minutes == 0:
    if hours == 1: 
        print(f'{Base[hours][0]} час ровно')
    elif hours in (2, 3, 4):
        print(f'{Base[hours][0]} часа ровно')
    elif hours in (5, 6, 7, 8, 9, 10, 11):
        print(f'{Base[hours][0]} часов ровно')
    elif hours == 0 or hours == 12:
        print(f'{Base[12][0]} часов ровно')    

elif minutes == 1:
    if hours == 12 or hours == 0: 
        print(f'{Base[minutes][2]} минута {Base[1][1]}')
    elif hours in tup_hours:
        print(f'{Base[minutes][2]} минута {Base[hours+1][1]}')

elif minutes >= 2 and minutes < 5:
    if hours == 12 or hours == 0: 
        print(f'{Base[minutes][0]} минуты {Base[1][1]}')
    elif hours in tup_hours:
        print(f'{Base[minutes][0]} минуты {Base[hours+1][1]}')

elif minutes >= 5 and minutes < 21:
    if hours == 12 or hours == 0: 
        print(f'{Base[minutes][0]} минут {Base[1][1]}')
    elif hours in tup_hours:
        print(f'{Base[minutes][0]} минут {Base[hours+1][1]}')        

elif minutes in (21, 31, 41, 51):
    if hours == 12 or hours == 0: 
        print(f'{Base[minutes // 10 * 10][0]} {Base[minutes][2]} минута {Base[1][1]}')
    elif hours in tup_hours:
        print(f'{Base[minutes // 10 * 10][0]} {Base[minutes][2]} минута {Base[hours+1][1]}')

elif minutes > 21 and minutes < 30:
    if hours == 12 or hours == 0: 
        print(f'{Base[minutes // 10 * 10][0]} {Base[minutes % 10][0]} минут {Base[1][1]}')
    elif hours in tup_hours:
        print(f'{Base[minutes // 10 * 10][0]} {Base[minutes % 10][0]} минут {Base[hours+1][1]}')

elif minutes == 30:
    if hours == 12 or hours == 0: 
        print(f'половина {Base[1][1]}')
    elif hours in tup_hours:
        print(f'половина {Base[hours+1][1]}')

elif minutes > 30 and minutes < 45 and minutes not in (21, 31, 41, 51):
    if hours == 12 or hours == 0: 
        print(f'{Base[minutes // 10 * 10][0]} {Base[minutes % 10][0]} минут {Base[1][1]}')
    elif hours in tup_hours:
        print(f'{Base[minutes // 10 * 10][0]} {Base[minutes % 10][0]} минут {Base[hours+1][1]}')

elif minutes >= 45 and minutes < 59:
    minutes = 60 - minutes
    if hours == 12 or hours == 0 and minutes in (2, 3, 4): 
        print(f'без {Base[minutes][3]} минут час')
    elif hours == 12 or hours == 0 and minutes not in (2, 3, 4): 
        print(f'без {Base[minutes][2]} минут час')    
    elif hours in tup_hours and minutes in (2, 3, 4):
        print(f'без {Base[minutes][3]} минут {Base[hours+1][0]}') 
    elif hours in tup_hours:
        print(f'без {Base[minutes][2]} минут {Base[hours+1][0]}') 

elif minutes == 59:
    if hours == 12 or hours == 0 and minutes in (2, 3, 4): 
        print(f'без {Base[1][3]} минуты час')
    elif hours in tup_hours:
        print(f'без {Base[1][3]} минуты {Base[hours+1][0]}')            
