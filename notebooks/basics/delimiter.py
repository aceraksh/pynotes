import csv

with open("Users.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)