data = False
while data == False:
    number = input("Enter the desired maximum number of characters per line. The value must be greater than 35:\n")
    if  not number.isdigit():
        print("The data entered is incorrect. You must enter a number greater than '35'. Try entering the data again, please.")
        data = False
    elif int(number) <= 35:
        print("Data entered incorrectly. The value must be greater than '35'. Try entering the data again, please.")
        data = False
    else:
        data = True
number = int(number)
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
    words = iter(text.split())
    lines = []
    readable_line = next(words)
    for word in words:
        if len(readable_line) + 1 + len(word) > number:
            lines.append(readable_line)
            readable_line = word
        else:
            readable_line += " " + word
    lines.append(readable_line)
next_lines = []
for next_word in lines:
    if len(next_word) == number:
        next_lines.append(next_word)
    if len(next_word) < number:
        next_word = next_word.replace(' ', '  ',  number - len(next_word))
        if len(next_word) < number:
            next_word = next_word.replace('  ', '   ', number - len(next_word))
        next_lines.append(next_word)
with open("task4.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(next_lines))
    print("Your file has been written.")