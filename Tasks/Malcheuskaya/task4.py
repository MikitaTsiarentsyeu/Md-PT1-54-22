while True:
    maxNum = input("Enter maximum number of characters per line (over 35): ")
    if maxNum == "":                    
        break
    if not maxNum.isdigit(): 
        print("Error: enter only number!")
        continue
    maxNum = int(maxNum) 
    if maxNum <= 35:
        print("Error: enter number over 35!")
        continue
    try:
        with open("text.txt", "r", encoding = "utf8") as file:
            textList =[] 
            for i in file.read().split("\n"): 
                lineList = [] 
                line = "" 
                for j in i.split(" "): 
                    if len(line + j) <= maxNum: 
                        line += j + " " 
                    else:
                        lineList.append(line.rstrip()) 
                        line = j + " " 
                lineList.append(line.rstrip()) 
                j = 0 
                while j < len(lineList) - 1: 
                    numOfSpaces = int((maxNum - len(lineList[j]))/lineList[j].count(" ")) + 1 #Вычисления минимальной длины пробелов для выравнивания строки
                    lineList[j] = lineList[j].replace(" ", " " * numOfSpaces) #Увеличение всех пробелов строки на минимальное значение
                    lineList[j] = lineList[j].replace(" " * numOfSpaces, " " * (numOfSpaces + 1), maxNum - len(lineList[j])) #увеличение пробелов для окончательного выравнивания
                    j += 1 
                textList.append(lineList) 
    except BaseException as err:
        print("Error:", err)
        break

    text = "" 
    for i in textList:
        for j in i:
            text += j + "\n" 
           
    with open ("text_new.txt", "w") as file: 
        file.write(text) 
        print("File was writed")
    
    
    
    







            
            
        



















        
