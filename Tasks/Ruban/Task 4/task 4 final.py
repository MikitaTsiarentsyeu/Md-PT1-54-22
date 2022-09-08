while True:
    mxsym = input('Please input preferred number of characters in one line (>35) \n')
    if mxsym.isdigit() == False:
        print('Incorrect input. Please try again')
    else: 
        mxsym = int(mxsym)    
        if mxsym < 36:
            print('Minimum number of characters is 36. Please try again')
        else:    
            break        
with open("text.txt", 'r', encoding='utf8') as f:
    s = f.read()
    f.close()

m = list(s.split('\n'))             #list of paragrhaphs
listfinal = []                      #final unformatted list of lists of paragraphs splitted by strings
listform = []                       #final formatted list

for i in range(len(m)):
    strg = m[i]
    lenres = len(strg)
    liststrg = []                   #list of paragraph strings
    while lenres > 0:
        if len(strg) >= mxsym:
            ind = strg.rfind(' ', 0, mxsym) + 1
            s1 = strg[0:ind]
            s1 = s1.rstrip()      
            liststrg.append(s1)
            strg = strg[ind:]        
        elif 0 < len(strg) < mxsym:
            liststrg.append(strg)
            strg = ''
        lenres -= ind
    listfinal.append(liststrg)    

for j in range(len(listfinal)):
    for k in range(len(listfinal[j])):
        finalstrg = listfinal[j][k]
        if k == len(listfinal[j]) - 1 or mxsym == len(finalstrg):
            listform.append(finalstrg)
        else:
            dif = mxsym - len(finalstrg)
            counter = 0
            spaceind = finalstrg.find(' ')
            t = 2                               #default value for of index increase for searching new space
            while counter != dif:
                finalstrg = finalstrg[:spaceind] + ' ' + finalstrg[spaceind:]
                spaceind = finalstrg.find(' ', spaceind + t)
                if spaceind == -1:
                    spaceind = finalstrg.find(' ')
                    t += 1        
                counter += 1
            listform.append(finalstrg)    

txtready = open("text_formatted.txt", "w+", encoding='utf8')
for  line in listform:
        txtready.write(line + '\n')
txtready.close()


        


    



      