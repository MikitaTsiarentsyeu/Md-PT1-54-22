import os
import my_textwrap
"""created module since there are 2 versions of homework and some functions are the same in both versions"""


def split_in_lines(text):
    """create one txt-file for one line in initial txt-file. used auxiliary files since it was homework after
    files theme"""
    with open(text, 'r', encoding='utf8') as f:
        i = 1
        for line in f:
            with open(f'text {i}.txt', 'w') as f_temp:
                f_temp.writelines(line)
                i += 1
    return i


def split_lines_length(q):
    """split text in each file to lines of the prescribed length deleting old files and creating new files"""
    limit = split_in_lines(text)
    y = 1
    while y != limit:
        with open(f'text {y}.txt', 'r+') as f:
            with open(f'text_1_{y}.txt', 'w+') as f_1:
                i = 0
                m = 0
                line_q = '1'
                line = f.read()
                while q + i - m + 1 < len(line):
                    line_q = line[i:q + i - m]
                    if line[q + i - m] == ' ':
                        f_1.writelines(line_q)
                        f_1.write('\n')
                        i += q - m + 1
                        m = 0
                        if len(line[i:]) <= q + 1:
                            f_1.write(line[i:])
                    else:
                        m += 1
            y += 1
        os.remove(f'text {y - 1}.txt')
    return y


def justify_length(q, text):
    """add spaces to fit prescribed length by creating list with embeded lists"""
    final_lst = []
    limit = split_lines_length(q)
    y = 1
    while y != limit:
        with open(f'text_1_{y}.txt', 'r+') as f:
            lst = []
            for line in f:
                lst.append(line)
        for i in range(len(lst) - 1):
            lst[i] = lst[i].split()

        for i in lst[:-1]:
            len_words = 0
            for j in i:
                len_words += len(j)
            blanks = q - len_words
            counter = 0
            while counter != blanks + 1:
                for j in range(len(i) - 1):
                    if counter > blanks:
                        break
                    else:
                        i[j] = i[j] + ' '
                        counter += 1
        os.remove(f'text_1_{y}.txt')
        for i in range(len(lst) - 1):
            lst[i] = ''.join(lst[i])
        for i in lst:
            final_lst.append(i)
        y += 1

    return final_lst


q = my_textwrap.symbols_limit()
text = 'text.txt'
final_lst = justify_length(q, text)
my_textwrap.write_final_file(final_lst)
