import datetime

full_hours_AM = {'01':'один час', '02':'два часа', '03':'три часа', '04':'четыре часа', '05':'пять часов',
                 '06':'шесть часов', '07':'семь часов', '08':'восемь часов', '09':'девять часов', '10':'десять часов',
                 '11':'одиннадцать часов', '12':'двенадцать часов', '00':'двенадцать часов'}
full_hours_PM = {'13':'один час', '14':'два часа', '15':'три часа', '16':'четыре часа', '17':'пять часов',
                 '18':'шесть часов', '19':'семь часов', '20':'восемь часов', '21':'девять часов', '22':'десять часов',
                 '23':'одинадцать часов', '24':'двенадцать часов', '00':'двенадцать часов'}
hours_AM = {'12':'первого', '01':'второго', '02':'третьего', '03':'четвёртого', '04':'пятого', '05':'шестого',
            '06':'седьмого', '07':'восьмого', '08':'девятого', '09':'десятого', '10':'одиннадцатого',
            '11':'двенадцатого', '00':'первого'}
hours_PM = {'24':'первого', '13':'второго', '14':'третьего', '15':'четвёртого', '16':'пятого', '17':'шестого',
            '18':'седьмого', '19':'восьмого', '20':'девятого', '21':'десятого', '22':'одиннадцатого',
            '23':'двенадцатого', '00':'первого'}
minutes = {'01':'одна минута', '02':'две минуты', '03':'три минуты', '04':'четыре минуты', '05':'пять минут',
           '06':'шесть минут', '07':'семь минут', '08':'восемь минут', '09':'девять минут', '10':'десять минут',
           '11':'одиннадцать минут', '12':'двенадцать минут', '13':'тринадцать минут', '14':'четырнадцать минут',
           '15':'пятнадцать минут', '16':'шестнадцать минут', '17':'семнадцать минут', '18':'восемнадцать минут',
           '19':'девятнадцать минут', '20':'двадцать минут', '21':'двадцать одна минута', '22':'двадцать две минуты',
           '23':'двадцать три минуты', '24':'двадцать четыре минуты', '25':'двадцать пять минут',
           '26':'двадцать шесть минут', '27':'двадцать семь минут', '28':'двадцать восемь минут',
           '29':'двадцать девять минут', '31':'тридцать одна минута', '32':'тридцать две минуты',
           '33':'тридцать три минуты', '34':'тридцать четыре минуты', '35':'тридцать пять минут',
           '36':'тридцать шесть минут', '37':'тридцать семь минут', '38':'тридцать восемь минут',
           '39':'тридцать девять минут', '40':'сорок минут', '41':'сорок одна минута', '42':'сорок две минуты',
           '43':'сорок три минуты', '44':'сорок четыре минуты'}
remaining_minutes = {'45':'пятнадцати минут', '46':'четырнадцати минут', '47':'тринадцати минут',
                     '48':'двенадцати минут', '49':'одиннадцати минут', '50':'десяти минут', '51':'девяти минут',
                     '52':'восьми минут', '53':'семи минут', '54':'шести минут', '55':'пяти минут',
                     '56':'четырёх минут', '57':'трёх минут', '58':'двух минут', '59':'одной минуты'}
hours_AM_with_remaining_minutes = {'12':'час', '01':'два', '02':'три', '03':'четыре', '04':'пять', '05':'шесть', '06':'семь', 
                              '07':'восемь', '08':'девять', '09':'десять', '10':'одиннадцать', '11':'двенадцать', '00':'час'}
hours_PM_with_remaining_minutes = {'24':'час', '13':'два', '14':'три', '15':'четыре', '16':'пять', '17':'шесть', '18':'семь', 
                              '19':'восемь', '20':'девять', '21':'десять', '22':'одиннадцать', '23':'двенадцать', '00':'час'}

answer = input("Do You want to know the current time? Enter 'Y' if You want, or 'N' if You don't want:\n").lower()

if answer == 'y':
        current_date_time = datetime.datetime.now()
        current_time = str(current_date_time.time()).split(':')[:2]
        print(current_time)
        if current_time[1] == '00':
            if int(current_time[0]) > 12:
                phrase = full_hours_PM.get(current_time[0])
                print(phrase, 'ровно')
            else:
                phrase = full_hours_AM.get(current_time[0])
                print(phrase, 'ровно')
        elif int(current_time[1]) == 30:
            if int(current_time[0]) > 12:
                phrase = hours_PM.get(current_time[0])
                print('половина', phrase)
            else:
                phrase = hours_AM.get(current_time[0])
                print('половина', phrase)
        elif int(current_time[1]) < 30 or 30 < int(current_time[1]) < 45:
            if int(current_time[0]) > 12:
                phrase_1 = hours_PM.get(current_time[0])
                phrase_2 = minutes.get(current_time[1])
                print(phrase_2, phrase_1)
            else:
                phrase_1 = hours_AM.get(current_time[0])
                phrase_2 = minutes.get(current_time[1])
                print(phrase_2, phrase_1)
        else:
            if int(current_time[0]) > 12:
                phrase_1 = hours_PM_with_remaining_minutes.get(current_time[0])
                phrase_2 = remaining_minutes.get(current_time[1])
                print('без', phrase_2, phrase_1)
            else:
                phrase_1 = hours_AM_with_remaining_minutes.get(current_time[0])
                phrase_2 = remaining_minutes.get(current_time[1])
                print('без', phrase_2, phrase_1)
elif answer == 'n':
        answer_2 = input('If You want to enter the time to know how it will be written in russian, please, write it in hh:mm form:\n').lower()
        time = answer_2.split(':')
        while (len(time) != 2) or (len(time[0]) != len(time[1]) != 2) or (not time[0].isdigit() and not time[1].isdigit()) or (int(time[1])>60 or int(time[0])>24):
            print('Your data is not correct! Please, try to be attentive')
            answer_2 = input('If You want to enter the time to know how it will be written in russian, please, write it in hh:mm form:\n')
            time = answer_2.split(':')
        if time[1] == '00':
            if int(time[0]) > 12:
                phrase = full_hours_PM.get(time[0])
                print(phrase, 'ровно')
            else:
                phrase = full_hours_AM.get(time[0])
                print(phrase, 'ровно')
        elif time[1] == '30':
            if int(time[0]) > 12:
                phrase = hours_PM.get(time[0])
                print('половина', phrase)
            else:
                phrase = hours_AM.get(time[0])
                print('половина', phrase)
        elif int(time[1]) < 30 or 30 < int(time[1]) < 45:
            if int(time[0]) > 12:
                phrase_1 = hours_PM.get(time[0])
                phrase_2 = minutes.get(time[1])
                print(phrase_2, phrase_1)
            else:
                phrase_1 = hours_AM.get(time[0])
                phrase_2 = minutes.get(time[1])
                print(phrase_2, phrase_1)
        else:
            if int(time[0]) > 12:
                phrase_1 = hours_PM_with_remaining_minutes.get(time[0])
                phrase_2 = remaining_minutes.get(time[1])
                print('без', phrase_2, phrase_1)
            else:
                phrase_1 = hours_AM_with_remaining_minutes.get(time[0])
                phrase_2 = remaining_minutes.get(time[1])
                print('без', phrase_2, phrase_1)
else:
    print('Your data is not correct! Please, try to be attentive')
    answer = input("Do You want to know the current time? Enter 'Y' if You want, or 'N' if You don't want:\n").lower()