index_prefix = "station101"
pet_list = {}
pet_count = 0

def generate_key(index):
    return index_prefix+str(index)

def add_pet(index, breed, name):
    key = generate_key(index)
    pet_list[key] = (name, breed)
    global pet_count
    pet_count += 1

def remove_pet(index):
    key = generate_key(index)
    if key in pet_list:
        del pet_list[key]
        global pet_count
        pet_count -= 1

add_pet(4685138, "shepherd", "zephirka")
add_pet(14861383, "kolly", "kolya")
add_pet(1843843, "british", "tom")

remove_pet(14861383)

print(pet_list, pet_count)