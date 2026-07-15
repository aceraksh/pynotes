import csv 
with open("users.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        name=str(row["name"])
        age=int(row["age"])
        print(age,name)