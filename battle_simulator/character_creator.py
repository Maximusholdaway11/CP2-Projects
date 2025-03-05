#Ttitle
import csv

def load_characters(characters):
    with open("battle_simulator/characters.csv") as file:
        file_csv_reader = csv.reader(file)
        for row in file_csv_reader:
            if row[0]:
                characters.append{"name": row[0], "strength": row[1]}

def character_creator():
