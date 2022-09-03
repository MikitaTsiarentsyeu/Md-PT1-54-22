import random
l = [3,2,5,4,6,1,7,8]

# print(sorted(l))
# print(l)
# l.sort()
# print(l)

[3,2,5,4,6,7,9,8,1,10]
[3,2,9,4,6,7,5,8,1,10]
[3,2,9,4,6,7,5,8,10,1]
[3,4,9,2,6,7,5,8,10,1]

def random_sort(l:list):
    "sorts the list l in place"
    counter = 0
    while not is_sorted(l):
        swap(l)
        counter += 1
        print(counter)

def is_sorted(l:list) -> bool:
    "returns True if the list l is sorted, returns False otherwise"
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def swap(l:list):
    "swaps two elements of the l in place"
    i = generate_index(len(l))
    j = i
    while i == j:
        j = generate_index(len(l))
    l[i], l[j] = l[j], l[i]

def generate_index(n:int) -> int:
    "generates a randomn index based on the n"
    return random.randrange(0, n)

random_sort(l)
print(l)