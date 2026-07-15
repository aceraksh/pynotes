import csv

def validate_row(row):
    return all(row)

data = [
    ["John", 28, "Toronto"],
    ["", 35, "Berlin"]
]

with open("validated.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        if validate_row(row):
            writer.writerow(row)