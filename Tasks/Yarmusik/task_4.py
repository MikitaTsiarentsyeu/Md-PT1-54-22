width = input('Number: ')
if width.isdigit() and int(width) > 35:
    width = int(width)
    full_text = []

    write_file = open('text1.txt', 'w')

    with open('text.txt', 'r') as read_line:
        for line in read_line:
            lineLength = len(line)
            words = line.split(' ')
            index = 0
            new_line = ''
            for pos in range(0, lineLength, width):
                while index < len(words) and (len(new_line) + len(words[index]) + 1) <= width:
                    if len(new_line) != 0 and words[index] != ' ':
                        new_line += " "
                    new_line = new_line + words[index]
                    index = index + 1
                while len(new_line) < width and new_line.find(' ') != -1:
                    diff = width - len(new_line)
                    new_line = new_line.replace(" ", "  ", diff)

                full_text.append(new_line + '\n')
                new_line = ''

            if index < len(words) and words[index] != '':
                new_line = words[index]
                full_text.append(new_line)
    write_file.writelines(full_text)
else:
    print('Error 500')