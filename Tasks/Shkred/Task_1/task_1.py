def validate_input(text, type):
    flag = False
    while not flag:
        inp = input(text +'\n')
        try: 
            if type == 'int': 
                result = int(inp)
            elif type == 'float': 
                result = float(inp) 
            flag = True           
        except:
            flag = False
    return result

while True:
    initial_deposit_amount = validate_input("Enter the deposit amount:", "float") 
    period = validate_input("Enter the required period in years:", "int") 
    percentage = validate_input("Enter the annual percentage:", "float")/100  
    monthly_capitalization = input("Enter Y to enable monthly capitalization:\n")

    if monthly_capitalization == 'Y':
        period *= 12
        percentage /= 12
    summ = initial_deposit_amount*((1+percentage)**period)
    print('%.2f' %summ)
    
    to_continue = input("Enter Y to start over:\n")
    if to_continue != 'Y':
        break  
          