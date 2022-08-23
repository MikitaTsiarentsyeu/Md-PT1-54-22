from decimal import Decimal, ROUND_UP
 
deposit_amount = Decimal(input('Enter deposit amount: '))
deposit_period = Decimal(input('Deposit term (years): '))
annual_interest_rate = Decimal(input('Annual interest rate (without "%"): '))
deposit_capitalization = input('Do you want to enable monthly capitalization? (Type "YES" or "NO") ')

if deposit_amount > 0 and deposit_period > 0 and annual_interest_rate > 0:    
    if deposit_capitalization == 'YES':
        deposit_amount *= (1 + (annual_interest_rate / 100 / 12)) ** (12 * deposit_period)
    else:
        deposit_amount += deposit_amount * annual_interest_rate * deposit_period / 100
    print('Your balance will be', deposit_amount.quantize(Decimal('0.01'), rounding=ROUND_UP), sep=': ', end="!")
else: 
    print('Too low deposit amount, or interest, or term. They should be more than 0. Please try again.')

