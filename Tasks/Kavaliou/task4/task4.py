while True:
    length = input("enter the character limit for the string length, minimum '35':\n")
    if length.isdigit() != True:
        print("Error. Enter a number, please")
        continue
    length = int(length)
    if length <= 35:
        print("Error. The number you enter should should be 35 or more")
        continue
    break

with open("text.txt", 'r', encoding="utf-8") as text_before:
    with open("final_text.txt", 'w', encoding="utf-8") as text_after:
        for line in text_before:
            current_line = line.split()
            while len(' '.join(current_line)) > length:
                word = [current_line.pop(0)]
                len_words = len(' '.join(word))
                while len_words < length:
                    next_word_len = len(current_line[0])
                    if len_words + next_word_len + 1 > length:
                        break
                    word.append(current_line.pop(0))
                    len_words += next_word_len + 1
                space = length - len_words
                while space != 0:
                    for i in range(len(word) - 1):
                        if space == 0:
                            break
                        word[i] += ' '
                        space -= 1
                text_after.write(' '.join(word) + '\n')
            text_after.write(' '.join(current_line) + '\n')
print("Check your new formatted file: final_text.txt")
