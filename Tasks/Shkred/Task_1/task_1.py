from decimal import Decimal 

def validate_input(text):
    flag = False
    while not flag:
        inp = input(text +'\n')
        if inp[0] == '-':
            continue
        try: 
            if text == "Enter the required period in years:":
                if int(inp):
                    pass
            elif float(inp): 
                pass       
            flag = True               
        except:
            pass
    return inp

while True:
    initial_deposit_amount = Decimal(validate_input("Enter the deposit amount:")) 
    period = Decimal(validate_input("Enter the required period in years:"))
    percentage = Decimal(validate_input("Enter the annual percentage:"))/100  
    monthly_capitalization = input("Enter Y to enable monthly capitalization or press the enter button:\n")

    if monthly_capitalization.upper() == 'Y':
        period *= 12
        percentage /= 12
    summ = initial_deposit_amount*((1+percentage)**period)
    print(summ.quantize(Decimal('1.00')))
    
    to_continue = input("Enter Y to start over or press the enter button:\n")
    if to_continue.upper() != 'Y':
        break  
          