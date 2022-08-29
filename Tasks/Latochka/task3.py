#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
hours_values = {0: ['двенадцать часов', 'двенадцатого','двенадцать'], 1: ['один час', 'первого', 'час'], 2: ['два часа', 'второго', 'два'], 3: ['три часа', 'третьего', 'три'], 4: ['четыре часа', 'четвертого', 'четыре'], 5: ['пять часов', 'пятого', 'пять'], 6: ['шесть часов', 'шестого', 'шесть'], 7: ['семь часов', 'седьмого', 'семь'], 8: ['восемь часов', 'восьмого', 'восемь'], 9: ['девять часов', 'девятого', 'девять'], 10: ['десять часов', 'десятого', 'десять'], 11: ['одиннадцать часов', 'одиннадцатого', 'одиннадцать'], 12: ['двенадцать часов', 'двенадцатого', 'двенадцать'], 13: ['один час', 'первого', 'час'], 14: ['два часа', 'второго', 'два'], 15: ['три часа', 'третьего', 'три'], 16: ['четыре часа', 'четвертого', 'четыре'], 17: ['пять часов', 'пятого', 'пять'], 18: ['шесть часов', 'шестого', 'шесть'], 19: ['семь часов', 'седьмого', 'семь'], 20: ['восемь часов', 'восьмого', 'восемь'], 21: ['девять часов', 'девятого', 'девять'], 22: ['десять часов', 'десятого', 'десять'], 23: ['одиннадцать часов', 'одиннадцатого','одиннадцать'], 24: ['двенадцать часов', 'двенадцатого','двенадцать']}
minute_values = {0: 'ровно', 1: 'одна минута', 2: 'две минуты', 3: 'три минуты', 4: 'четыре минуты', 5: 'пять минут', 6: 'шесть минут', 7: 'семь минут', 8: 'восемь минут', 9: 'девять минут', 10: 'десять минут', 11: 'одиннадцать минут', 12: 'двенадцать минут', 13: 'тринадцать минут', 14: 'четырнадцать минут', 15: 'пятнадцать минут', 16: 'шеснадцать минут', 17: 'семнадцать минут', 18: 'восемнадцать минут', 19: 'девятнадцать минут', 20: 'двадцать минут', 21: 'двадцать одна минута', 22: 'двадцать две минуты', 23: 'двадцать три минуты', 24: 'двадцать четыре минуты', 25: 'двадцать пять минут', 26: 'двадцать шесть минут', 27: 'двадцать семь минут', 28: 'двадцать восемь минут', 29: 'двадцать девять минут', 30: 'половина', 31: 'тридцать одна минута', 32: 'тридцать две минуты', 33: 'тридцать три минуты', 34: 'тридцать четыре минуты', 35: 'тридцать пять минут', 36: 'тридцать шесть минут', 37: 'тридцать семь минут', 38: 'тридцать восемь минут', 39: 'тридцать девять минут', 40: 'сорок минут', 41: 'сорок одна минута', 42: 'сорок две минуты', 43: 'сорок три минуты', 44: 'сорок четыре минуты', 45: 'пятнадцти минут', 46: 'четырнадцати минут', 47: 'тринадцати минут', 48: 'двенадцати минут', 49: 'одиннадцати минут', 50: 'десяти минут', 51: 'девяти минут', 52: 'восьми минут', 53: 'семи минут', 54: 'шести минут', 55: 'пяти минут', 56: 'четырёх минут', 57: 'трёх минут', 58: 'двух минут', 59: 'одной минуты'}
data = False
while data == False:
	choice = input('Enter "1" if you want to know the current time.  Enter "2" if you want to enter your own time.:\n')
	if choice == '1' or choice == '2':
		data = True
	else: 
		data = False
		print('Data entered incorrectly. You must enter "1" or "2". Try entering the data again, please.')
if choice == '1':
	now = datetime.datetime.now()
	curent_hour = now.hour
	curent_minute = now.minute
else:
	while data == True:
		user_time = input('Enter your time in the format hh:mm, please:\n')
		if len(user_time) == 5 and user_time[0:2].isdigit() and user_time[3:].isdigit() and user_time[2] == ':':
			user_time = user_time.split(':')
			curent_hour = int(user_time[0])
			curent_minute = int(user_time[1])
			if curent_hour == 24 and  curent_minute != 0:
				data = True
				print('Data entered incorrectly. If the value "hh" is "24", the value "mm" must be "00". Please try entering your details again.')
			elif curent_hour < 25 and  curent_minute < 60:
				data = False
			else:
				data = True
				print('Data entered incorrectly. The "hh" value must not be greater than "24" and the "mm" value must not be greater than 59. Try entering the data again, please.')
		else: 
			data = True
			print('Data entered incorrectly. You must enter two digits with ":" between them. Try entering the data again, please.')
if curent_minute == 0:
	print(f"{hours_values[curent_hour][0]} {minute_values[curent_minute]}")
elif curent_minute < 30:
	print(f"{minute_values[curent_minute]} {hours_values[curent_hour + 1][1]}")
elif curent_minute == 30:
	print(f"{minute_values[curent_minute]} {hours_values[curent_hour + 1][1]}")
elif curent_minute > 30 and curent_minute < 45:
	print(f"{minute_values[curent_minute]} {hours_values[curent_hour + 1][1]}")
else:
	print(f"без {minute_values[curent_minute]} {hours_values[curent_hour + 1][2]}")	