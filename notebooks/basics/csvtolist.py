import csv
with open("users.csv","r") as f:
    reader=csv.reader(f)
    data=tuple(reader)
print(data)