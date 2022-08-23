contacts = {'9103976271': [("Reina", "Meinhard"), ("Memphis", "Tennessee")], '4199392609': [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
'9099459979': [("Ermes", "Angela"), ("Dallas", "Texas")],
'6123479367': [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
'7548993768': [("Margarete", "Quintin"), ("Raleigh", "North Carolinaf")]}

number = input("Input a phone number: ")

if number.isdigit():
    if 1 < len(number) <= 10:

        try:
            contact = contacts[number]

            name = contact[0][0]
            surname = contact[0][1]
            city = contact[1][0]
            state = contact[1][1]

            print(f"{name} {surname} from {city} {state}")
        except:
            print("Contact with this phone number does not exist.")
    else:
        print("Entered phone number is longer than 10 digits.")
else:
    print("An unsupported phone number format was entered.")