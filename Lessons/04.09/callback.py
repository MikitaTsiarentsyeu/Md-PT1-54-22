def apply_to_coll(coll, func):
    for i in coll:
        print(repr(func(i)))

def sq(x):
    return x*x

apply_to_coll([1,2,3,4,5], str)
apply_to_coll([1,2,3,4,5], float)
apply_to_coll([1,2,3,4,5], sq)