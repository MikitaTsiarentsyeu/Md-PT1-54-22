from datetime import datetime
dh = {00:'двенадцать', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять',
    11:'одиннадцать', 12:'двенадцать', 13:'один', 14:'два', 15:'три', 16:'четыре', 17:'пять', 18:'шесть', 19:'семь', 20:'восемь', 
    21:'девять', 22:'десять', 23:'одиннадцать', 24:'двенадцать'}
d1 = {1:'первого', 2:'второго', 3:'третьего', 4:'четвертого', 5:'пятого', 6:'шестого', 7:'седьмого', 8:'восьмого', 9:'девятого', 10:'десятого',
    11:'одиннадцатого', 12:'двенадцатого', 13:'первого', 14:'второго', 15:'третьего', 16:'четвертого', 17:'пятого', 18:'шестого', 19:'седьмого', 
    20:'восьмого', 21:'девятого', 22:'десятого', 23:'одиннадцатого', 24:'двенадцатого'}
dm = {00:'двенадцать', 1:'одна', 2:'две', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать', 
    12:'двенадцать', 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семнадцать', 18:'восемнадцать', 
    19:'девятнадцать', 20:'двадцать', 30:'тридцать', 40:'сорок', 50:'пятьдесят'}

a = input('Press N if you want to know current time and press T if you want to enter your time\n')
a = a.upper()
if a == 'T':
    x = input('Enter time in format hh.mm:\n')
    x = ''.join(i for i in x if i.isdigit())
    while len(x) < 3 or len(x) > 4:
        print('Check your data and reenter time')
        break    
    else:
        m = int(x[-2:])
        h = int(x[:-2])
        space = ''
        firstdigit = m // 10
        lastdigit = m % 10

        if lastdigit  == 1:
            space = 'минута'
        if 1 < lastdigit <= 4:
            space = 'минуты'
        if lastdigit > 4 or (lastdigit  == 1 and firstdigit == 1):
            space = 'минут'

        if m == 00:
            if 4 < h < 13 or 16 < h <= 24 or h == 0:
                space = 'часов'
            if 1 < h <= 4 or 13 < h <= 16:
                space = 'часа'
            if h == 1 or h == 13:
                space = 'час'     
            print(f'{dh[h]} {space} ровно')
        if 0 < m < 30:
            if firstdigit == 2:
                print(f'{dm[20]} {dm[lastdigit]} {space} {d1[h + 1]}')
            else: print(f'{dm[m]} {space} {d1[h + 1]}')
        if m == 30:
            print(f'половина {d1[h+1]}')
        if 30 < m < 45:
            if firstdigit == 3:
                print(f'{dm[30]} {dm[lastdigit]} {space} {d1[h + 1]}')
            else: print(f'{dm[40]} {dm[lastdigit]} {space} {d1[h + 1]}')
        if m >= 45:
            space = dm[60 - m]
            if h == 0 or h == 12:
                dh[h + 1] = 'час'
            if 60 - m == 1:
                space = space.replace('а', 'ой')
                print(f'без {space} минуты {dh[h + 1]}')  
            if 60 - m == 2:
                space = space.replace('е', 'ух')
                print(f'без {space} минут {dh[h + 1]}')
            if 60 - m == 3:
                space = space.replace('и', 'ех')
                print(f'без {space} минут {dh[h + 1]}')
            if 60 - m == 4:
                space = space + 'х'
                print(f'без {space} минут {dh[h + 1]}')
            if 60 - m == 8:
                space = space.replace('емь', 'ьми')
                print(f'без {space} минут {dh[h + 1]}')
            if 5 <= 60 - m <= 7 or 9 <= 60 - m <=15:
                space = space.replace('ть', 'ти')
                print(f'без {space} минут {dh[h + 1]}')
elif a == 'N':
    x = datetime.now()
    firstdigit = x.minute // 10
    lastdigit = x.minute % 10
    space = ''
    
    if lastdigit  == 1:
        space = 'минута'
    if 1 < lastdigit <= 4:
        space = 'минуты'
    if lastdigit > 4 or (lastdigit  == 1 and firstdigit == 1):
        space = 'минут'
    
    if x.minute == 0:
        if 4 < x.hour < 13 or 16 < x.hour <= 24:
                space = 'часов'
        if 1 < x.hour <= 4 or 13 < x.hour <= 16:
                space = 'часа'
        if x.hour == 1 or x.hour == 13:
                space = 'час'     
        print(f'{dh[x.hour]} {space} ровно')
    if 0 < x.minute < 30:
        if firstdigit == 2:
            print(f'{dm[20]} {dm[lastdigit]} {space} {d1[x.hour + 1]}')
        else: print(f'{dm[x.minute]} {space} {d1[x.hour + 1]}')
    if x.minute == 30:
        print(f'половина {d1[x.hour + 1]}')
    if 30 < x.minute < 45:
        if firstdigit == 3:
            print(f'{dm[30]} {dm[lastdigit]} {space} {d1[x.hour + 1]}')
        else: print(f'{dm[40]} {dm[lastdigit]} {space} {d1[x.hour + 1]}')
    if x.minute >= 45:
        space = dm[60 - x.minute]
        if x.hour == 0 or x.hour == 12:
            dh[x.hour + 1] = 'час'
        if 60 - x.minute == 1:
            space = space.replace('а', 'ой')
            print(f'без {space} минуты {dh[x.hour + 1]}')  
        if 60 - x.minute == 2:
            space = space.replace('е', 'ух')
            print(f'без {space} минут {dh[x.hour + 1]}')
        if 60 - x.minute == 3:
            space = space.replace('и', 'ех')
            print(f'без {space} минут {dh[x.hour + 1]}')
        if 60 - x.minute == 4:
            space = space + 'х'
            print(f'без {space} минут {dh[x.hour + 1]}')
        if 60 - x.minute == 8:
            space = space.replace('емь', 'ьми')
            print(f'без {space} минут {dh[x.hour + 1]}')
        if 5 <= 60 - x.minute <= 7 or 9 <= 60 - x.minute <=15:
            space = space.replace('ть', 'ти')
            print(f'без {space} минут {dh[x.hour + 1]}')
else: print('Check your choose')