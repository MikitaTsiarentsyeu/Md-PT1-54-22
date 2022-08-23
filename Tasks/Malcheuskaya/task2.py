d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

tel = input("Enter your phone number: ")

if len(tel) == 10 and tel.isdigit():
    try:
        x = d.get(int(tel))
        print(x[0][0], x[0][1], "from", x[1][0], x[1][1]) #если d.get не нашел номер, то при попытке обратиться к х[0][0] возникает ошибка и обработка переходит в блок except
    except:
        print("The number was not found")    
else:
    print("Error: you did not enter a number")    






  


