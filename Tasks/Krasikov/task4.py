while True:
    width = (input('Please enter ur width > 35 symbols:\n'))
    if not width.isdigit():   #валидация на числа
        print('Please enter digits in ur width\n')
        continue
    width = int(width) #строку в целочисленное
    if width <= 35: #валидация на кол-во символов
        print('error.Just width >35.\n')
        continue
    break      
with open('text4.txt', 'r', encoding = 'utf-8') as g:    #открытие исходника для чтения
    with open('fix_text4.txt', 'w', encoding = 'utf-8') as g_new:   #открытие нового файла для запииси
        text = g.read().split()    #прочли и разделили по пробелам
        string = [] #создали пустой список
        print(len(''.join(string)))
        for word in text:           #начали цикл для каждого слова в списке text
            if width - len(''.join(string)) >= len(word):  #если длина пользователя - длина сложенных слов без пробелов больше или равна длину слова
                string.append(word), string.append(' ')  #то в список добавляется слово и пробел
            else:   #иначе
                string.pop() #последнее удаляется из списка
                while len(''.join(string).rstrip()) != width: # пока длина всех символов строки с удаленными последними пробелами не равна длине пользователя
                    for i, symbol in enumerate(string):
                        if len(''.join(string).rstrip()) == width: # если длина всех символов строки с удаленными последними пробелами равна длине строки
                            break #стоп
                        if symbol != ' ': # если переменная символ не равна пробелу
                            string.insert(i + 1, ' ') #в список вставляется пробел в позицию с индексом + 1 отличного от номера повторения
                g_new.write(''.join(string) + '\n') 
                string = [word, ' ']
        g_new.write(''.join(string)) #запись в новый файл
print('Check ur new txt file')