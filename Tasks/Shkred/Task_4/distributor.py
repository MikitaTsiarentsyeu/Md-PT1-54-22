def row_distributor(cut_sentences, row_len):
    i, counter, row_collection, except_list = 0, 0, [], []
    while i < len(cut_sentences):
        row_length = len(cut_sentences[i])
        row, length, j = '', 0, 0 
        while row_length:
            if cut_sentences[i][j] == cut_sentences[i][-1]:
                if length + len(cut_sentences[i][j]) <= row_len:
                    except_list.append(counter)
                    row += cut_sentences[i][j] 
                    row_length -= 1
                    row_collection.append(row)
                    counter += 1
                    break 
                else:
                    row_collection.append(row[:-1])
                    counter += 1
                    row, length = '', 0    
                    j -= 1
            elif length + len(cut_sentences[i][j])  <= row_len:         
                row += cut_sentences[i][j] + ' '
                length += len(cut_sentences[i][j]) + 1
                row_length -= 1
            else:
                row_collection.append(row[:-1])
                counter += 1
                j -= 1
                row,length ='', 0    
            j += 1
        i += 1
    return row_collection, except_list
        