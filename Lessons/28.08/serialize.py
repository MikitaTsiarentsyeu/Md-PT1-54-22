import json
import pickle
import csv

s = '{"width":3840,"height":2100,"resolution":90,"quality":90,"settings":[{"filename":"_largePreview1.jpg","seek":10},{"filename":"_largePreview2.jpg","seek":35},{"filename":"_largePreview3.jpg","seek":70},{"filename":"_largePreview4.jpg","seek":95}]}'

my_obj = json.loads(s)
print(type(my_obj), my_obj)

print(my_obj["settings"][0]["seek"])
my_obj["settings"][0]["seek"] = 15

print(json.dumps(my_obj))

with open("test.json", 'w') as f:
    json.dump(my_obj, f)

my_obj["settings"] = tuple(my_obj["settings"])
with open("test.json", 'w') as f:
    json.dump(my_obj, f)

with open("test.json", 'r') as f:
    my_obj = json.load(f)

print(my_obj["settings"])


my_print = pickle.loads(pickle.dumps(print))
my_print("test string", 1, 2, 3)
print(id(my_print), id(print))


data_v1 = {
    "model":["80 1.6 Specs", "80 1.6 Specs"],
    "year":[1989,1993],
    "horsepower":[69,102],
    "engine size":["1595 cm3", "1595 cm3"]
}

data_v2 = [
    {
        "model":"80 1.6 Specs",
        "year":1989,
        "horsepower":69,
        "engine size":"1595 cm3",
    },
    {
        "model":"80 1.6 Specs",
        "year":1993,
        "horsepower":102,
        "engine size":"1595 cm3"
    }
]

headline = ['model', 'year', 'horsepower', 'engine size']

with open("v1.json", 'w') as f:
    json.dump(data_v1, f)

with open("v2.json", 'w') as f:
    json.dump(data_v2, f)

with open("v1.pickle", 'wb') as f:
    pickle.dump(data_v1, f)

with open("v2.pickle", 'wb') as f:
    pickle.dump(data_v2, f)

with open('v2.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerows(data_v2)

with open('v1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headline)
    for i in range(len(data_v1[headline[0]])):
        row = []
        for field in headline:
            row.append(data_v1[field][i])
        writer.writerow(row)