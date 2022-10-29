while True:

    number = input('Enter how much symbols are required (more than 35):\n')
    if not number.isdigit():
        print('Only numbers are allowed')
        continue
    
    number = int(number)
    
    if number < 35:
        print('Enter more than 35 symbols')
    else: break

with open("text.txt", "r") as f:
    p_list=f.read().split('\n')
    text = []
    for p in range(len(p_list)):
        words_List = iter(p_list[p].split())
        line = next(words_List)
        for word in words_List:
            if len(line) + len(word) >= number:
                text.append(line)
                line = word
            else:
                line += " " + word
        text.append(line)

new_text=[]
for w in text:
    
    if len(w) == number:
        new_text.append(w)
    if len(w) < number:
        w = w.replace(' ', ' '*2,  number - len(w))
        if len(w) < number:
            w = w.replace('  ', ' '*2, number - len(w))
        new_text.append(w)

with open("FinalText.txt", "w") as f:
    f.write("\n".join(new_text))
    print("The file has been wriiten")