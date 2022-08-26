import datetime

current_date_time = datetime.datetime.now()
b = current_date_time.time()
time1 = {1: ["один", "первого", "одной"], 2: ["два", "второго", "двух"], 3: ["три", "третьего", "трех"],
         4: ["четыре", "четвертого", "четырех"], 5: ["пять", "пятого", "пяти"],6: ["шесть", "шестого", "шести"],
         7: ["семь", "седьмого", "семи"], 8: ["восемь", "восьмого", "восьми"],9: ["девять", "девятого", "девяти"],
         10: ["десять", "десятого", "десяти"],11: ["одиннадцать", "одиннадцатого", "одиннадцати"],
         12: ["двенадцать", "двенадцатого", "двенадцати"],13: ["тринадцать", "", "тринадцати"],
         14: ["четырнадцать", "", "четырнадцати"], 15: ["пятнадцать", "", "пятнадцати"], 16: ["шестнадцать", ""],
         17: ["семнадцать", ""], 18: ["восемнадцать", ""],19: ["девятнадцать", ""], 20: ["двадцать", ""],
         21: ["двадцать один", ""], 22: ["двадцать два", ""],23: ["двадцать три", " "], 24: ["двадцать четыре", ""],
         25: ["двадцать пять", ""], 26: ["двадцать шесть", ""], 27: ["двадцать семь", ""], 28: ["двадцать восемь", ""],
         29: ["двадцать девять", ""], 30: ["тридцать", ""], 31: ["тридцать один", ""], 32: ["тридцать два", ""],
         33: ["тридцать три", ""], 34: ["тридцать четыре", ""],35: ["тридцать пять", ""], 36: ["тридцать шесть", ""],
         37: ["тридцать семь", ""], 38: ["тридцать восемь", ""], 39: ["тридцать девять", ""], 40: ["сорок", ""],
         41: ["сорок один", ""], 42: ["двадцать один", ""], 43: ["сорок три", ""], 44: ["сорок четыре", ""],
         45: ["сорок пять", ""], 46: ["сорок шесть", ""], 47: ["сорок семь", ""], 48: ["сорок восемь", ""],
         49: ["сорок девять", ""],50: ["пятьдесят", ""],51: ["пятьдесят один", ""], 52: ["пятьдесят два", ""],
         53: ["пятьдесят три", ""], 54: ["пятьдесят четыре", ""], 55: ["пятьдесят пять", ""],
         56: ["пятьдесят шесть", ""], 57: ["пятьдесят семь",""],58: ["пятьдесят восемь", ""],
         59: ["пятьдесят девять", ""]}
user_value = input("Enter 'b' if you want to see the current time or 'n' if you want to enter the date yourself :\n")
if user_value == "b":
    value = ("{:%H:%M}".format(b))
    print(value)
    s1 = value.split(':')
    key1 = int(s1[0])
    key2 = int(s1[1])
    hour1 = time1.get(key1)
    min1 = time1.get(key2)

    if key2 == 00:
        if key1 > 12:
            if key1 == 1:
                print("{:} час ровно".format(time1.get(key1 - 12)[0]))
            elif key1 > 1 and key1 < 5:
                print("{:} часа ровно".format(time1.get(key1 - 12)[0]))
            else:
                print("{:} часов ровно".format(time1.get(key1 - 12)[0]))
        else:
            if key1 == 1:
                print("{:} час ровно".format(time1.get(key1)[0]))
            elif key1 > 1 and key1 < 5:
                print("{:} часа ровно".format(time1.get(key1)[0]))
            else:
                print("{:} часов ровно".format(time1.get(key1)[0]))
    elif key2 < 30:
        if key1 > 12:
            print("{0} минут {1}".format(time1.get(key2)[0], time1.get(key1 - 11)[1]))
        else:
            print("{0} минут {1}".format(time1.get(key2)[0], time1.get(key1 + 1)[1]))
    elif key2 == 30:
        if key1 >= 12:
            print("половина {:}".format(time1.get(key1 - 11)[1]))
        else:
            print("половина {:}".format(time1.get(key1 + 1)[1]))
    elif key2 == 30 and key1 == 4:
        print("половина {:}".format(time1.get(3)))
    elif key2 > 30 and key2 < 45:
        if key1 > 12:
            print("{0} минут {1}".format(time1.get(key2)[0], time1.get(key1 - 11)[1]))
        else:
            print("{0} минут {1}".format(time1.get(key2)[0], time1.get(key1 + 1)[1]))

    elif key2 >= 45:
        if key1 > 12:
            print("без {0} минут {1}".format(time1.get(60 - key2)[2], time1.get(key1-11)[0]))
        else:
            print("без {0} минут {1}".format(time1.get(60 - key2)[2], time1.get(key1 + 1)[0]))

elif user_value == "n":
    while True:
        n = (input("Enter your time in the format hh:mm:\n"))
        if len(n) != 5:
            print("The format of your value is incorrect, please try again")
            continue

        if n[2] != ":":
            print("The format of your value is incorrect, it should be a colon, please try again")
            continue
        values = n.split(":")

        failed = False
        for value in values:
            if not value.isdigit():
                failed = True
                break

        if failed:
            print("the format of your value is incorrect, the time should consists of only digits, please try again")
            continue

        key3 = int(values[0])
        key4 = int(values[1])

        if key3 < 0 or key3 > 24:
            print("The format of your value is incorrect, the hour value is incorrect, please try again")
            continue

        if key4 < 0 or key4 > 60:
            print("the format of your value is incorrect, the minutes value is incorrect, please try again")
            continue

        if key4 == 00:
            if key3 > 12:
                if key3 == 1:
                    print("{:} час ровно".format(time1.get(key3 - 12)[0]))
                elif key3 > 1 and key3 < 5:
                    print("{:} часа ровно".format(time1.get(key3 - 12)[0]))
                else:
                    print("{:} часов ровно".format(time1.get(key3 - 12)[0]))
            else:
                if key3 == 1:
                    print("{:} час ровно".format(time1.get(key3)[0]))
                elif key3 > 1 and key3 < 5:
                    print("{:} часа ровно".format(time1.get(key3)[0]))
                else:
                    print("{:} часов ровно".format(time1.get(key3)[0]))
        elif key4 < 30:
            if key3 > 12:
                print("{0} минут {1}".format(time1.get(key4)[0], time1.get(key3 - 11)[1]))
            else:
                print("{0} минут {1}".format(time1.get(key4)[0], time1.get(key3 + 1)[1]))
        elif key4 == 30:
            if key3 >= 12:
                print("половина {:}".format(time1.get(key3 - 11)[1]))
            else:
                print("половина {:}".format(time1.get(key3 + 1)[1]))
        elif key4 == 30 and key3 == 4:
            print("половина {:}".format(time1.get(3)))
        elif key4 > 30 and key4 < 45:
            if key3 > 12:
                print("{0} минут {1}".format(time1.get(key4)[0], time1.get(key3 - 11)[1]))
            else:
                print("{0} минут {1}".format(time1.get(key4)[0], time1.get(key3 + 1)[1]))

        elif key4 >= 45:
            if key3 > 12:
                print("без {0} минут {1}".format(time1.get(60 - key4)[2], time1.get(key3 - 11)[0]))
            else:
                print("без {0} минут {1}".format(time1.get(60 - key4)[2], time1.get(key3 + 1)[0]))
        break
else:
    print("You entered incorrect data, please try again")

