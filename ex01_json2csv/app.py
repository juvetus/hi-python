import json
import csv


with open("data.json" , 'r')  as f :
    data = json.load(f)
    names = data["names"]


with open("data.csv" , 'w') as f:
    fieldnames = names[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for name in names:
        writer.writerow(name)


