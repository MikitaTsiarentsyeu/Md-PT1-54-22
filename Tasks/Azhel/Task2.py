girls = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

search = input("Please enter a telephone number:\n")

if len(search) != 10 or not search.isdigit() or int(search) not in girls.keys():
    print("The number was not found")
else:
    n = girls.get(int(search)) #name_and_address
    print(n[0][0], n[0][1], 'from', n[1][0], 'state', n[1][1])