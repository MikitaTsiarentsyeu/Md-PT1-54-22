try:
    lineSize = int(input("Enter the maximum number of characters per line, it must be greater than 35:\n"))
    if lineSize > 35:
        with open('Tasks\Lavyshyk_Olga\homework4\\text.txt', 'r') as file:
            text = file.read()
            text = text.replace('\n', ' ')
            # print(text)
            listText = text.split(' ')
            # print(listText)
            newText = ""
            tempText = ""

        for word in listText:
            if lineSize > len(tempText + word + ' '):
                tempText = tempText + word + " "
                if listText[-1] == word:
                    newText = newText + tempText + '\n'

                # print (tempText)
            else:
                tempText = tempText.strip()

                templist = tempText.split(" ")
                numSpace = len(templist) - 1
                dif = lineSize - len(tempText)
                tempText = ""
                if numSpace > dif:
                    for index, word in enumerate(templist):
                        if index == 0:
                            tempText = tempText + word
                        elif index > 0 and index < dif + 1:
                            tempText = tempText + " " + " " + word
                        else:
                            tempText = tempText + " " + word
                elif numSpace < dif:
                    val1 = int(dif / numSpace)
                    val2 = dif - numSpace * val1

                    for index, word in enumerate(templist):
                        if index == 0:
                            tempText = tempText + word
                        elif index > 0 and index < val2 + 1:
                            tempText = tempText + ((val1 + 2) * " ") + word
                        else:
                            tempText = tempText + ((val1 + 1) * " ") + word

                else:
                    for index, word in enumerate(templist):
                        if index == 0:
                            tempText = tempText + word
                        else:
                            tempText = tempText + " " + " " + word

                newText = newText + tempText + '\n'
                tempText = word + " "
        print(newText)
        

    else:
        print("The value must be greater than 35!")
except:
    print("You entered an invalid value, please try again!")

with open('Tasks\Lavyshyk_Olga\homework4\\newtext.txt', "w") as file:
    file.write(newText)
    print("File was created")


