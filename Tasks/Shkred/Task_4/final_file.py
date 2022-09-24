def output(fixed_rows):
    with open("edited.txt", 'w') as edited_file:  
            for row in fixed_rows:
                edited_file.write(row + '\n') 
    print("Your final text in edited.txt file!")
