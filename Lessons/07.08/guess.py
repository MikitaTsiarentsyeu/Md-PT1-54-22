import random

my_number = random.randint(0, 10)

your_number = int(input("Guess my number (from 0 to 10):\n"))

if your_number == my_number:
    print("The number is correct!")
else:
    print("You are a looooooser!")