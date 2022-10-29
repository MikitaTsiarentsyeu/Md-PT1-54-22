class Engine:

    def __init__(self, power, volume):
        self.power = power
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.__power = power

    volume = property(get_volume)
    power = property(get_power, set_power)

class Car:

    __colors = ["red", "black", "blue"]

    def __init__(self, make, model, color, engine):
        self.__make = make
        self.__model = model
        self.color = color
        self.engine = engine

    def get_make(self):
        return self.__make.capitalize()

    def get_model(self):
        return self.__model.capitalize()

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color in self.__colors:
            self.__color = color

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    make = property(get_make)
    model = property(get_model)
    color = property(get_color, set_color)
    engine = property(get_engine, set_engine)

class SuperCar:

    def __init__(self, make, model, color, power, volume):
        self.__make = make
        self.__model = model
        self.color = color
        self.__engine = Engine(power, volume)

    def get_make(self):
        return self.__make.capitalize()

    def get_model(self):
        return self.__model.capitalize()

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color in self.__colors:
            self.__color = color

    def get_engine(self):
        return self.__engine

    make = property(get_make)
    model = property(get_model)
    color = property(get_color, set_color)
    engine = property(get_engine)

e = Engine(120, 6)

c = Car("ford", "mustang", "red", e)
print(c.get_color())
print(c.get_model())

c.color = "blue"
print(c.color)
print(c.make)
print(c.model)

# c.make = "test"

c.engine = Engine(150, 6)
# c._Car__color = "green"
# print(c.get_color())

# c._Car__model = "focus"
# print(c.get_model())

print("#"*20)

class Food:

    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type

    def __str__(self) -> str:
        return self.name

class Animal:

    def __init__(self, name, color, sound) -> None:
        self.name = name
        self.color = color
        self.__sound = sound

    def eat(self, something):
        print(f"eating {something}")

    def phe(self):
        print("pheee...")

    def sleep(self, time):
        print(f"sleeping for the next {time}")

    def say_something(self, count=1):
        print(self.__sound*count)


class Carnivore(Animal):

    def eat(self, something):
        if something.type == "meat":
            Animal.eat(self, something)
        else:
            Animal.phe(self) 

class Herbivore(Animal):

    def eat(self, something):
        if something.type == "herbal":
            Animal.eat(self, something)
        else:
            Animal.phe(self)

class Omnivore(Carnivore, Herbivore):

    def eat(self, something):
        if something.type == "meat":
            Carnivore.eat(self, something)
        elif something.type == "herbal":
            Herbivore.eat(self, something)
        else:
            Animal.phe(self)

class Dog(Animal):

    def __init__(self, name, color, sound, breed):
        super().__init__(name, color, sound)
        self.breed = breed

    # def bark(self, count):
    #     print("BARK!"*count)

    def fetch(self, something):
        print(f"here's your {something}")

class Cat(Animal):

    # def meow(self, count):
    #     print("meow"*count)

    def hit_and_run(self):
        print("you're dead!")

d = Dog("Zephyrka", "white", "bark", "wss")
d.sleep("3 hours")
# d.bark(3)

c = Cat("Simba", "red", "meow")
# c.meow(3)

stake = Food("stake", "meat")
grass = Food("grass", "herbal")

leo = Carnivore("leo", "yellow", "rrrrrrrr")
cow = Herbivore("murka", "white", "muuu")
human = Omnivore("Fedor", "skin tone", "bla-bla-bla")

# leo.eat(stake)
# leo.eat(grass)

# cow.eat(stake)
# cow.eat(grass)

# human.eat(stake)
# human.eat(grass)

for animal in [leo, cow, human]:
    for food in [stake, grass]:
        print(f"{animal.name} trying to eat {food}:")
        animal.eat(food)