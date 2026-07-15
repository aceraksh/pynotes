import csv

fields = ["name", "age", "city"]

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 25, "city": "Paris"})