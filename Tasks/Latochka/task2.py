phonebook  = {'9103976271' : [("Reina", "Meinhard"), ("Memphis", "Tennessee")], '4199392609' : [("Stephanie", "Bruce"), ("Greensboro", "North Carolina")], '9099459979' : [("Ermes", "Angela"), ("Dallas", "Texas")], '6123479367' : [("Lorenza", "Takuya"), ("Indianapolis", "Indiana")], '7548993768' : [("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}
data = False
while data == False:
	number = input("Enter phone number, please:\n")
	if number.isdigit() and len(number) == 10:	
		if number in phonebook:
			print(f"{phonebook[number][0][0]} {phonebook[number][0][1]} from {phonebook[number][1][0]}, {phonebook[number][1][1]}")
			data = True
		else:
			print("the number was not found")
			data = True
	else:
		data = False
		print("Phone number entered incorrectly. You must enter 10 digits. Try entering your phone number again, please.")