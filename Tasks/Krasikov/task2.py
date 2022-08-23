dict= {
    9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
    4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
    9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
    6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
    7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
ph = input(('Please enter your phone number for find:\n'))
if ph.isdigit() and len(ph) == 10:
    ph=int(ph)
    if ph in dict:
        print(f'{dict[ph][0][0]} {dict[ph][0][1]} from {dict[ph][1][0]}, {dict[ph][1][1]}')
    else:
        print('Phone number was not found.')
else:
    print('Validation error, please try again.')
