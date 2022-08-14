print('Hello! Welcome to the investment calculator. Please enter the deposit amount:')
deposit = float(input())
print('Please enter the deposit term (years):')
years = float(input())
print('Please enter interest rate (% per year):')
percent = float(input())
total_deposit = ((1+(percent*years)/100)*deposit)

print('Total deposit amount at the end of the term:', '%.2f' % (total_deposit))
print('Your final profit:', '%.2f' % (total_deposit  -deposit))
print('Do you want to calculate your profit using monthly capitalization? Answer only YES or NO:')
capitalization = input().upper()

if capitalization == 'YES':
    total_deposit_with_mountly_capitalization = float(((1+percent/12/100)**(years*12))*deposit)
    print('Your income with capitalization will be:', '%.2f' % total_deposit_with_mountly_capitalization)
    print('Your final profit will be:', '%.2f' % (total_deposit_with_mountly_capitalization - deposit))
elif capitalization == 'NO':
    print('Thank you for using our calculator! Have a nice day!')
else:
    print ('Invalid input. Please try again.')
