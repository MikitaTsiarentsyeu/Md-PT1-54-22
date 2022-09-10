def prepare():
    print("Starting a new pizza making process")
    print("preparing a base")
    print("choosing a sauce")

def add_ingridient(ingridient):
    print(f"adding {ingridient}")

def grind_cheese():
    print("grinding some cheese")

def bake():
    print("baking the pizza")

def done():
    print("boxing")
    print("slicing")
    print("DONE!")


# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake()
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake()
#     done()

# def make_4chs():
#     prepare()
#     add_ingridient("parmejano")
#     add_ingridient("maasdam")
#     add_ingridient("mozarella")
#     add_ingridient("chedar")
#     grind_cheese()
#     bake()
#     done()

def pizza_factory(ingridients):
    def factory_method():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        bake()
        done()
    return factory_method

make_pepperoni = pizza_factory(["pepperoni"])
make_double_pepperoni = pizza_factory(["pepperoni", "pepperoni"])
make_4chs = pizza_factory(["parmejano", "maasdam", "mozarella", "chedar"])

make_double_pepperoni()
make_4chs()