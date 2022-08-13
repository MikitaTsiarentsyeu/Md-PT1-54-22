a = 'my test str'
b = "my test str"
c = """my test str"""
d = '''my test str'''

print(a, b, c, d)
print("'" == '"')
print(a == b == c == d)

x = """    my first line
    my second line
    my third line"""

y = "\tmy first line\n\tmy second line\n\tmy third line"

print(x)
print(y)

x = "my \"test\" s\\tr"
print(x)

"""this is a very good program
that will run on any system"""

"test"

'test'

s = "my very long string"
print(len(s))
print(len(" "))
print(len(""))

print(s[0], s[1], s[2], s[3])
print(s[len(s)-1])
# print(s[len(s)]) error
print(s[-1], s[-2], s[-3])
print(s[-len(s)])

print(s[0:7])
print(s[0:2])

print(s[3:-3])
print(s[::])
print(s[3:])
print(s[::-1])
print(s[3:-3:1])
print(s[3:-3:3])

# s[0] = "t" error
# del s[0] error

print("s" in s and " " in s)
print("long" in s)
print("test" in s)

print(s.find(" "))
print(s.find("long"))
print(s.find("long!!!!!"))

print(s.replace(" ", "___"), s)
s = s.replace("very", "not so").replace(" ", "___")
print(s)

print("my very long str".split())
print(s.split("___"))

print(list(s))

s = "34524535:adidas_superstar"
print(s.split(":"))

x = "my very long str".split()
s = "KINDA_SOME_SPACE".join(x)
print(s)

print(s.lower())
print(s.upper())
print(s.capitalize())

print("!!!test!!!".strip("!"))
print("!!!te!!st!!!".replace("!", ""))

print("454".isalpha())
print("fdfgdgf".isdigit())
print("dfsf454".isalnum())

c, d, p = "cat", "dog", "parrot"
"a cat, a dog, and a parrot"
s = "a " + c + ", a " + d + ", and a " + p
"a cat"
"a cat, a"
"a cat, a dog"
"a cat, a dog, and a"
"a cat, a dog, and a parrot"
print(s)

print("a {}, a {}, and a {}".format(c, d, p))
print("a {1}, a {2}, and a {0}".format(c, d, p))

# print("your value is %s for %d" % ("test", 88)) old style, NEVER USE

print(f"a {c}, a {d}, and a {p}")
print(f"your value is {int(25/5)}")