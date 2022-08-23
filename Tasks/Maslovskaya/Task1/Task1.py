import decimal

def is_number(x):
    try: 
        float(x)
    except ValueError:
        print("Entered value isn't correct. Please, try again and use only number with maximum of two decimal places.")
        return False
    else:
        if  decimal.Decimal(x)>0 and decimal.Decimal(x)*100==int(decimal.Decimal(x)*100):
            return True
        else:
            print("Entered value isn't correct. Please, try again and use only number with maximum of two decimal places.")
            return False

a= input("Hello. Let's check how much money you'll get at the end of deposit period.\nPlease, enter a sum of money in BYN that you want to place on your deposit:\nBYN ") 
while is_number(a)!=True:
    a= input("Please, enter a sum of money in BYN that you want to place on your deposit account:\nBYN ") 

b= input("Please, enter the annual percentage that you would like to receive on your deposit:\n% ") 
while is_number(b)!=True:
    b= input("Please, enter the annual percentage that you would like to receive on your deposit:\n% ") 

c= input("Please, enter the period in years for which you would like to place your deposit:\nyears ") 
while is_number(c)!=True:
    c= input("Please, enter the period in years for which you would like to place your deposit:\nyears ") 

d= input("To get the maximum income, we recommend that you choose a contract with a monthly capitalization of interest.\nPlease, entered yes or no to set your choice:\n") 
while (d=='yes' or d=='no')!=True:
    #print("Please, entered yes or no to set your choice:\n ")
    d= input("Please, entered yes or no to set your choice:\n")   

a=decimal.Decimal(a)
b=decimal.Decimal(b)
c=decimal.Decimal(c)*12
dep_without_cap=round(a+((a*b*c*30)/(100*360)),2)
dep_with_cap=round(a*((1+(b*30)/(100*360))**c),2)
if d=='no':
    print("If you put",a,"BYN on a deposit for",b,"years at",c,"% per annum without monthly capitalization of interest you'll get",dep_without_cap,"BYN at the end of period")
    print("Your income will be",dep_without_cap-a,"BYN")
else:
    print("If you put",a,"BYN on a deposit for",b,"years at",c,"% per annum with monthly capitalization of interest you'll get",dep_with_cap,"BYN at the end of period")
    print("Your income will be",dep_with_cap-a,"BYN")