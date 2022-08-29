import datetime

num = { 0:  ["двенадцать",   "первого"],
        1:  ["один",         "второго",       "одной",      "одна"],
        2:  ["два",          "третьего",      "двух",       "две"],
        3:  ["три",          "четвертого",    "трёх"],
        4:  ["четыре",       "пятого",        "четырёх"],
        5:  ["пять",         "шестого",       "пяти"],
        6:  ["шесть",        "седьмого",      "шести"],
        7:  ["семь",         "восьмого",      "семи"],
        8:  ["восемь",       "девятого",      "восьми"],
        9:  ["девять",       "десятого",      "девяти"],
        10: ["десять",       "одиннадцатого", "десяти"],
        11: ["одиннадцать",  "двенадцатого",  "одиннадцати"],
        12: ["двенадцать",   "первого",       "двенадцати"],
        13: ["тринадцать",   "",              "тринадцати"],
        14: ["четырнадцать", "",              "четырнадцати"],
        15: ["пятнадцать",   "",              "пятнадцати"],
        16: ["шестнадцать"],
        17: ["семнадцать"],
        18: ["восемнадцать"],
        19: ["девятнадцать"],
        20: ["двадцать"],
        30: ["тридцать"],
        40: ["сорок"]}

while True:

    time = input("Press ENTER or write your time in hh:mm format: ")
    if time == "":
        time = str(datetime.datetime.now().time())[:5].split(":")
    else:    
        if len(time) != 5:
            print("Error: Enter your time in hh:mm format!")
            continue
        if time[2] != ":":
            print("Error: Colon is missing!")
            continue
        time = time.split(":")
        if not time[0].isdigit() or not time[1].isdigit():
            print("Error: Time must be digits only!")
            continue
        if time[0] < "00" or time[0] > "24":
            print("Error: The hour must be in range from 00 to 24!")
            continue
        if time[1] < "00" or time[1] > "59":
            print("Error: The minutes must be in range from 00 to 59!")
            continue
        
    time = [int(time[0]), int(time[1])] 
    if time[0] > 12:
        time[0] = time[0] - 12

    if time[1] == 0:
        if time[0] == 1:
            print(num[time[0]][0], "час ровно")
        if time[0] > 1 and time[0] < 5:
            print(num[time[0]][0], "часа ровно")
        if time[0] > 4 or time[0] == 0:
            print(num[time[0]][0], "часов ровно")

    if time[1] == 30:
        print("половина", num[time[0]][1])

    if (time[1] > 0 and time[1] < 21) or time[1] == 40:
        if time[1] == 1:
            print(num[time[1]][3], "минута", num[time[0]][1])
        if time[1] == 2:
            print(num[time[1]][3], "минуты", num[time[0]][1])    
        if time[1] > 2 and time[1] < 5:
            print(num[time[1]][0], "минуты", num[time[0]][1])
        if time[1] > 4:
            print(num[time[1]][0], "минут", num[time[0]][1])

    if time[1] > 20 and time[1] < 45 and time[1] != 30 and time[1] != 40:
        if time[1]%10 == 1:
            print(num[(time[1]//10)*10][0], num[time[1]%10][3], "минута", num[time[0]][1])
        if time[1]%10 == 2:
            print(num[(time[1]//10)*10][0], num[time[1]%10][3], "минуты", num[time[0]][1])    
        if time[1]%10 > 2 and time[1]%10 < 5:
            print(num[(time[1]//10)*10][0], num[time[1]%10][0], "минуты", num[time[0]][1])
        if time[1]%10 > 4:
            print(num[(time[1]//10)*10][0], num[time[1]%10][0], "минут", num[time[0]][1])

    if time[1] > 44:
        if time[0] == 12 or time[0] == 0:
            if 60-time[1] == 1:
                print("без", num[60-time[1]][2], "минуты час")
            if 60-time[1] > 1:
                print("без", num[60-time[1]][2], "минут час")
        else:
            if 60-time[1] == 1:
                print("без", num[60-time[1]][2], "минуты", num[time[0]+1][0])
            if 60-time[1] > 1:
                print("без", num[60-time[1]][2], "минут", num[time[0]+1][0])


