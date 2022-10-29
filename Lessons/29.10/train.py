class FreightTrain:

    def __init__(self, cart_count):
        self.cart_count = cart_count

    def __str__(self):
        return f"I'm a train with {self.cart_count} carts, choo-choo!"

    def __len__(self):
        return self.cart_count

    def __eq__(self, other):
        if not isinstance(other, FreightTrain):
            return False

        return self.cart_count == other.cart_count   

    def __add__(self, other):
        try:
            return FreightTrain(self.cart_count+other.cart_count)
        except:
            raise TypeError("cannot add non-FreightTrain object")

train = FreightTrain(10)
print(train)

print(len(train))

loooooooong = FreightTrain(35)
print(train == loooooooong)

print(loooooooong + train == FreightTrain(45))