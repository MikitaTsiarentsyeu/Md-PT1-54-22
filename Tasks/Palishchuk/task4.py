while True:
    num = input('Please, enter a count of the characters (over 35): ')
    
    if not num.isdigit():
        print("Please, enter a numbers only (over 35)")
        continue

    num = int(num)
    if num < 35:
        print("The count of the characters must be at least 35 characters")
        continue

    try:
        with open('text.txt', 'r') as file:
            text = file.readlines()
            result = ""

            for line in text:
                line = line.replace("вЂ™", "'").replace('вЂњ', '"').replace('вЂќ', '"')

                while line != "":
                    
                    if len(line) > num:
                        index_of_last_space = line.rfind(" ", 0, num)
                        sub_line = line[:index_of_last_space]
                        line = line[index_of_last_space:].lstrip()   
                        words = sub_line.split(" ")
                        amount_of_words = len(words)
                        not_space_symbols = len(sub_line.replace(" ", ""))
                        amount_of_spaces = num - 1 - not_space_symbols

                        if amount_of_words > 1:
                            count_of_spaces_between_words = int(amount_of_spaces / (amount_of_words - 1))
                            count_of_long_spaces = amount_of_spaces % (amount_of_words - 1)

                            counter = 0
                            for word in words:
                                result += (word + (" " * count_of_spaces_between_words))

                                if counter < count_of_long_spaces:
                                    result += " "
                            
                                counter += 1

                        else:
                            result += words[0]
                    
                    else:
                        result += line
                        line = ""
                    
                    result = result.rstrip() + "\n"
            
            result = result.rstrip("\n")
    
    except:
        print("The file doesn`t exist")

    with open("text_copy.txt", "w") as new:
        new.write(result)
        print("A new formatted copy has been written")