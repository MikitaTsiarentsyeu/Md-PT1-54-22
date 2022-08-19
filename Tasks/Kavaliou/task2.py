phonebook = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]} 

phone_number  = input('Enter the telephone number: ')

while len(phone_number) != 10 or phone_number.isdigit() != True:
    print('Wrong telephon number. Try other one: ')
    phone_number = input('Enter the telephone number: ')

phone_number  = int(phone_number)

if phone_number in phonebook:
    contacts = phonebook[phone_number]
    name = contacts [0] [0]
    surname = contacts [0] [1]
    city = contacts [1] [0]
    state = contacts [1] [1]
    print(f'{name} {surname} from {city}, {state}')
else:
    print(f'{phone_number} was not found in the phonebook. Try other one: ')
