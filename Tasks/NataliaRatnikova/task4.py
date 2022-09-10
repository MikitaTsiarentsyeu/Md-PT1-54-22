while True:
    required = input('please enter the length of the string you would like to have, at least 35 symbols:\n')
    if required.isdigit() == False:
        print('The ammount of symbols should be a number, please try again')
        continue
    if int(required) < 35:
        print('The amount of symbols shoul be more then 35, please try again')
        continue
    break

required = int(required)

with open(r'/Users/natalaratnikova/Documents/GitHub/Md-PT1-54-22/Tasks/NataliaRatnikova/text.txt', 'r', encoding='UTF-8') as f: 
    file_lines = f.read().split('\n')

final_text = ''

for current_file_line in file_lines:
    words = current_file_line.split(' ')
    line = 0
    new_lines = [[words[0]]]
    current_length = len(words[0])
    for current_word in words[1:]:
        if current_length + len(current_word) + 1 < required:
            current_length += len(current_word) + 1
            new_lines[line].append(current_word)
        else: 
            new_lines.append([current_word])
            current_length = len(current_word)
            line += 1

    for i in range(len(new_lines)):
        current_line = new_lines[i]
        line_length = 0
        for current_word in current_line:
            line_length += len(current_word)
        while line_length < required:
            word_count = len(current_line) - 1
            if  word_count == 0:
                word_count = 1
            for j in range(word_count):
                current_line[j] = current_line[j] + ' '
                line_length += 1
                if line_length >= required:
                    break

    for current_line in new_lines:
        final_text += '\n' + ''.join(current_line)

final_text = final_text[1:]

print(final_text)   

with open (r'/Users/natalaratnikova/Documents/GitHub/Md-PT1-54-22/Tasks/NataliaRatnikova/final_text.txt', "w", encoding='UTF-8') as final: 
     final.write(final_text[1:]) 
     print("The file have been written")