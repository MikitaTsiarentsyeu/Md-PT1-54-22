database = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
            4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
            9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
            6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
            7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

def validation():
    flag = False
    while not flag:
        inp=input("Enter 10 values of phone number:\n")
        if len(inp)==10 and inp.isdigit():
            flag = True          
    return inp

while True:
    s=int(validation())
    if s in database:
        print(f"{database[s][0][0]} {database[s][0][1]} from {database[s][1][0]} , {database[s][1][1]}")
    else:
        print("the number was not found")    

    question = input("press Y if you want to comlete:\n")
    if question.upper() !='Y':
        break