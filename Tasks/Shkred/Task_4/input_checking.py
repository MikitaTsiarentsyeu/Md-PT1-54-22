def more_than_thirty_five():
    flag = False
    while not flag:
        try:
            row_length = int(input("Enter an integer greater than 35:\n"))
            if row_length > 35:
                flag = True 
        except:
            print("Your input isn't integer, try again")
    return row_length
    