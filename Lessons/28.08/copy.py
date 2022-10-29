chunk_size = 40
counter = 0

with open("text.txt", 'r') as donor:
    with open("text_new.txt", 'w') as recepient:
        while True:
            chunk = donor.read(chunk_size)
            if chunk:
                recepient.write(chunk + '\n')
            else:
                break

print("done!")