import os

print(os.name)

print(os.sep)

print(os.sep.join(['level 1', 'level 2', 'level 3']))

path = os.path.join('level 1', 'level 2', 'level 3')
print(path)

# os.makedirs(path)

print(os.listdir())
for i in os.walk(os.getcwd()):
    print(i)

initial = os.getcwd()
os.chdir(path)
print(os.getcwd())

open('test.txt', 'w')
os.remove('test.txt')

os.chdir(initial)
os.removedirs(path)