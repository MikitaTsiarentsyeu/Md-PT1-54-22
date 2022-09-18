

# print(test)
l = []

try:
    raise RuntimeError("demonstration of the raise operator working")
    try:
        print(test)
    except:
        print("something went wrong")
    l[0]
    print("after the error")
except NameError:
    print("the variable does not exist")
except IndexError:
    print("some index error occured")
except Exception as er:
    print("generic exception")
    print(er)
finally:
    print("this block runs every time")



print("the main logic")

with open("test.txt") as f:
    f.read()

try:
    f = open("test.txt")
    f.read()
finally:
    f.close()