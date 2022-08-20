name = input("Please, enter Your name:\n")
year = int(input("Ok, how many years do You want to hold Your money in our trust bank?:\n"))

if year<=0:
    print("Seriously!? Are You a fool?!\n")
elif 0<year<=5:
    percent = 3
elif 5<year<= 15:
    percent = 5
elif 15<year<= 50:
    percent = 10
else:
    percent = 15 
    print("It's too much time, but I hope Your children will be happy.\n")
            
sum = int(input("What amount of money do You want to hold in our trust bank?:\n"))
x = year
while x!=0:
    income = sum*percent/100
    sum += income
    x -= 1

print("In",year,"years You will get", round(sum),"bucks. My congratulations!")