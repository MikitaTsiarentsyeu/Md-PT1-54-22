def times(a, b):
    return a*b

def times(a:int, b:int) -> int:
    "this function will multiply only int values"
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times(2,4))
print(times([2],4))
print(times('2',4))

def eq(coll1, coll2):
    for i in coll1:
        if i not in coll2:
            return False
    for i in coll2:
        if i not in coll1:
            return False
    return True

print(eq([1,2,3], [3,2,1,1,1,1,1,1]))
print(eq((1,2,3), [3,2,1]))
print(eq("123", ['3','2','1']))

# def space_sum(coll):
#     res = 0
#     for i in coll:
#         if i == ' ':
#             res+=1
#     return res

def space_sum(coll, elem):
    res = 0
    for i in coll:
        if i == elem:
            res+=1
    return res

print(space_sum("", ' '))
print(space_sum("word word word", 'w'))
print(space_sum([1,2,3,' ',5], 2))
