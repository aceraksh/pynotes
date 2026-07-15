import csv

with open("users.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Charlie", 40, "USA"])
    writer.writerow(["Charles", 40, "Uk"])