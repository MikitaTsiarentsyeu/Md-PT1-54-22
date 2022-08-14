d = {}
print(d, type(d))

d = {"one":1, "two":2.0, 3:"three"}
print(d)

print(d["one"])
print(d[3])

d[1.0] = "one"
print(d)

d[1.0] = 1
print(d)

print(d.keys())
print(list(d.values())[0])
print(d.items())

print(1.0 in d)
print(1 in d.values())

# d["some key"] error
x = d.get("some key", "the key was not found")
print(x)

x = d.get("one", "the key was not found")
print(x)

print(d.pop("one"))
print(d)

print(d.popitem())
print(d)

del d["two"]
print(d)

del d