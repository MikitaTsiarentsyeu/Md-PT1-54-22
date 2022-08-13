from decimal import Decimal 

def validate_input(text, type):
    flag = False
    while not flag:
        inp = input(text +'\n')
        if inp[0]=='-':
            continue
        try: 
            if type == 'int': 
                result = int(inp)
                if str(result) != inp:
                    continue
            elif type == 'Decimal': 
                result = Decimal(inp) 
            flag = True           
        except:
            flag = False
    return result

while True:
    initial_deposit_amount = validate_input("Enter the deposit amount:", "Decimal")
    period = validate_input("Enter the required period in years:", "int")
    percentage = validate_input("Enter the annual percentage:", "Decimal")/100  
    monthly_capitalization = input("Enter Y to enable monthly capitalization or press the enter button:\n")

    if monthly_capitalization.upper() == 'Y':
        period *= 12
        percentage /= 12
    summ = initial_deposit_amount*((1+percentage)**period)
    print(summ.quantize(Decimal('1.00')),type(summ))
    
    to_continue = input("Enter Y to start over or press the enter button:\n")
    if to_continue.upper() != 'Y':
        break  
          