
from re import search


my_list = [2,4,6,8,10,12,14]

def search(l, target, low, high):
    if high >= low:
        mid = (low + high) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            return search(l, target, low, mid-1)
        else:
            return search(l, target, mid+1, high)
    else:
        return -1 # or return False, or return None

print(search(my_list, 15, 0, len(my_list)-1))
