#MaksiukVasil_task_2

PhoneBook = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")], 
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

number0 = input('Please enter the telephon number: ')

if len(number0) == 10 and int(number0):
    number1 = int(number0)
    if PhoneBook.get(int(number0)) != None:
        print(f"{PhoneBook[number1][0][0]} {PhoneBook[number1][0][1]} from {PhoneBook[number1][1][0]}, {PhoneBook[number1][1][1]}.")
    elif PhoneBook.get(number1) == None:
        print('The number was not found.')
else:
    print('Incorrect number! Please enter a valid phone number - 10 digits (no letters or other symbols).')