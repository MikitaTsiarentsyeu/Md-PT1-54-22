d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")], 
    4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")], 
    9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")], 
    6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")], 
    7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

counter = 1
while counter < 2:
    tel = input("Enter the phone number:\n")
    if len(tel) == 10 and tel.isdigit():
        tel = int(tel)
        if tel in d:
            print("{}: {} {} from {}, {}".format(tel, d[tel][0][1], d[tel][0][0], d[tel][1][0], d[tel][1][1]))
            counter += 1
        else:
            print("The phone number '{}' doesn`t exist".format(tel))
    else:
        print("'{}' is incorrect phone number, please, try again".format(tel))