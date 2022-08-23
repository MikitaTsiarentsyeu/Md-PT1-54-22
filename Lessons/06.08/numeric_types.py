import decimal
import fractions
import math
import random

x = 5
print(type(x), x)

print(5+5)
print(5-5)
print(5*5)
print(5**5)
print(10%6)
print(5/5)
print(5//3)

print(int(2.8))
print(int(-2.8))

x = 2.8
print(type(x), x)

print(5.0+5.0)
print(5.5-5.4)
print(5.25*5.25)
print(256**0.5)
print(10.5%6)
print(5/5)
print(5.5//3.3)

print(float(3))
print(float('3.125'))

print(round(3.5))
print(round(4.5))
print(round(5.5))
print(round(6.5))

print(3.3==3.3)
print(1.1+1.1+1.1==3.3)
print(1.1+1.1+1.1)


x = decimal.Decimal(1.1)
y = decimal.Decimal(3.3)

print(x+x+x==y)
print(x)
print(x+x+x)

x = decimal.Decimal('1.1')
y = decimal.Decimal('3.3')

print(x+x+x==y)
print(x)
print(x+x+x)
print(repr(x), type(x))

print(type(3+x))
print("string"*4)


x = fractions.Fraction(2, 3)
print(type(x), x)

x = fractions.Fraction(5, 10)
print(type(x), x)

x = fractions.Fraction(2.8)
print(x)

x = fractions.Fraction('2.8')
print(x)

print(math.cos(math.pi))
print(math.sqrt(256))
print(math.pow(5, 3.25))
print(math.factorial(6))


print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

print(random.randrange(1, 10))

l = [1,2,3,4,5,6,7,8,9]
random.choice(l)
random.shuffle(l)
print(l)