data_base = {'9103976271': [("Reina", "Meinhard"), ("Memphis", "Tennessee")],
             '4199392609': [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
             '9099459979': [("Ermes", "Angela"), ("Dallas", "Texas")],
             '6123479367': [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
             '7548993768': [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
data = True
while data == True:
    number = input("Enter phone number:\n")
    if number.isdigit() and len(number) == 10:
        if number in data_base:
            data = True
            print("Data by number:",
                  f"{data_base[number][0][0]} {data_base[number][0][1]} from {data_base[number][1][0]}, {data_base[number][1][1]}")
        else:
            data = True
            print("Phone number not found")
    else:
        data = False
        print("Wrong input format! The number must be from 10 digits!")
