
def check_str(String):
    Up, Down = 0, 0
    for Symbol in String:
        if Symbol.isupper():
            Up+=1
        elif Symbol.islower():
            Down+=1
        else:
            continue
    return f"{Up} upper case,{Down} lower case"

def is_prime(Number):
    if Number == 1:
        return("False")
    else:
        i, j = 2, 1
        while i < Number and j == 1:
            if Number%i == 0:
                j+=1
                i+=1
            else:
                i+=1
        if j == 1:
            return("True")
        else:
            return("False")

def get_ranges(List):
    List2 = []
    a = 1
    while True:
        if len(List) == 0:
            break
        elif len(List) == 1:
            List2.append(List[0])
            List.pop(0)
            break
        else:
            while True:
                if len(List) > a and List[0] + a == List[a]:
                    a+=1
                elif a > 1:
                    List2.append(f"{List[0]}-{List[a-1]}")
                    for i in range(a):
                        List.pop(0)
                    a = 1
                    break
                else:
                    List2.append(List[0])
                    List.pop(0)
                    break
    return str(List2).replace('[','"').replace(']','"').replace("'",'')