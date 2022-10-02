class Simple:
    pass

# print(type(Simple))

# s = Simple()
# print(type(s))

# s.test = "test"
# print(s.test)

# Simple.test = "main test value"

# s1 = Simple()
# print(s1.test)
# print(s.test)

class Dog:

    # name = "Zephyrka"
    # breed = "wss"
    # color = "white"
    
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    def sleep(self):
        print(f"I'm {self.name} and I'm sleeping")


d = Dog("Zephyrka", "wss", "white")
print(d.name, d.breed, d.color)
d.sleep()

d1 = Dog("Bucks", "shepherd", "black")
print(d1.name, d1.breed, d1.color)
d1.sleep()