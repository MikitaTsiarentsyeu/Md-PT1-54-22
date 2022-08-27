dict = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

phone = input("please, enter the phone number: \n")
if phone.isnumeric() and len(phone)==10:
    phone = int(phone)
    if phone in dict.keys():
        print(str(dict[phone][0][0])+" "+str( dict[phone][0][1])+" from "+str(dict[phone][1][0])+", "+str( dict[phone][1][1]))
    else:
        print("the number was not found")
else:
    print("phone number isn't correct, please, try again")