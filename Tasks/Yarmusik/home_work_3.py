from datetime import datetime, time

number_ones = {1: ['час', 'первого', 'одна', 'одной'], 2: ['два', 'второго', 'две', 'двух'], 3: ['три', 'третьего', 'трех'],
         4: ['четыре', 'четвертого', 'четырех'], 5: ['пять', 'пятого', 'пяти'], 6: ['шесть', 'шестого', 'шести'],
         7: ['семь', 'седьмого', 'семи'], 8: ['восемь', 'восьмого', 'восьми'], 9: ['девять', 'девятого', 'девяти'],
        10: ['десять', 'десятого', 'десяти'], 11: ['одиннадцать', 'одиннадцатого', 'одиннадцати'], 12: ['двенадцать', 'двенадцатого', 'двенадцати'],
        13: ['тринадцать', 'тринадцати'], 14: ['четырнадцать', 'четырнадцати'], 15: ['пятнадцать', 'пятнадцати'], 16: ['шестнадцать'],
        17: ['семнадцать'], 18: ['восемьнадцать'], 19: ['девятнадцать']}

number_tens = {20: ['двадцать'], 30: ['тридцать'], 40: ['сорок'], 50: ['пятьдесят']}

your_option = input('enter 1 - if you want to know the current time, \nenter 2 - if you want to enter the time yourself: ')
current_time = datetime.now()

if your_option == '1':
    print(f'Current time: {current_time.strftime("%I:%M")}')
elif your_option == '2':
    your_time = input('Enter your time (HH:MM): ')
    split_time = your_time.split(':')

    if len(your_time) == 5:
        if your_time[2] == ':':
            split_time = your_time.split(':')

            hour = split_time[0]
            min = split_time[1]

            if split_time[0].isdigit() and split_time[1].isdigit():
                if int(split_time[0]) <= 12 and int(split_time[1]) <=59:
                    if 1 <= int(min) < 30:
                        if int(min) < 9:
                            if int(hour) == 12:
                                out = number_ones[1]
                            else:
                                out = number_ones[int(split_time[0]) + 1]

                            out_min = number_ones[int(split_time[1])]
                            if int(min) == 1:
                                print(f'{out_min[2]} минута {out[1]}')
                            elif int(min) == 2:
                                print(f'{out_min[2]} минуты {out[1]}')
                            else:
                                print(f'{out_min[0]} минуты {out[1]}')
                        elif 10 <= int(min) <= 19:
                            if int(hour) == 12:
                                out = number_ones[1]
                            else:
                                out = number_ones[int(split_time[0]) + 1]

                            out_min = number_ones[int(split_time[1])]
                            print(f'{out_min[0]} минуты {out[1]}')

                        elif 20 <= int(min) <= 29:
                            if int(hour) == 12:
                                out = number_ones[1]
                            else:
                                out = number_ones[int(split_time[0]) + 1]

                            out_min = number_tens[20]

                            if int((split_time[1][1])) == 1:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[2]} минута {out[1]}')
                            elif int((split_time[1][1])) == 2:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[2]} минуты {out[1]}')
                            elif int(split_time[1]) == 20:
                                print(f'{out_min[0]} минут {out[1]}')
                            else:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[0]} минуты {out[1]}')

                    elif int(min) == 30:
                        if int(hour) == 12:
                            out = number_ones[1]
                            print(f'Половина {out[1]}')
                        else:
                            out = number_ones[int(split_time[0]) + 1]
                            print(f'Половина {out[1]}')
                    elif int(min) > 30:
                        if 30 < int(min) <= 39:
                            if int(hour) == 12:
                                out = number_ones[1]
                            else:
                                out = number_ones[int(split_time[0]) + 1]

                            out_min = number_tens[30]

                            if int((split_time[1][1])) == 1:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[2]} минута {out[1]}')
                            elif int((split_time[1][1])) == 2:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[2]} минуты {out[1]}')
                            else:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[0]} минуты {out[1]}')

                        elif 40 <= int(min) < 45:
                            if int(hour) == 12:
                                out = number_ones[1]
                            else:
                                out = number_ones[int(split_time[0]) + 1]

                            out_min = number_tens[40]

                            if int((split_time[1][1])) == 1:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[2]} минута {out[1]}')
                            elif int((split_time[1][1])) == 2:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[2]} минуты {out[1]}')
                            else:
                                out_min_split = number_ones[int((split_time[1][1]))]
                                print(f'{out_min[0]} {out_min_split[0]} минуты {out[1]}')

                        elif 45 <= int(min) <= 49:
                            if int(hour) == 12:
                                out = number_ones[1]
                            else:
                                out = number_ones[int(split_time[0]) + 1]

                            out_min = number_tens[40]

                            out_min_split = number_ones[60 - int((split_time[1]))]
                            print(f'без {out_min_split[2]} минут {out[1]}')

                        elif 50 <= int(min) <= 59:
                            if int(hour) == 12:
                                out = number_ones[1]
                            else:
                                out = number_ones[int(split_time[0]) + 1]

                            out_min = number_tens[50]

                            out_min_split = number_ones[60 - int((split_time[1]))]

                            if int((split_time[1][1])) == 59 or int((split_time[1][1])) == 58:
                                print(f'без {out_min_split[3]} минуты {out[1]}')
                            else:
                                print(f'без {out_min_split[2]} минут {out[1]}')

                    elif int(min) == 0:
                        out = number_ones[int(split_time[0])]
                        print(f'{out[0]} ровно')
                else:
                    print('Your time is not valid!')
            else:
                print('Your time is not valid!')
        else:
            print('Your time is not valid!')
    else:
        print('Your time is not valid!')
else:
    print('Your option is not valid!')



