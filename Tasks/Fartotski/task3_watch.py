import datetime
hours={0:"двенадцать часов", 1:"один час", 2:"два часа", 3:"три часа", 4:"четыре часа", 5:"пять часов", 6:"шесть часов", 7:"семь часов", 8:"восемь часов", 9:"девять часов",
       10:"десять часов", 11:"одинадцать часов", 12:"двенадцать часов", 13:"один час", 14:"два часа", 15:"три часа", 16:"четыре часа", 17:"пять часов", 18:"шесть часов",
       19:"семь часов", 20:"восемь часов", 21:"девять часов", 22:"десять часов", 23:"одинадцать часов"}
hours_1={1:"первого", 2:"второго", 3:"третьего", 4:"четвертого", 5:"пятого", 6:"шестого", 7:"седьмого", 8:"восьмого", 9:"девятого",
       10:"десятого", 11:"одинадцатого", 12:"двенадцатого", 13:"первого", 14:"второго", 15:"третьего", 16:"четвертого", 17:"пятого", 18:"шестого",
       19:"седьмого", 20:"восьмого", 21:"девятого", 22:"десятого", 23:"одинадцатого", 24:"двенадцадого"}
hours_2={1:"час", 2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять", 10:"десять", 11:"одинадцать",
         12:"двенадцать", 13:"час", 14:"два", 15:"три", 16:"четыре", 17:"пять", 18:"шесть", 19:"семь", 20:"восемь", 21:"девять",
         22:"десять", 23:"одинадцать", 24:"двенадцать"}
minutes={0:"ноль минут", 1:"одна минута", 2:"две минуты", 3:"три минуты", 4:"четыре минуты", 5:"пять минут", 6:"шесть минут", 7:"семь минут", 8:"восемь минут",
         9:"девять минут", 10:"десять минут", 11:"одинадцать минут", 12:"двенадцать минут", 13:"тринадцать минут", 14:"четырнадцать минут", 15:"пятнадцать минут",
         16:"шестнадцать минут", 17:"семьнадцать минут", 18:"восемьнадцать минут", 19:"девятнадцать минут", 20:"двадцать минут", 21:"двадцать одна минута",
         22:"двадцать две минуты", 23:"двадцать три минуты", 24:"двадцать четыре минуты", 25:"двадцать пять минут", 26:"двадцать шесть минут", 27:"двадцать семь минут",
         28:"двадцать восемь минут", 29:"двадцать девять минут", 30:"тридцать минут", 31:"тридцать одна минута", 32:"тридцать две минуты", 33:"тридцать три минуты",
         34:"тридцать четыре минуты", 35:"тридцать пять минут", 36:"тридцать шесть минут", 37:"тридцать семь минут", 38:"тридцать восемь минут", 39:"тридцать девять минут",
         40:"сорок минут", 41:"сорок одна минута", 42:"сорок две минуты", 43:"сорок три минуты", 44:"сорок четыре минуты"}
minutes_1={1:"одной минуты", 2:"двух минут", 3:"трех минут", 4:"четырех минут", 5:"пяти минут", 6:"шести минут", 7:"семи минут", 8:"восьми минут", 9:"девяти минут",
           10:"десяти минут", 11:"одиннадцати минут", 12:"двенадцати минут", 13:"тринадцати минут", 14:"четырнадцати минут", 15:"пятнадцати минут"}
now=datetime.datetime.now()
x=input("please, press '1' - if you want to display the current time or '2' - if you want to enter the time manually: \n")
if x=="1":
    time_now=now.strftime("%H:%M")
    values = time_now.split(':')
    hour = int(values[0])
    minute = int(values[1])
    if minute==0:
        print(hours[hour], "ровно")
    elif minute<30:
        print(minutes[minute], hours_1[hour+1])
    elif minute==30:
        print("половина", hours_1[hour+1])
    elif minute>30 and minute<45:
        print(minutes[minute], hours_1[hour+1])
    elif minute>=45:
        minute=60-minute
        print("без", minutes_1[minute], hours_2[hour+1])
else:
    while True:
        user_time=input("please enter the time in the format hh:mm \n")
        if len(user_time) != 5:
            print("the format of your value is incorrect, please try again")
            continue
        if user_time[2] !=':':
            print("the format of your value is incorrect, the 'colons' are missing, please try again")
            continue
        values = user_time.split(':')
        failed = False
        for value in values:
            if not value.isdigit():
                failed = True
                break
        if failed:
            print("the format of your value is incorrect, the time should consists of only digits, please try again")
            continue
        hour = int(values[0])
        minute = int(values[1])
        if hour < 0 or hour >= 24:
            print("the format of your value is incorrect, the hour value is incorrect, please try again")
            continue
        if minute < 0 or minute > 59:
            print("the format of your value is incorrect, the minute value is incorrect, please try again")
            continue
        break
    if minute==0:
        print(hours[hour], "ровно")
    elif minute<30:
        print(minutes[minute], hours_1[hour+1])
    elif minute==30:
        print("половина", hours_1[hour+1])
    elif minute>30 and minute<45:
        print(minutes[minute], hours_1[hour+1])
    elif minute>=45:
        minute=60-minute
        print("без", minutes_1[minute], hours_2[hour+1])
