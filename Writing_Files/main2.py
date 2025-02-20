import csv

data = [["username", "hi", "color", "red"],
        ["username", "hello", "color", "green"],
        ["username", "hilo", "color", "blue"],
        ["username", "helloi", "color", "yellow"]]

with open("Writing_Files/sample.csv", "w", newline='') as file:
    fieldnames = ["username", "color"]
    writer = csv.writer(file, delimiter="|")
    writer.writerows(data)

with open("Writing_Files/sample.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter="|")
    for row in csv_reader:
        print(row)