from input_checking import more_than_thirty_five
from preparer import list_preparer
from distributor import row_distributor
from indents import add_indents
from final_file import output
with open("text.txt","r") as f:
    required_string_length = more_than_thirty_five()    
    sentences_list = f.readlines()
    cut_sentences = list_preparer(sentences_list)
    distributed_rows, except_list = row_distributor(cut_sentences, required_string_length)
    edited_text = add_indents(distributed_rows, required_string_length, except_list)
    output(edited_text)
    