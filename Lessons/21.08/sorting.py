l = [3,2,4,5,8,7,6,1]

# l_sorted = sorted(l)
# print(l_sorted, l)

# l.sort(reverse=True)
# print(l)

# print(sorted("ccc aaa bbb".split()))

# print(sorted([[7,8,9], [1,2,3], [4,5,6]]))


# for j in range(len(l)-1):
#     for i in range(len(l)-j-1):
#         if l[i]>l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
#     print(l)


for j in range(len(l)-1):
    min = j
    for i in range(j, len(l)):
        if l[i] < l[min]:
            min = i
    l[j], l[min] = l[min], l[j]
    print(l)