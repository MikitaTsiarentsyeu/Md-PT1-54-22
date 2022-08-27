a = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

while True:
   try:
      b = int(input('Please enter phone number :\n'))
      c = str(b)
      if len(c) == 10 :
         break
      else:
         print('Wrong number! Try again')
   except ValueError:
         print('You are loser! Enter only digits')
        
if b in a :
   x = a[b]
   x[0] = str(x[0]).replace("'", "").replace(",", "").replace("(", "").replace(")", "")
   x[1] = str(x[1]).replace("'", "").replace("(", "").replace(")", "")

   print(str(x[0]), 'from', str(x[1]))
else :
   print("The number was not found")
