while True:
    user_value = input('Введите максимальное количество символов в строке (больше 35):\n')

    failed = False
    if  not user_value.isdigit():
        failed = True
        if failed:
            print('Вы ввели значение неверно, введите цифру больше 35 еще раз.\n')
            continue
    if int(user_value) <= 35:
        print('Вы ввели значение неверно, введите цифру больше 35 еще раз.\n')
        continue
    break

max_symbols = int(user_value)

with open(r'Tasks\Galetskaya-Olga\Task4\text.txt', 'r', encoding='utf-8') as file:
    content = file.read().split('\n')
        
    new_text = []
    
    for line in content:
        len_counter = 0
        new_textline = ''
        for word in line.split():
            if len_counter + len(word) + 1 < max_symbols:
                new_textline += word + ' '
                len_counter += len(word) + 1
            elif len_counter + len(word) + 1 == max_symbols:
                new_textline += word
                new_text.append(new_textline.rstrip())
                new_textline = ''
                len_counter = 0
            elif len_counter + len(word) + 1 > max_symbols:
                len_counter = 0
                new_text.append(new_textline.rstrip())
                new_textline = ''
                new_textline += word + ' '
                len_counter = len(word) + 1
        new_text.append(new_textline.rstrip())        
    
    new_text2 = []

    for line2 in new_text:
        if len(line2) == max_symbols:
            new_text2.append(line2)
        if len(line2) < max_symbols:
            line2 = line2.replace(' ', '  ',  max_symbols - len(line2))
            if len(line2) < max_symbols:
                line2 = line2.replace('  ', '   ' , max_symbols - len(line2))
            new_text2.append(line2)
                          
    result_text = '\n'.join(new_text2) 

with open ("result_text.txt", "w", encoding='utf-8') as file: 
    file.write(result_text) 
    print("Файл записан")
