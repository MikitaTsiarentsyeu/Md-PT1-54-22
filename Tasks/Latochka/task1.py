import decimal
from decimal import Decimal, ROUND_HALF_UP
data = False
while data == False:
	amount = input('Enter the deposit amount, please:\n')
	deposit_period = input('Enter the term of the deposit in years, please:\n')
	interest_rate = input('Enter the amount of interest on the deposit, please: \n')
	try:
		amount = float(amount)
		deposit_period = float(deposit_period)
		interest_rate = float(interest_rate)
	except:
		data = False
		print('Data entered incorrectly.  The deposit amount, deposit period and interest rate must be numbers greater than 0. Try entering the data again, please.')
	else:
			if amount <= 0 or deposit_period <= 0 or interest_rate <= 0:
				data = False
				print('Data entered incorrectly.  The deposit amount, deposit period and interest rate must be numbers greater than 0. Try entering the data again, please.')
			else:
				data = True
else:
	amount = decimal.Decimal(amount)
	deposit_period = decimal.Decimal(deposit_period)
	interest_rate = decimal.Decimal(interest_rate)
while data == True:
	capitalization = input('Do you want to enable monthly capitalization? ("Yes" or "No"):\n')
	if capitalization == 'No':
		amount += amount * deposit_period * interest_rate / 100
		print('The amount on your account after the end of the deposit period will be', amount.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP))
		break
	elif capitalization == 'Yes':
		amount *=(1 + (interest_rate / 100 / 12))**(deposit_period * 12)
		print('The amount on your account after the end of the deposit period will be', amount.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP))
		break
	else:
		print('You entered the data incorrectly.  The answer must be "Yes" or "No".  Try again, please.')