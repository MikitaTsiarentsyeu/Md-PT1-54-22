def add_indents(distributed_rows, row_len, except_list):
    i, len_list = 0, len(distributed_rows)
    while len_list:
        current_strlen = len(distributed_rows[i])
        if i in except_list:
            pass    
        elif current_strlen == row_len:
            pass  
        else:
            spaces_num = distributed_rows[i].count(' ')
            dif = row_len - current_strlen
            extend_row  = '' 
            number_of_max_extensions = dif % spaces_num
            min_extension = dif // spaces_num + 1

            if spaces_num >= dif:
                extend_row = distributed_rows[i].replace(' ', 2 * ' ', dif)
                distributed_rows[i] = extend_row
            elif number_of_max_extensions == 0:
                extend_row = distributed_rows[i].replace(' ', ' ' * min_extension)
                distributed_rows[i] = extend_row           
            else:
                max_extension = min_extension + 1
                extend_row = distributed_rows[i].replace(' ', ' ' * max_extension, number_of_max_extensions)
                current_strlen += len(extend_row) - current_strlen
                ind_for_remaining_spaces = current_strlen - extend_row[::-1].find(' ' * max_extension) + 1
                distributed_rows[i] = extend_row[:ind_for_remaining_spaces] + extend_row[ind_for_remaining_spaces:].replace(' ', ' ' * min_extension)
        len_list -= 1
        i += 1
    right_text = distributed_rows
    return right_text
         