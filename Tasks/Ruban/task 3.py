dmin = {1:"одна минута",
2:"две минуты",
3:"три минуты",
4:"четыре минуты",
5:"пять минут",
6:"шесть минут",
7:"семь минут",
8:"восемь минут",
9:"девять минут",
10:"десять минут",
11:"одинадцать минут",
12:"двенадцать минут",
13:"тринадцать минут",
14:"четырнадцать минут",
15:"пятнадцать минут",
16:"шестнадцать минут",
17:"семнадцать минут",
18:"восемнадцать минут",
19:"девятнадцать минут",
20:"двадцать минут",
21:"двадцать одна минута",
22:"двадцать две минуты",
23:"двадцать три минуты",
24:"двадцать четыре минуты",
25:"двадцать пять минут",
26:"двадцать шесть минут",
27:"двадцать семь минут",
28:"двадцать восемь минут",
29:"двадцать девять минут",
30:"половина",
31:"тридцать одна минута",
32:"тридцать две  минуты",
33:"тридцать три минуты",
34:"тридцать четыре минуты",
35:"тридцать пять минут",
36:"тридцать шесть минут",
37:"тридцать семь минут",
38:"тридцать восемь минут",
39:"тридцать девять минут",
40:"сорок минут",
41:"сорок одна минута",
42:"сорок две минуты",
43:"сорок три минуты",
44:"сорок четыре минуты",
45:"без пятнадцати минут",
46:"без четырнадцати минут",
47:"без тринадцати минут",
48:"без двенадцати минут",
49:"без одинадцати минут",
50:"без десяти минут",
51:"без девяти минут",
52:"без восьми минут",
53:"без семи минут",
54:"без шести минут",
55:"без пяти минут",
56:"без четырех минут",
57:"без трех минут",
58:"без двух минут",
59:"без одной минуты"}
dhour = {0:["двенадцать", "двенадцать часов ровно", "двенадцатого"],
1:["час", "один час ровно", "первого"],
2:["два", "два часа ровно", "второго"],
3:["три", "три часа ровно", "третьего"],
4:["четыре", "четыре часа ровно", "четвертого"],
5:["пять", "пять часов ровно", "пятого "],
6:["шесть", "шесть часов ровно", "шестого"],
7:["семь", "семь часов ровно", "седьмого"],
8:["восемь", "восемь часов ровно", "восьмого"],
9:["девять", "девять часов ровно", "девятого"],
10:["деcять", "десять часов ровно", "десятого"],
11:["одинадцать", "одинадцать часов ровно", "одинадцатого"]}
print('Hi User! Please choose program mode')
while True:
    prmode = input('Type "current" for text output of current time or "manual" for text output of manually entered time \n')
    if prmode != 'current' and prmode != 'manual':
        print('Incorrect input. Please try again')
    else:    
        break
if prmode == 'current':    
    import datetime
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.strftime('%H:%M')
    values = current_time.split(':')
    hour = int(values[0]) 
    minute = int(values[1])
    if 11<hour<24:
        hour = hour - 12
    if minute == 0:
        print(f'Текущее время {dhour.get(hour)[1]}')
    elif 0 < minute < 45:
        hour = hour + 1          
        print(f'Текущее время {dmin.get(minute)} {dhour.get(hour)[2]}')
    elif 45 <= minute <= 59:
        hour = hour + 1         
        print(f'Текущее время {dmin.get(minute)} {dhour.get(hour)[0]}')    
if prmode == 'manual':
    while True:
        user_time = input('Please input time in the format hh:mm \n')
        if len(user_time) != 5 or user_time[2] != ':':
            print('The format of your value is incorrect, please try again')               
            continue     
        values = user_time.split(':')
        failed = False
        for value in values:
            if not value.isdigit():
                failed = True
                break    
        if failed:
            print("The format of your value is incorrect, the time should consist of only digits, please try again")
            continue
        hour = int(values[0])
        minute = int(values[1])
        if hour < 0 or hour > 23:
            print("The hour value is incorrect, please try again")
            continue
        if minute < 0 or minute > 59:
            print("The hour value is incorrect, please try again")
            continue
        break
    if 11<hour<24:
        hour = hour - 12    
    if minute == 0:
        print(f'Время пользователя {dhour.get(hour)[1]}')
    elif 0 < minute < 45:
        hour = hour + 1           
        print(f'Время пользователя {dmin.get(minute)} {dhour.get(hour)[2]}')
    elif 45 <= minute <= 59:
        hour = hour + 1          
        print(f'Время пользователя {dmin.get(minute)} {dhour.get(hour)[0]}')         