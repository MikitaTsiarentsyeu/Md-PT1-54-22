counter = 0

while counter < 10:
    counter += 1
    print(counter)

print("the end")

l = [0.0,1,2,3,4,5,"test"]

for i in l:
    print(i)

print(f"the last value of i - {i}")

index = 0
while index < len(l):
    print(l[index])
    index += 1

for index in range(len(l)):
    print(l[index])


for i in range(0, 11, 2):
    print(i)

for i, e in enumerate("some string"):
    print(i, e)

i = 2
for i in {1,2,3,4,5}:
    print(i)

d = {"one":1, "two":2, "three":3}
for i in d:
    print(i, d[i])

for k, v in d.items():
    print(k, v)

for v in d.values():
    print(v)

print("---------------------------")

for i in l:
    print(i)
    print(l.pop())

print(l)

# l = [1]
# for i in l:
#     l.append(1)
#     print(l)


# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i > 5:
#         break
#     print(i)

for i in range(10):
    print("the start of iteration")
    print(i)
    continue
    print("the end of iteration")

l = [0.0,1,2,3,4,5,"test"]
i = 0
while True:
    if i == len(l):
        break
    if i % 2 == 0:
        i += 1
        continue
    print(l[i])
    i += 1

for i in range(10):
    print(i)
    if i > 3:
        break
else:
    print("the end")



l = [3,7,5,2,1,3,56,8,0,87,5,2]

min = l[0]
for i in l:
    if i == min:
        continue
    if i < min:
        min = i
print(min)