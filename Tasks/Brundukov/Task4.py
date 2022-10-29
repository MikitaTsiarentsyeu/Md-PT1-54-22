while True:
    user_number = input("please, enter the length of the string (more than 35) : \n")
    if len(user_number) < 2:
        print("the format of your value is incorrect, please try again")
        continue
    if not user_number.isdigit():
        print("enter only number, please try again")
        continue
    user_number=int(user_number)
    if user_number<35:
        print("your value is less than 35, please try again")
    else:break
with open("text.txt", "r") as f:
    s=f.read()
    wordsList = iter(s.split())
    lines = []
    currentLine = next(wordsList)
    for word in wordsList:
        if len(currentLine) + 1 + len(word) > user_number:
            lines.append(currentLine)
            currentLine = word
        else:
            currentLine += " " + word
    lines.append(currentLine)
lines_2=[]
for word_2 in lines:
    if len(word_2) == user_number:
        lines_2.append(word_2)
    if len(word_2) < user_number:
        word_2 = word_2.replace(' ', '  ',  user_number - len(word_2))
        if len(word_2) < user_number:
            word_2 = word_2.replace('  ', '   ', user_number - len(word_2))
        lines_2.append(word_2)
with open("newText.txt", "w") as f:
    f.write("\n".join(lines_2))
    print("File was writed")
