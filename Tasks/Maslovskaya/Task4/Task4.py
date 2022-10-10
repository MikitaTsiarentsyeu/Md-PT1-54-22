import os

read_file='' 
flag = True

def write_in_file(read_file):
    with open("text1.txt",'a+',encoding='UTF-8') as f:   
        f.write(read_file)
        if flag:
            f.write('\n')

def reading_file(cursor):
 
    while True:
        with open("text.txt",'r+',encoding='UTF-8') as f:
            
            f.seek(cursor)
            d = list(f.read(slice+1))
            f.seek(cursor)

            if len(d)<slice+1:
                read_file = f.read(len(d))
                global flag
                flag=False
                write_in_file(read_file)
                print(f'The work is done!\nFormatted to a line width of {slice} symbols text is written in text1.txt file in this folder.')

                break
                
            elif '\n' in d:
                read_file = f.read(d.index('\n')).strip()
                f.seek(f.tell()+1)

            else:
                spaces = [j for j in range(slice,-1,-1) if d[j] == ' ']

                if spaces==[]:
                    os.remove("text1.txt")
                    f.seek(0)
                    max_len = max(len(word) for word in set(f.read().split()))
                    print(f"Can't format to a line width of {slice} symbols text from the text.txt file because some of words in it have {max_len} characters length. Please, try again. ")
                    flag=True
                    break
                
                elif spaces[0]==slice:
                    read_file = f.read(spaces[0])
                
                elif len(spaces)==1:
                    read_file = f.read(spaces[0])                 
                        
                elif spaces[0]<slice and len(spaces)>1:
                    
                    read_file = f.read(spaces[0]).replace(' ','  ',slice-spaces[0])
                    ps=len(read_file)
                    
                    while ps!=slice:
                        read_file = read_file.replace('  ','   ',slice-ps)
                        ps=len(read_file)

            cursor=f.tell()+1
            write_in_file(read_file)

        return reading_file(cursor)

# Here I really did not understand at all why the maximum number of symbols is 105. If you enter 106, an error occurs 
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte in python.
# What does it mean? And how to solve this problem? Google didn't help me in this question :(   
    
def validation():
    slice=input("Enter the line width (use only poitive numbers) to format the text from the file text.txt:\n")
    if slice.isdigit():
        if int(slice)<106 and int(slice)>0:
            return int(slice)
        elif int(slice)>105:
            print("Range too big. Maximum line width 105 symbols. Please, try again.")
            return validation()
    print("Entered value isn't correct. Please, try again.")
    return validation()

while flag:
    cursor=0
    slice=validation()
    cursor=reading_file(cursor)







