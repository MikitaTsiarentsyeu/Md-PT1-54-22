p = 1
while p < 2:
    Symbols = input("\033[1m\nPlease, enter the value of symbols in line (enter a value above then 35 symbols):\033[0m\n")
    try:
        check = float(Symbols)
    except ValueError:
        print("\n\033[1;31mPlease, enter a numerical value\033[0m\n")
    else:
        if int(Symbols) <= 35:
            print("\n\033[1;31mPlease, enter a numerical value above 35\033[0m\n")
        else:
            p = 2
Symbols = int(Symbols)
a = Symbols
with open ("text.txt", "r") as donor:
        List = donor.read().replace('вЂ™', "'").replace('вЂњ', '"').replace('вЂќ', '"').split('\n')
New_List = []
for i in range(len(List)):
    a = Symbols
    while True:
        if len(List[i]) <= a:
            NewLine = List[i]
            New_List.append(NewLine)
            break
        else:
            if List[i][a] == ' ':
                NewLine = List[i][:a]
                List[i] = List[i].replace(NewLine, '')
                List[i] = List[i].lstrip()
                if Symbols - len(NewLine) == 0:
                    New_List.append(NewLine)
                else:
                    x = Symbols - len(NewLine) #need spaces
                    y = len(NewLine) - len(NewLine.replace(' ', '')) #count of spaces
                    z = ' '*(x//y+1) + '|'
                    NewLine = NewLine.replace(' ', z)
                    if len(NewLine.replace('|','')) == Symbols:
                        New_List.append(NewLine.replace('|',''))
                    else:
                        b = Symbols - len(NewLine.replace('|',''))
                        c = 0
                        while c < b:
                            NewLine = NewLine.replace("|", " ", 1)
                            c = c + 1
                        New_List.append(NewLine.replace('|',''))
                    a = Symbols            
            else:
                a = a - 1
with open ("newtext.txt", "w") as rec:
    for i in range(len(New_List)):
        NewLine = New_List[i]
        rec.write(NewLine + '\n')
List.clear()
New_List.clear()