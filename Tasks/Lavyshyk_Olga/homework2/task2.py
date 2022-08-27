
d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
try:
     number = int(input(" Enter phone number:\n"))
     number1 = str(number)
     if len(number1) != 10:
          print("You entered the wrong number of characters")
     else:
          list1 = (d[number])
          list2 = list1[0]
          list3 = list1[1]
          listNew = list2 + list3
          name = listNew[0]
          surname = listNew[1]
          city = listNew[2]
          state = listNew[3]
          print("{{{0}}} {{{1}}} from {{{2}}}, {{{3}}}".format(name, surname, city, state))
     
except ValueError:
     print ("You entered an invalid value")
except KeyError:
     print("The number was not found")

