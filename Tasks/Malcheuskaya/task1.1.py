import decimal
import math

def EnterVal(text, var): #функция проверки правильности ввода данных
    try:
        if var == 1:
            x = decimal.Decimal(input(text))
        elif var == 2:
            x = int(input(text))
        else:
            x = input(text)
            if x != "yes" and x != "no":
                print('Error:You did not enter "yes" or "no"')
                x = EnterVal(text, var)         
    except:
        print("Error:You did not enter a number")
        x = EnterVal(text, var)
    return x

money = EnterVal("Enter initial deposit, $: ", 1)
years = EnterVal("Enter the term of the deposit, years: ", 2)
percent = EnterVal("Annual percentage, %: ", 1)
kap = EnterVal("Include monthly capitalization? (yes/no): ", 3)

if kap == "yes":
    result = money * (1 + percent / (100 * 12))**(12 * years) #формула сложного процента
    print("Your total amount is", math.floor(result*100)/100, "$") #вывод результата с округлением до сотых в меньшую сторону
else:
    result = money * (1 + percent / 100 )** years
    print("Your total amount is", math.floor(result*100)/100, "$")
