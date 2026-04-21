import csv
with open("filebook.csv","w", newline="")as file:
    writer = csv.writer(file)

    writer.writerow(["Name","Age","city"])  # Header
    writer.writerow(["sri",20,"Hydrabad"])
    writer.writerow(["Ravi",22,"Chennai"])
