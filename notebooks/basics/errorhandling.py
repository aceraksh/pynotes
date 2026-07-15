import csv
try:
    with open("users.csv","r") as f:
        reader=csv.reader(f)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found")