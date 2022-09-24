def list_preparer(collection):
    for i in range(len(collection)):
        sentence_editor = collection[i][:-1].replace("вЂ™","'").replace("вЂњ",'"').replace("вЂќ",'"').split()
        collection[i] = sentence_editor
    return collection 
        