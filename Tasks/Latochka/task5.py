# 1. Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию о количестве букв в верхнем и нижнем регистре.check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'
def check_str(string):
	upper_case = 0
	lower_case = 0
	for i in string:
		if i.isupper():
			upper_case += 1
		if i.islower():
			lower_case += 1
	return f'{upper_case} upper case, {lower_case} lower case'
print(check_str('The quick Brown Fox'))

# 2. Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, если число является простым, и False, если нет.
def is_prime(n):
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
print(is_prime(787))
print(is_prime(777))

# 3. Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.
def get_ranges(list):
	x = str(list[0])
	for i in range(1, len(list)):
		if list[i] - list[i-1] == 1:
			if list[i] == list[-1]:
				x += "-" + str(list[i])
			else:
				if list[i+1] - list[i] != 1:
					x += "-" + str(list[i])
		elif list[i] - list[i-1] != 1:
			if  list[i] == list[-1]:
				x += ", " + str(list[i])
			else:
				x += ", " + str(list[i])
	return x
print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10])) 
print(get_ranges([4,7,10]))  
print(get_ranges([2, 3, 8, 9]))