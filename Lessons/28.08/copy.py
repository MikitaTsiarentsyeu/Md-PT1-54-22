chunk_size = 100
counter = 0

with open("69561.jpg", 'rb') as donor:
    with open("test.jpg", 'wb') as recepient:
        while True:
            chunk = donor.read(chunk_size)
            if chunk:
                counter += 1
                print(counter)
                recepient.write(chunk)
            else:
                break

print("done!")