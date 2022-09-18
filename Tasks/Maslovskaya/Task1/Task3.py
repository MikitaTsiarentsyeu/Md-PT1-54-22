import os

read_file='' 
cursor=0
fl = True

def reading_file(cursor):
 
    while True:
        with open("text.txt",'r+',encoding='UTF-8') as f:
            
            f.seek(cursor)
            d = list(f.read(slice+1))
            f.seek(cursor)

            if len(d)<slice+1:
                read_file = f.read(len(d))
                write_in_file(read_file)
                print(f'The work is done!\nFormatted to a line width of {slice} characters text is written in text1.txt file in this folder.')
                global fl
                fl=False
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
                    print(f"Can not format to a line width of {slice} characters text from the text.txt file because some of words in it have {max_len} characters length. Please, try again. ")
                    fl=True
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
    
def write_in_file(read_file):
    with open("text1.txt",'a+',encoding='UTF-8') as f:   
        f.write(read_file)
        f.write('\n')


def validation(slice):
    try: 
        int(slice)
    except ValueError:
        print("Entered value isn't correct. You can use only poitive numbers. Please, try again.")
        return False
    else:

        # Here I really did not understand at all why the maximum number of characters is 105. If you enter 106, an error occurs 
        # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte in python.
        # What does it mean? And how to solve this problem? Google didn't help me in this question :(

        if int(slice)>106:
            print("Entered value too big. The maximum line width can be 105 characters. Please, try again.")
            return False
        elif int(slice)<0:
            print("Entered value isn't correct. You can use only poitive numbers. Please, try again.")
            return False
        else:
            return True   

while fl:
    slice=input("Enter the line width (use only poitive numbers) to format the text from the file text.txt:\n")
    while validation(slice)!=True:
        slice= input("Enter the line width (use only poitive numbers) to format the text from the file text.txt:\n") 
    slice = int(slice)
    cursor=0
    cursor=reading_file(cursor)









