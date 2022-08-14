s = {1,3,5}
print(s, type(s))

s = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
print(s)

s = set()
print(s, type(s))

print(list("test"))
print(set("xdfgjokljhgfdsdfghjko"))

l1 = [1,2,3,3,3,3,3,]
l2 = [3,2,1]
print(l1 == l2)
print(set(l1) == set(l2))

s = "txcuyil;jhgukdtsrfgjklj;jiuhkgydrsfghjkl;kjitfdfghjklkjhgfd"
st = set(s)
print(len(s)-len(st))