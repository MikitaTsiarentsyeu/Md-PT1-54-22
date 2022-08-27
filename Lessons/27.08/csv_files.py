import csv

with open("test.csv", 'r') as f:
    isFirst = True
    for line in f:
        if isFirst:
            isFirst = False
            continue
        if not line:
            continue
        data = line.strip('\n').split(',')
        print(f"{data[0]} {data[1]}: color {data[2]}, sizes {data[3]}")

data = ['adidas', 'campus', 'white', '45-46']

# with open("test.csv", 'a') as f:
#     f.write('\n'+','.join(data))

headline = ['make','model','color','sizes']

with open("test.csv", 'r') as f:
    reader = csv.DictReader(f, headline)
    for l in reader:
        print(l)

    # reader = csv.reader(f)
    # for l in reader:
    #     print(l)


with open("new_test.csv", 'w', newline='\n') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerow({field:"test" for field in headline})
    # writer = csv.writer(f)
    # writer.writerow(data)