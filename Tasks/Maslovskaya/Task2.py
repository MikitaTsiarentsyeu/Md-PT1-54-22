d={9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],6123479367:[("Lorenza", "Takuya"),("Indianapolis", "Indiana")],7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

def is_number(x):
    try: 
        int(x)
    except ValueError:
        print("Entered value isn't correct. Please, try again.")
        return False
    else:
        if len(x)==10:
            return True
        else:
            print("Entered value isn't correct. Please, try again.")
            return False

x=(input("Hello. If you want to find an owner of a phone number, please, enter it:\n"))
while is_number(x)!=True:
    x= input("Enter the correct number (only 10 digitals):\n") 


def my_func(x):
    return d.get(x,'not found')

g=my_func(int(x))

if g=='not found':
    print("Sorry, the phone number was not found.")
else:
    print(f"The owner of this phone number is {g[0][0]} {g[0][1]} from {g[1][0]}, {g[1][1]}")