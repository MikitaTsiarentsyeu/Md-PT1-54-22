from datetime import datetime
current_time = datetime.now().time()

d1 = {0:[("00"), ("12"), ("двеннадцать часов"), ("двеннадцатого")], 
    1:[("01"), ("13"), ("один час"), ("первого")], 
    2:[("02"), ("14"), ("два часа"), ("второго")], 
    3:[("03"), ("15"), ("три часа"), ("третьего")], 
    4:[("04"), ("16"), ("четыре часа"), ("четвертого")], 
    5:[("05"), ("17"), ("пять часов"), ("пятого")], 
    6:[("06"), ("18"), ("шесть часов"), ("шестого")], 
    7:[("07"), ("19"), ("семь часов"), ("седьмого")], 
    8:[("08"), ("20"), ("восемь часов"), ("восьмого")], 
    9:[("09"), ("21"), ("девять часов"), ("девятого")], 
    10:[("10"), ("22"), ("десять часов"), ("десятого")], 
    11:[("11"), ("23"), ("одиннадцать часов"), ("одиннадцатого")],
    12:[("00"), ("12"), ("двеннадцать часов"), ("двеннадцатого")]}

d2 = {0:[("00"), ("ровно")], 
    1:[("01"), ("одна минута"), ("одной")], 
    2:[("02"), ("две минуты"), ("двух")], 
    3:[("03"), ("три минуты"), ("трех")], 
    4:[("04"), ("четыре минуты"), ("четырех")], 
    5:[("05"), ("пять минут"), ("пяти")], 
    6:[("06"), ("шесть минут"), ("шести")], 
    7:[("07"), ("семь минут"), ("семи")], 
    8:[("08"), ("восемь минут"), ("восьми")], 
    9:[("09"), ("девять минут"), ("девяти")], 
    10:[("10"), ("десять минут"), ("десяти")], 
    11:[("11"), ("одиннадцать минут"), ("одиннадцати")], 
    12:[("12"), ("двенадцать минут"), ("двенадцати")], 
    13:[("13"), ("тринадцать минут"), ("тринадцати")], 
    14:[("14"), ("четырнадцать минут"), ("четырнадцати")], 
    15:[("15"), ("пятнадцать минут"), ("пятнадцати")], 
    16:[("16"), ("шестнадцать минут")], 
    17:[("17"), ("семнадцать минут")], 
    18:[("18"), ("восемнадцать минут")], 
    19:[("19"), ("девятнадцать минут")], 
    20:[("двадцать"), ("двадцати")], 
    30:[("тридцать"), ("половина")], 
    40:["сорок"]}

counter = 0

while counter < 1:
    text = input("Do you want to enter your time (Y or N)?\n")

    if text == "Y":
        
        while True:
            user_value = input("Please, enter your time in 'hh:mm' format:\n")
            
            if len(user_value) != 5:
                print("The format of your value is incorrect, please, try again")
                continue
            
            if user_value[2] != ":":
                print("You are missed a colon, please, try again")
                continue 
            
            values = user_value.split(":")
            failed = False
            
            for value in values:
                if not value.isdigit():
                    failed = True
                    break
            
            if failed:
                print("The format of your time is incorrect, you should use only digits, please, try again")
                continue
            
            h = int(values[0])
            m = int(values[1])
            
            if h >= 24:
                print("The format of your time is incorrect, please, enter value for hours from zero to twenty three")
                continue
            
            if m >= 60:
                print("The format of your time is incorrect, please, enter value for minutes from zero to fifty nine")
                continue
        
            break
            
        if h >= 12:
            h = h - 12
            if h in d1:
                if m == 0:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][1], d2[m][0], d1[h][2], d2[m][1]))
                elif m < 20:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][1], d2[m][0], d2[m][1], d1[h+1][3]))
                elif m == 20:
                    if m in d2:
                        print("{}:{} - {} минут {}".format(d1[h][1], m, d2[m][0], d1[h+1][3]))
                elif m > 20 and m < 30:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][1], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 30:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][1], m, d2[m][1], d1[h+1][3]))
                elif m > 30 and m < 45:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][1], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 45:
                    x = 60 - m
                    if x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][1], m, d2[x][2], d1[h+1][3]))
                elif m > 45:
                    x = 60 - m
                    if x > 1 and x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][1], m, d2[x][2], d1[h+1][3]))
                    if x == 1 and x in d2:
                        print("{}:{} - без {} минуты {}".format(d1[h][1], m, d2[x][2], d1[h+1][3]))
        
        elif h < 12:
            if h in d1:
                if m == 0:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][0], d2[m][0], d1[h][2], d2[m][1]))
                elif m < 20:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][0], d2[m][0], d2[m][1], d1[h+1][3]))
                elif m == 20:
                    if m in d2:
                        print("{}:{} - {} минут {}".format(d1[h][0], m, d2[m][0], d1[h+1][3]))
                elif m > 20 and m < 30:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][0], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 30:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][0], m, d2[m][1], d1[h+1][3]))
                elif m > 30 and m < 45:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][0], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 45:
                    x = 60 - m
                    if x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][0], m, d2[x][2], d1[h+1][3]))
                elif m > 45:
                    x = 60 - m
                    if x > 1 and x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][0], m, d2[x][2], d1[h+1][3]))
                    if x == 1 and x in d2:
                        print("{}:{} - без {} минуты {}".format(d1[h][0], m, d2[x][2], d1[h+1][3]))

        counter += 1

    elif text == "N":
        
        h = current_time.hour
        m = current_time.minute
        
        if h >= 12:
            h = h - 12
            if h in d1:
                if m == 0:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][1], d2[m][0], d1[h][2], d2[m][1]))
                elif m < 20:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][1], d2[m][0], d2[m][1], d1[h+1][3]))
                elif m == 20:
                    if m in d2:
                        print("{}:{} - {} минут {}".format(d1[h][1], m, d2[m][0], d1[h+1][3]))
                elif m > 20 and m < 30:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][1], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 30:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][1], m, d2[m][1], d1[h+1][3]))
                elif m > 30 and m < 45:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][1], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 45:
                    x = 60 - m
                    if x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][1], m, d2[x][2], d1[h+1][3]))
                elif m > 45:
                    x = 60 - m
                    if x > 1 and x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][1], m, d2[x][2], d1[h+1][3]))
                    if x == 1 and x in d2:
                        print("{}:{} - без {} минуты {}".format(d1[h][1], m, d2[x][2], d1[h+1][3]))
        elif h < 12:
            if h in d1:
                if m == 0:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][0], d2[m][0], d1[h][2], d2[m][1]))
                elif m < 20:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][0], d2[m][0], d2[m][1], d1[h+1][3]))
                elif m == 20:
                    if m in d2:
                        print("{}:{} - {} минут {}".format(d1[h][0], m, d2[m][0], d1[h+1][3]))
                elif m > 20 and m < 30:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][0], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 30:
                    if m in d2:
                        print("{}:{} - {} {}".format(d1[h][0], m, d2[m][1], d1[h+1][3]))
                elif m > 30 and m < 45:
                    x = m % 10
                    y = m - x
                    if x and y in d2:
                        print("{}:{} - {} {} {}".format(d1[h][0], m, d2[y][0], d2[x][1], d1[h+1][3]))
                elif m == 45:
                    x = 60 - m
                    if x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][0], m, d2[x][2], d1[h+1][3]))
                elif m > 45:
                    x = 60 - m
                    if x > 1 and x in d2:
                        print("{}:{} - без {} минут {}".format(d1[h][0], m, d2[x][2], d1[h+1][3]))
                    if x == 1 and x in d2:
                        print("{}:{} - без {} минуты {}".format(d1[h][0], m, d2[x][2], d1[h+1][3]))
        
        counter += 1
        
    else:
        print("Your input is incorrect, please, use 'Y' for 'yes' or 'N' for 'no'")