import csv

with open("users.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        print(row)