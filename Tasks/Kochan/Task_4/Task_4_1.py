import random
import my_textwrap


def text_download(text):
    """created an auxiliary list from the text from the file"""
    lst = []
    with open(text, 'r+', encoding='utf8') as f:
        for line in f:
            line = line.split()
            lst.append(line)
    return lst


def split_lines_length(q, lst):
    """created list with the strings of prescribed length"""
    lst_line = []
    for i in lst:
        lst_temp = []
        for j in range(len(i)):
            if len(lst_temp) == 0:
                planned_length = len(i[j])
            else:
                planned_length = my_textwrap.len_elem(lst_temp) + 1 + len(i[j])
            if planned_length < q:
                if j + 1 <= len(i) - 1 and planned_length + len(i[j + 1]) + 1 < q:
                    lst_temp.append(i[j])
                    lst_temp.append(' ')
                elif j + 1 <= len(i) - 1 and planned_length + len(i[j + 1]) + 1 > q:
                    lst_temp.append(i[j])
                    lst_line.append(lst_temp)
                    lst_temp = []
                elif j + 1 > len(i) - 1:
                    lst_temp.append(i[j])
                    lst_line.append(''.join(lst_temp))
            elif planned_length > q:
                if j + 1 <= len(i) - 1:
                    lst_temp = []
                    lst_temp.append(i[j])
                    lst_temp.append(' ')
                elif j + 1 > len(i) - 1:
                    lst_line.append(lst_temp)
                    lst_temp = []
                    lst_temp.append(i[j])
                    lst_temp.append(' ')
                    lst_line.append(lst_temp)
    for i in lst_line:
        """since high preciseness wasn't prescribed decided tu use randomness"""
        if isinstance(i, list):
            spaces_missing = q - my_textwrap.len_elem(i)
            for k in range(spaces_missing):
                ind_random = int(random.randrange(1, len(i) - 1, 2))
                i.insert(ind_random, ' ')
    return lst_line



lst = text_download('text.txt')
q = my_textwrap.symbols_limit()
fin_line = split_lines_length(q, lst)
my_textwrap.write_final_file(fin_line)
