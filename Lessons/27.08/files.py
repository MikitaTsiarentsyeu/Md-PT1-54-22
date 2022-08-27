# f = open("test.txt", 'w')
# print(f, type(f))
# f.write("some test content")
# f.close()

with open("test.txt", 'w') as very_important_file:
    very_important_file.write("new test content ")
    very_important_file.write("another content\n")
    very_important_file.writelines(["line 1\n", "line 2\n", "line 3\n"])
    # very_important_file.read() error


with open("test.txt", 'r') as f:
    for l in f:
        print(l)
    # print(f.readlines())
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # f.seek(9)
    # print(repr(f.read(5)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10000)))
    # print(repr(f.read()))
    # f.seek(0)
    # print(repr(f.read()))


with open("test.txt", 'a') as f:
    f.write("appended content\n")
    # f.seek(0)
    # f.write("prepended content") writing to end anyway
    # f.read()

with open("test.txt", 'a+') as f:
    f.write("appended content\n")
    f.seek(0)
    # f.write("prepended content")
    print(repr(f.read()))


with open("test.txt", 'r+') as f:
    f.write("text from read mode")
    print(f.read())

with open("test.txt", 'w+') as f:
    f.write("totally new content")
    f.seek(0)
    f.write("test")
    print(f.read())