from datetime import datetime


def mode_choice():
    mode = input(
        "please select program mode: \n\tfor 'current time' enter 'c', \n\tfor 'user time' enter 'u':\n "
    )
    if mode == 'c':
        get_time_in_words(get_current_time())
    elif mode == 'u':
        get_time_in_words(get_user_time())
    else:
        print('input was wrong please try again')
        return mode_choice()


def get_current_time():
    return datetime.now().hour, datetime.now().minute


def get_user_time():
    user_time = input('Please enter time like hh:mm: \n')
    if len(user_time) == 5:
        if user_time[2] == ':':
            if user_time[0:2].isdigit() and user_time[3:].isdigit():
                if 0 <= int(user_time[0:2]) <= 23 and 0 <= int(user_time[3:]) <= 59:
                    return int(user_time.split(':')[0]), int(user_time.split(':')[1])
                elif int(user_time[0:2]) == 24 and int(user_time[3:]) == 0:
                    return int(user_time.split(':')[0]), int(user_time.split(':')[1])
    print('The format was wrong. Please try again')
    return get_user_time()


def get_time_in_words(time):
    hour, min = time

    if min == 0:
        return time_0(hour)
    # first haven't use 'elif on this level and sometimes worked 'else' from the next level
    # (there was nested leve of if/else before refactoring )
    #  why? next level is separated by indent...

    elif 0 < min < 30 or 30 < min < 45:
        return time_1_44(hour, min)
    elif min == 30:
        return time_30(hour)
    elif min >= 45:
        return time_45(hour, min)
    # haven't used 'else' since seem more logical without else. is it OK?


def time_0(hour):
    if 2 <= hour <= 4 or 22 <= hour <= 24:
        print(f'{dict_numb[hour][0]} часа ровно')
    elif hour == 1 or hour == 21:
        print(f'{dict_numb[hour][0]} час ровно')
    else:
        print(f'{dict_numb[hour][0]} часов ровно')


def time_30(hour):
    print(f'половина {dict_numb[hour][1]}')


def time_45(hour, min):
    hour = hour + 1
    min = 60 - min
    if min == 1:
        print(f'Без {dict_numb[min][2]} минуты {dict_numb[hour][0]}')
    else:
        print(f'Без {dict_numb[min][2]} минут {dict_numb[hour][0]}')


def time_1_44(hour, min):
    min_unit = min % 10
    min_dec = min - min % 10
    if min < 21:
        if min == 1:
            print(f'{dict_numb[min][3]} минутa {dict_numb[hour][1]}')
        elif min == 3 or min == 4:
            print(f'{dict_numb[min][0]} минуты {dict_numb[hour][1]}')
        elif min == 2:
            print(f'{dict_numb[min][3]} минуты {dict_numb[hour][1]}')
        else:
            print(f'{dict_numb[min][0]} минут {dict_numb[hour][1]}')

    elif 21 <= min < 30 or 30 < min < 45:
        if min_unit == 2:
            print(f'{dict_numb[min_dec][0]} {dict_numb[min_unit][3]} минуты {dict_numb[hour][1]}')
        elif min_unit == 3 or min_unit == 4:
            print(f'{dict_numb[min_dec][0]} {dict_numb[min_unit][0]} минуты {dict_numb[hour][1]}')
        elif min_unit == 1:
            print(f'{dict_numb[min_dec][0]} {dict_numb[min_unit][3]} минута {dict_numb[hour][1]}')
        else:
            print(f'{dict_numb[min_dec][0]} {dict_numb[min_unit][0]} минут {dict_numb[hour][1]}')


# is it worth to use decorators here (to decorate get_time_in_words with mode_choice and get_user_time and get_current time?
# is there any lifehack how display such dictionaries in the program?
dict_numb = {1: ['один', 'второго', 'одной', 'одна'],
             2: ['два', 'третьего', 'двух', 'две'],
             3: ['три', 'четвертого', 'трех', ''],
             4: ['четыре', 'пятого', 'четырех', ''],
             5: ['пять', 'шестого', 'пяти', ''],
             6: ['шесть', 'седьмого', 'шести', ''],
             7: ['семь', 'восьмого', 'семи', ''],
             8: ['восемь', 'девятого', 'восьми', ''],
             9: ['девять', 'десятого', 'девяти', ''],
             10: ['десять', 'одиннадцатого', 'десяти', ''],
             11: ['одиннадцать', 'двенадцатого', 'одиннадцати', ''],
             12: ['двенадцать', 'первого', 'двенадцати', ''],
             13: ['тринадцать', 'второго', 'тринадцати', ''],
             14: ['четырнадцать', 'третьего', 'четырнадцати', ''],
             15: ['пятнадцать', 'четвертого', 'пятнадцати', ''],
             16: ['шестнадцать', 'пятого', '', ''],
             17: ['семнадцать', 'шестого', '', ''],
             18: ['восемнадцать', 'седьмого', '', ''],
             19: ['девятнадцать', 'восьмого', '', ''],
             20: ['двадцать', '    девятого', '', ''],
             21: ['двадцать один', 'девятого', '', ''],
             22: ['двадцать два', 'одиннадцатого', '', ''],
             23: ['двадцать три', 'двенадцатого', '', ''],
             24: ['двадцать четыре', 'первого', '', ''],
             30: ['тридцать', '', '', ''],
             40: ['сорок', '', '', ''],
             0: ['', '', '', '']
             }

mode_choice()
