d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
p = input('Please enter phone number \n')
if p.isdigit()==False:
    print('Phone number format is not valid')   
elif len(p)!=10:
    print('Please check length of number')
else:
    ph = int(p) 
    if int(ph) in d.keys():
        print(d.get(ph)[0][0], ' ', d.get(ph)[0][1], ' ', 'from ', d.get(ph)[1][0], ', ', d.get(ph)[1][1], sep='')
    else: print('The number was not found')     
    




