#Max Holdaway, Reading files notes
import csv
users = {}

with open('Reading_Files/note_file.txt') as file:
    content = file.read()
    index = content.find("notes")
    print(content[index:index+5])

with open('Reading_Files/sample.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        print(f'username {row[0]}, favorite color {row[1]}')

with open('Reading_Files/sample.csv') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    for row in csv_reader:
        users.update({row[0]:row[1]})

print(users)