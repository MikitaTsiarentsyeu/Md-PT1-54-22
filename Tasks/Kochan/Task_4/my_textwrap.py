import os



def symbols_limit():
    q = input('please enter line\'s length (not less than 35 )\n')
    try:
        q = int(q)
    except:
        TypeError
        print('the entered values weren\'t figures')
        return symbols_limit()

    if int(q) < 35:
        print('the entered number was  wrong please try again')
        return symbols_limit()
    else:
        return int(q)




def len_elem(x):
    len_elem = 0
    for i in x:
        len_elem += len(i)
    return len_elem


def write_final_file(fin_line):
    with open('final.txt', 'a+', encoding='utf8') as f:
        for i in fin_line:

            if isinstance(i, str):
                i = i.rstrip('\n')
                f.write(i)
                f.write('\n')
            else:
                f.write(''.join(i))
                f.write('\n')



# def write_final_file():
#     # write requested info in final file
#     final_lst = justify_length(q)
#     with open('final.txt', 'a+', encoding='utf8') as f:
#         for i in final_lst:
#             for j in i:
#                 f.write(j)
#                 f.write('\n')