while True:
    l = input("Enter the length of the string (minimum 36 characters): ")
    if l.isdigit() is True and int(l) > int(35):
        with open('text.txt', 'r') as donor:
            with open('result.txt', 'w') as recepient:
                text = donor.read().split()
                list = []
                for i in text:
                    if int(l) - len(' '.join(list)) > len(i):
                        list.append(i)                                     
                    elif int(l) - len(' '.join(list)) <= len(i):
                        list
                        while len(''.join(list).rstrip()) < int(l):
                            for i1, v in enumerate(list):
                                if len(''.join(list).rstrip()) == int(l):
                                    break
                                if v != ' ' and len(''.join(list).rstrip()) < int(l):
                                    list.insert(i1+1, ' ')
                        recepient.write(''.join(list).rstrip() + '\n')
                        list = [i]
                recepient.write(''.join(list).rstrip())                     
    else: 
        False
        print("Wrong data format: only numbers can be entered and min value is \"36\". Please try again.")
        continue
    l2 = input("""The text with the updated line length is saved in a new file. 
    Do you want to set a new string length? Enter Y(yes) or N(no): """)
    if l2.upper() == "Y":
        True
    elif l2.upper() == "N":
        print("Have a good day!")
        break
    elif l2 != "Y" or l2 != "N":
        print("Wrong answer! Enter only \"Y\" or \"N\"")
        continue
    
    