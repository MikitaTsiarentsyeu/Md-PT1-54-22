d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")], 4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")], 9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")], 6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")], 7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
x = input('Enter telephone number (10 numbers only):\n') 
if x.isdigit() and len(x) == 10:
    if x == '9103976271':
        print(f'{d[9103976271][0][0]} {d[9103976271][0][1]} from {d[9103976271][1][0]}, {d[9103976271][1][1]}')
    elif x == '4199392609':
        print(f'{d[4199392609][0][0]} {d[4199392609][0][1]} from {d[4199392609][1][0]}, {d[4199392609][1][1]}')
    elif x == '9099459979':
        print(f'{d[9099459979][0][0]} {d[9099459979][0][1]} from {d[9099459979][1][0]}, {d[9099459979][1][1]}')
    elif x == '6123479367':
        print(f'{d[6123479367][0][0]} {d[6123479367][0][1]} from {d[6123479367][1][0]}, {d[6123479367][1][1]}')
    elif x == '7548993768':
        print(f'{d[7548993768][0][0]} {d[7548993768][0][1]} from {d[7548993768][1][0]}, {d[7548993768][1][1]}')
    else: print('the number was not found')
else: print('Check your data')
