d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]} 

phone = input("Please, enter the phone number:\n")
while len(phone) != 10 or phone.isdigit() == False:
    print("Invalid number. Please, try again")
    phone = input("Please, enter the phone number:\n")

phone=int(phone)
if phone in d:
    print(f"{d[phone][0][0]} {d[phone][0][1]} from {d[phone][1][0]}, {d[phone][1][1]}")
else:
    print("the number was not found")


# """The 2d solution"""

# d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
# 4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
# 9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
# 6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
# 7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]} 

# L1 = [("Reina", "Meinhard"), ("Memphis", "Tennessee")]
# L2 = [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")]
# L3 = [("Ermes", "Angela"), ("Dallas", "Texas")]
# L4 = [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")]
# L5 = [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]

# phone = input("Please, enter the phone number:\n")
# while len(phone) != 10 or phone.isdigit() == False:
#     print("Invalid number. Please, try again")
#     phone = input("Please, enter the phone number:\n")

# if phone == '9103976271':
#     print(f"{L1[0][0]} {L1[0][1]} from {L1[1][0]}, {L1[1][1]}")
# elif phone == '4199392609':
#     print(f"{L2[0][0]} {L2[0][1]} from {L2[1][0]}, {L2[1][1]}") 
# elif phone == '9099459979':
#     print(f"{L3[0][0]} {L3[0][1]} from {L3[1][0]}, {L3[1][1]}") 
# elif phone == '6123479367':
#     print(f"{L4[0][0]} {L4[0][1]} from {L4[1][0]}, {L4[1][1]}") 
# elif phone == '7548993768':
#     print(f"{L5[0][0]} {L5[0][1]} from {L5[1][0]}, {L5[1][1]}") 
# else: print("the number was not found")

