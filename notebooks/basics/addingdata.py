import csv 
with open("True.csv","w") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["Name", "Age", "dept"])
    writer.writerow(["Alice", 25, "cse"])
with open("True.csv","r") as f:
    reader=csv.reader(f)
    for row in f:
        print(row)
        