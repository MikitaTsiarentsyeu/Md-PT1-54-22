while True:
    user_value = input("enter the date in the 'dd.mm.yyyy' format:\n")

    if len(user_value) != 10:
        print("the format of your value is incorrect, please try again")
        continue

    if user_value[2] != '.' or user_value[5] != '.':
        print("the format of your value is incorrect, the dots are missing, please try again")
        continue

    values = user_value.split('.')

    failed = False
    for value in values:
        if not value.isdigit():
            failed = True
            break
    
    if failed:
        print("the format of your value is incorrect, the date should consists of only digits, please try again")
        continue
    
    day = int(values[0])
    month = int(values[1])
    year = int(values[2])

    if day < 1 and day > 31:
        print("the format of your value is incorrect, the day value is incorrect, please try again")
        continue

    if month < 1 and month > 12:
        print("the format of your value is incorrect, the month value is incorrect, please try again")
        continue


    if year < 1900 and year > 2022:
        print("the format of your value is incorrect, the year value is incorrect, please try again")
        continue

    break

print("main logic goes here")