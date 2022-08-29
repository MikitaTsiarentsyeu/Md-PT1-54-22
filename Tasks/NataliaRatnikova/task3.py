import datetime

hours = {00:['двенадцать', 'двенадцатого'],
1:['час', 'первого'], 
2:['два', 'второго'], 
3:['три', 'третьего'], 
4:['четыре','четвертого'], 
5:['пять','пятого'], 
6:['шесть','шестого'], 
7:['семь','седьмого'], 
8:['восемь','восьмого'], 
9:['девять','девятого'], 
10:['десять','десятого'], 
11:['одиннадцать','одиннадцатого'], 
12:['двенадцать','двенадцатого'], 
13:['час', 'первого'], 
14:['два', 'второго'], 
15:['три', 'третьего'], 
16:['четыре', 'четвертого'], 
17:['пять', 'пятого'], 
18:['шесть', 'шестого'], 
19:['семь', 'седьмого'], 
20:['восемь', 'восьмого'], 
21:['девять', 'девятого'], 
22:['десять', 'десятого'], 
23:['одиннадцать', 'одиннадцатого'], 
24:['двенадцать', 'двенадцатого']}

minutes = {00:['ровно'],
1:['одна', 'одной'], 
2:['две', 'двух'], 
3:['три', 'трех'], 
4:['четыре', 'четырех'], 
5:['пять', 'пяти'], 
6:['шесть', 'шести'], 
7:['семь', 'семи'], 
8:['восемь', 'восьми'], 
9:['девять', 'девяти'], 
10:['десять', 'десяти'], 
11:['одиннадцать', 'одннадцати'], 
12:['двенадцать', 'двенадцати'], 
13:['тринадцать', 'тринадцати'], 
14:['четырнадцать', 'четырнадцати'], 
15:['пятнадцать', 'пятнадцати'], 
16:['шестнадцать'], 
17:['семнадцать'], 
18:['восемнадцать'], 
19:['девятнадцать'], 
20:['двадцать'], 
21:['двадцать одина'], 
22:['двадцать две'], 
23:['двадцать три'], 
24:['двадцать четыре'], 
25:['двадцать пять'], 
26:['двадцать шесть'], 
27:['двадцать семь'], 
28:['двадцать восемь'], 
29:['двадцать девять'], 
30:['половина'], 
31:['тридцать одна'], 
32:['тридцать две'], 
33:['тридцать три'], 
34:['тридцать четыре'], 
35:['тридцать пять'], 
36:['тридцать шесть'], 
37:['тридцать семь'], 
38:['тридцать восемь'], 
39:['тридцать девять'], 
40:['сорок'], 
41:['сорок одна'], 
42:['сорок две'], 
43:['сорок три'], 
44:['сорок четыре'], 
45:['пятнадцати'], 
46:['четырнадцати'], 
47:['тринадцати'], 
48:['двенадцати'], 
49:['одиннадцати'], 
50:['десяти'],
51:['девяти'], 
52:['восьми'], 
53:['семи'], 
54:['шести'], 
55:['пяти'], 
56:['четырех'], 
57:['трех'], 
58:['двух'], 
59:['одной'], 
}

while True:
    mode = input('Please, enter "now" if you want to know current time or enter the time in format hh:mm if you want to know specific one:\n')
    if mode == 'now' or mode == 'Now':
        current_time = datetime.datetime.now().strftime("%H:%M")
        current_time = current_time.split(':')
        nhours = int(current_time[0])
        nminutes = int(current_time[1])
        if nhours in hours and nminutes in minutes:
            if nminutes == 00 and nhours == 1:
                print(f'The current time is {hours[nhours][0]} {minutes[nminutes][0]}')
            if nminutes == 00 and nhours > 1 and nhours <= 4:
                print(f'The current time is {hours[nhours][0]} часа {minutes[nminutes][0]}')
            if nminutes == 00 and nhours > 4 or nminutes == 00 and nhours == 00:
                print(f'The current time is {hours[nhours][0]} часов {minutes[nminutes][0]}')
            if nminutes == 30:
                print(f'The current time is половина {hours[nhours+1][1]}')
            if nminutes == 1 or nminutes == 21 or nminutes == 31 or nminutes == 41:
                print(f'The current time is {minutes[nminutes][0]} минута {hours[nhours+1][1]}')    
            if nminutes > 0 and nminutes <= 4 or nminutes > 21 and nminutes <= 24 or nminutes > 31 and nminutes <= 34 or nminutes > 41 and nminutes <= 44:
                print(f'The current time is {minutes[nminutes][0]} минуты {hours[nhours+1][1]}')
            if nminutes > 4 and nminutes < 21 or nminutes > 24 and nminutes < 30 or nminutes > 34 and nminutes < 40:
                print(f'The current time is {minutes[nminutes][0]} минут {hours[nhours+1][1]}')
            if nminutes >= 45 and nminutes < 59:
                print(f'The current time is без {minutes[nminutes][0]} минут {hours[nhours+1][0]}')
            if nminutes == 59:
                print(f'The current time is без {minutes[nminutes][0]} минуты {hours[nhours+1][0]}')
        break
    if len(mode) == 5 and mode[0:2].isdigit() == True and mode[3:].isdigit()== True and mode[2] == ':':
        mode = mode.split(':')
        userhours = int(mode[0])
        userminutes = int(mode[1])
        if userhours in hours and userminutes in minutes:
            if userminutes == 00 and userhours == 1:
                print(f'The current time is {hours[userhours][0]} {minutes[userminutes][0]}')
            if userminutes == 00 and userhours > 1 and userhours <= 4:
                print(f'The current time is {hours[userhours][0]} часа {minutes[userminutes][0]}')
            if userminutes == 00 and userhours > 4 or userminutes == 00 and userhours == 00:
                print(f'The current time is {hours[userhours][0]} часов {minutes[userminutes][0]}')
            if userminutes == 30:
                print(f'The current time is половина {hours[userhours+1][1]}')
            if userminutes == 1 or userminutes == 21 or userminutes == 31 or userminutes == 41:
                print(f'The current time is {minutes[userminutes][0]} минута {hours[userhours+1][1]}')    
            if userminutes > 0 and userminutes <= 4 or userminutes > 21 and userminutes <= 24 or userminutes > 31 and userminutes <= 34 or userminutes > 41 and userminutes <= 44:
                print(f'The current time is {minutes[userminutes][0]} минуты {hours[userhours+1][1]}')
            if userminutes > 4 and userminutes < 21 or userminutes > 24 and userminutes < 30 or userminutes > 34 and userminutes < 40:
                print(f'The current time is {minutes[userminutes][0]} минут {hours[userhours+1][1]}')
            if userminutes >= 45 and userminutes < 59:
                print(f'The current time is без {minutes[userminutes][0]} минут {hours[userhours+1][0]}')
            if userminutes == 59:
                print(f'The current time is без {minutes[userminutes][0]} минуты {hours[userhours+1][0]}')
        break
    else:
        print('The format is incorrect, please try again')

