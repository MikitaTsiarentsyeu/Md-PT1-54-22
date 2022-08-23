List = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

p = 1
while p < 2:
    x = input("Please, enter the telephone number:\n")
    try:
        check = float(x)
    except ValueError:
        print("\n\033[1;31mPlease, enter a numerical value\033[0m\n")
    else:
        if len(x) == 10:
            p = 2
        else:
            print("\n\033[1;31mPlease, enter a proper count of symbols\033[0m\n")
x = int(x)
y = List.get(x)
if y == None:
    print("\n\033[1mThe number was not found\033[0m\n")
else:
    print(f"\n\033[1;32m{y[0][1]} {y[0][0]} from {y[1][0]}, {y[1][1]}\033[0m\n")
    y = List.get(x)