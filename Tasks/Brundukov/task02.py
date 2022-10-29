book  = {'9103976271' : [("Reina", "Meinhard"),("Memphis", "Tennessee")],
  '4199392609' : [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
   '9099459979' : [("Ermes", "Angela"), ("Dallas", "Texas")],
    '6123479367' : [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
     '7548993768' : [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

inp = input("Введите номер:\n")
if  inp.isdigit() and len(inp) == 10:	
	if inp in book:
			print(f"Имя:»»»»  {book[inp][0][0]} {book[inp][0][1]}\nОткуда:»»»»  {book[inp][1][0]}, {book[inp][1][1]}")			
	else:
			print("Такого номера нет в списке")		
else:
	print("Проверте правильность введенного номера")