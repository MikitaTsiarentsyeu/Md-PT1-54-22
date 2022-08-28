from datetime import datetime

d_hours = {0: 'двенадцать', 1: 'час', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
      11: 'одиннадцать', 12: 'двенадцать'}
d_hours_plus = { 0: 'первого', 1: 'второго', 2: 'третьего', 3: 'четвертого', 4: 'пятого', 5: 'шестого', 6: 'седьмого',
                7: 'восьмого', 8: 'девятого', 9: 'десятого', 10: 'одиннадцатого', 11: 'двенадцатого', 12: 'первого'}
d_minutes = {1: 'одна', 2: 'две', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять',
     11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
     17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать', 30: 'тридцать', 40: 'сорок'}
d_min_to_h = {59: 'одной', 58: 'двух', 57: 'трех', 56: 'четырех', 55: 'пяти', 54: 'шести', 53: 'семи', 52: 'восьми',
              51: 'девяти', 50: 'десяти', 49: 'одиннадцати', 48: 'двенадцати', 47: 'тринадцати', 46: 'четырнадцати', 45: 'пятнадцати'}

while True:
    user_choice = input("Для получения в текстовом формате текущего времени введите '1', своего времени - '2': \n")
    if not user_choice.isdigit():
        print("Доступны только цифры")
        continue
    elif user_choice == "1":
        user_time = datetime.now().strftime("%H:%M").split(':')
        hours, minutes = int(user_time[0]), int(user_time[1])
    elif user_choice == "2":
        while True:
            user_time = input("Введите время в формате 'hh:mm':\n")
            if len(user_time) != 5:
                print("Некорректный формат данных, повторите попытку")
                continue
            if user_time[2] != ':':
                print("Неправильный разделитель. Часы и минуты должны разделяться знаком ':'")
                continue
            time = user_time.split(':')
            if not time[0].isdigit() or not time[1].isdigit():
                print("Вы указали часы или минуты не цифрами. Введите цифры")
                continue
            hours, minutes = int(time[0]), int(time[1])
            if not 0 <= hours <= 23:
                print("Неверно указаны часы. Введите количество часов от 00 до 23")
                continue
            if not 0 <= minutes <= 59:
                print("Неверно указаны минуты. Введите количество минут от 00 до 59")
                continue
            break
    else:
        print("Доступны только цифры 1 и 2")
    break
if hours in range(13, 24):
    hours -= 12
if minutes == 0:
    if hours == 1:
        print(f'{d_hours[hours]} ровно')
    elif hours in [2, 3, 4]:
        print(f'{d_hours[hours]} часа ровно')
    else:
        print(f'{d_hours[hours]} часов ровно')
elif minutes == 1:
    print(f'{d_minutes[minutes]} минута {d_hours_plus[hours]}')
elif minutes in range(2, 5):
    print(f'{d_minutes[minutes]} минуты {d_hours_plus[hours]}')
elif minutes in range(5, 21) or minutes == 40:
    print(f'{d_minutes[minutes]} минут {d_hours_plus[hours]}')
elif minutes in [21, 31, 41]:
    print(f'{d_minutes[minutes - 1]} {d_minutes[minutes % 10]} минута {d_hours_plus[hours]}')
elif minutes % 10 in range(2,5) and minutes < 45:
    print(f'{d_minutes[minutes - minutes % 10]} {d_minutes[minutes % 10]} минуты {d_hours_plus[hours]}')
elif minutes == 30:
    print(f'половина {d_hours[hours]}')
elif minutes in range(26, 45):
    print(f'{d_minutes[minutes - minutes % 10]} {d_minutes[minutes % 10]} минут {d_hours_plus[hours]}')
elif minutes == 59:
    if hours == 12:
        print(f'без {minutes} минуты час')
    else:
        print(f'без {d_min_to_h[minutes]} минуты {d_hours[hours + 1]}')
else:
    if hours == 12:
        print(f'без {d_min_to_h[minutes]} минут час')
    else:
        print(f'без {d_min_to_h[minutes]} минут {d_hours[hours+1]}')
