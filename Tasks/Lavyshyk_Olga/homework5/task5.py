def check_str(str1):
    countLower = 0
    countUpper = 0

    for char in str1:

       if char.islower():
           countLower += 1
       elif  char != " ":
        continue
       else:
           char.isupper()
           countUpper +=1

    return (countLower , countUpper)

str1 = ""
result = check_str(str1)
#print(f"{result[1]} upper case, {result[0]} lower case")




def is_prime(num): 

    for i in range(2, num):
        if  i % num == 0:
            return False
        else:
            return True
        return num



def get_ranges(l):
    flag = False
    resalt = ""
    for i in range(0,len(l)-1):
        if l[i + 1] - l[i] == 1:

            if not flag:
               resalt = resalt + str(l[i]) + "-"
               flag = True
            else:
                continue

        if l[i + 1] - l[i] != 1:

            if flag:
               resalt = resalt + str(l[i]) + ","
               flag = False
            else:
                resalt = resalt + str(l[i]) + ","

    return (resalt + str(l[-1]))

get_ranges([[]])
