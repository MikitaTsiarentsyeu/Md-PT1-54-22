import random
import pickle
import os

name = 'test.pickle'

if os.path.exists(name):
    with open(name, 'rb') as f:
        l = pickle.load(f)
else:
    l = []
print(l)

for i in range(100):
    l.append(random.randint(0, 100))

print(l)

with open(name, 'wb') as f:
    pickle.dump(l, f)