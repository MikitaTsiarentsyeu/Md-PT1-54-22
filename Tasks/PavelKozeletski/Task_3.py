from datetime import datetime

option = 1
while option < 2:
    answer = input("\nDo you want to check system time?(Y/N):\nIf you choose option No(N), you will have to enter the time manually\n")
    if answer == "Y":
        option = 2
    elif answer == "N":
        option = 3
    else:
        print("\n\033[1;31mPlease, enter a proper value\033[0m\n")
if option == 2:
    h, m = int(datetime.now().time().hour) if int(datetime.now().time().hour) < 12 else int(datetime.now().time().hour)-12, datetime.now().time().minute
else:
    p = 1
    while p < 2:
        t = input("\nPlease, enter the time in format: HH:MM in  24-hour time:\n")
        try:
            check = float(t.split(':')[0])
            check = float(t.split(':')[1])
        except IndexError:
            print("\n\033[1;31mPlease, enter \":\" between numbers\033[0m\n")
        except ValueError:
            print("\n\033[1;31mPlease, enter a proper value\033[0m\n")
        else:
            if len(t) == 5 and len(t.split(':')[0]) == 2:
                if float(t.split(':')[0]) > 23:
                    print ("\n\033[1;31mPlease, enter a proper count of hours\033[0m\n")
                elif float(t.split(':')[1]) > 59:
                    print ("\n\033[1;31mPlease, enter a proper count of minutes\033[0m\n")
                elif float(t.split(':')[0]) <0 and float(t.split(':')[1]):
                    print ("\n\033[1;31mHours and minutes couldn't be negative\033[0m\n")
                else:
                    p = 2
            else:
                print("\n\033[1;31mPlease, enter a proper count of symbols\033[0m\n")
    h, m = int(t.split(':')[0]) if int(t.split(':')[0]) < 12 else int(t.split(':')[0])-12, int(t.split(':')[1])
l1 = {
0:("двенадцать", "двенадцатого"),
1:("один", "первого"),
2:("два", "второго"),
3:("три", "третьего"),
4:("четыре", "четвертого"),
5:("пять", "пятого"),
6:("шесть", "шестого"),
7:("семь", "седьмого"),
8:("восемь", "восьмого"),
9:("девять", "девятого"),
10:("десять", "десятого"),
11:("одиннадцать", "одиннадцатого"),
12:("двенадцать", "двенадцатого")
}
l2 = {
1:("одна", "одиннадцать", "", "одной"),
2:("две", "двенадцать", "двадцать", "двух"),
3:("три", "тринадцать", "тридцать", "трех"),
4:("четыре","четырнадцать", "сорок", "четырех"),
5:("пять", "пятнадцать", "пятьдесят", "пяти"),
6:("шесть", "шестнадцать", "", "шести"),
7:("семь", "семьнадцать", "", "семи"),
8:("восемь", "восемьнадцать", "", "восьми"),
9:("девять", "девятнадцать", "", "девяти"),
10:("десять","", "", "десяти")
}
if m == 0:    
    if h == 1:
        print(f"\n\033[1;32m{l1.get(h)[0]} час ровно\033[0m\n")
    else:
        print(f"\n\033[1;32m{l1.get(h)[0]} часа ровно\033[0m\n") if h > 0 and h < 5 else print(f"\n\033[1;32m{l1.get(h)[0]} часов ровно\033[0m\n")
elif m > 0 and m < 30:
    if m < 11:
        if m == 1:
            print(f"\n\033[1;32m{l2.get(m)[0]} минута {l1.get(h+1)[1]}\033[0m\n") 
        elif m > 1 and m < 5:
            print(f"\n\033[1;32m{l2.get(m)[0]} минуты {l1.get(h+1)[1]}\033[0m\n")
        else:
            print(f"\n\033[1;32m{l2.get(m)[0]} минут {l1.get(h+1)[1]}\033[0m\n") 
    elif m < 20:
        print(f"\n\033[1;32m{l2.get(int(m-10))[1]} минут {l1.get(h+1)[1]}\033[0m\n") if m > 10 else print(f"\n\033[1;32m{l2.get(int(m))[1]} минут {l1.get(h+1)[1]}\033[0m\n")
    elif m == 20:
        print(f"\n\033[1;32m{l2.get(int(m/10))[2]} минут {l1.get(h+1)[1]}\033[0m\n")
    elif m == 21:
        print(f"\n\033[1;32m{l2.get(int(m/10))[2]} {l2.get(int(m%10))[0]} минута {l1.get(h+1)[1]}\033[0m\n")
    elif m > 21 and m < 25:
        print(f"\n\033[1;32m{l2.get(int(m/10))[2]} {l2.get(int(m%10))[0]} минуты {l1.get(h+1)[1]}\033[0m\n")
    else:
        print(f"\n\033[1;32m{l2.get(int(m/10))[2]} {l2.get(int(m%10))[0]} минут {l1.get(h+1)[1]}\033[0m\n")
elif m == 30:
        print(f"\n\033[1;32mполовина {l1.get(h+1)[1]}\033[0m\n")
elif m > 30 and m < 45:
    if m == 40:
        print(f"\n\033[1;32m{l2.get(m/10)[2]} минут {l1.get(h+1)[1]}\033[0m\n")
    else:
        if m%10 == 1:
            print(f"\n\033[1;32m{l2.get(int(m/10))[2]} {l2.get(m%10)[0]} минута {l1.get(h+1)[1]}\033[0m\n")
        elif m%10 > 1 and m%10 < 5:
            print(f"\n\033[1;32m{l2.get(int(m/10))[2]} {l2.get(m%10)[0]} минуты {l1.get(h+1)[1]}\033[0m\n")
        else:
            print(f"\n\033[1;32m{l2.get(int(m/10))[2]} {l2.get(m%10)[0]} минут {l1.get(h+1)[1]}\033[0m\n")
else:
    if m > 44 and m < 50:
        print(f"\n\033[1;32mбез {l2.get((m-60)*(-1)-10)[1][:-1]}и минут {l1.get(h+1)[0]}\033[0m\n")
    elif m == 59:
        print(f"\n\033[1;32mбез {l2.get((m-60)*(-1))[3]} минуты {l1.get(h+1)[0]}\033[0m\n")
    else:
        print(f"\n\033[1;32mбез {l2.get((m-60)*(-1))[3]} минут {l1.get(h+1)[0]}\033[0m\n")        