Base = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

print('Please, enter the telephone number')
telephone = input()
if telephone.isdigit() and len(telephone) == 10:
    telephone = int(telephone)
    if telephone in Base:
        print(f'{Base[telephone][0][0]} {Base[telephone][0][1]} from {Base[telephone][-1][0]}, {Base[telephone][-1][-1]}')
    else:
        print('the number was not found')    
else:
    print('Uncorrect number. Please, try again.')  
