#Max Holdaway Updated Battle Simulator: Character Creator function(s)
import csv
import matplotlib.pyplot as plt
import numpy as np
import copy
from faker import Faker
from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator

#Function to save characters to csv file
def save_characters(characters):
    with open("battle_simulator/updated_battle_simulator/characters.csv", "w") as file:
        file_csv_writer = csv.writer(file)
        for character in characters:
            file_csv_writer.writerow(character.values())

#Function to load characters from the csv file
def load_characters(characters):
    with open("battle_simulator/updated_battle_simulator/characters.csv", "r") as file:
        file_csv_reader = csv.reader(file)
        for row in file_csv_reader:
            if row != []:
                characters.append({"name": row[0], "health": int(row[1]), "strength": int(row[2]), "defense": int(row[3]), "speed": int(row[4]), "xp": int(row[5]), "backstory": row[6], "address": row[7]})
        return characters

#Function to display a characters stats as a graph
def display_character_info_bar_graph(characters):
    def select_character(characters):
        if characters != []:
            character_choice = inquirer.select(
                message="What is the name of the character you want to view?:",
                choices=[char.get('name') for char in characters],
            ).execute()
            return character_choice
        else:
            return ""
    user_char_input = select_character(characters)
    temp_character = ""
    for character in characters:
        if character['name'] == user_char_input:
            temp_character = copy.deepcopy(character)
    #If the character is actually a character show the user the graph
    if temp_character != "":
        plt.style.use('_mpl-gallery')

        x = ["Health", "Strength", "Defense", "Speed", "xp"]
        y = [temp_character['health'], temp_character['strength'], temp_character['defense'], temp_character['speed'], temp_character['xp']]
        graph_pos = [0.1, 0.1, 5, 5]
        fig, ax = plt.subplots()
        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
        ax.set(ylim=(0, 100), yticks=np.arange(1, 101), ylabel="Stats", position=graph_pos)

        plt.show()
        return True
    else:
        print("Character not found please input a different character.")
        return False

#Function to show a characters backstory and address
def show_address_and_backstory(characters):
    #Getting the name of the character wanting to be selected
    def select_character_name(characters):
        if characters != []:
            character_choice = inquirer.select(
                message="What is the name of the character you want to view?:",
                choices=[char.get('name') for char in characters],
            ).execute()
            return character_choice
        else:
            return ""
    #Using that name to actually select said character
    def select_character(characters, char_name):
        if char_name != "":
            for char in characters:
                if char['name'] == char_name:
                    character = copy.deepcopy(char)
                    return character
        else:
            return ""
    char_selection_name = select_character_name(characters)
    char_selection = select_character(characters, char_selection_name)
    print(char_selection)
    #Showing the backstory and address of the character if the character is actually a character
    if char_selection != "":
        print(f"Here is your characters backstory:\n{char_selection['backstory']}.")
        print(f"Here is your characters address:\n{char_selection['address']}.")
    else:
        print("No characters are created please create a character.")
        

#Function to create a character
def character_creator(characters):
    def get_stat(type):
        while True:
            type_num = inquirer.text(
            message=f"What is your characters {type}? (please have it be below 100 and above 0): ",
            validate =NumberValidator(message="Please type in a number."),
            ).execute()
            type_num = int(type_num)
            if type_num > 100 or type_num == 0:
                print("Please select a stat below 100 and above 0")
                continue
            elif type_num <= 100:
                return type_num
    print("This is a character creator.")
    word_generator = Faker()
    user_char_name = word_generator.name()
    user_char_health = get_stat('health')
    user_char_strength = get_stat('strength')
    user_char_defense = get_stat('defense')
    user_char_speed = get_stat('speed')
    character_backstory = word_generator.text()
    character_address = word_generator.address()
    user_character = {"name": user_char_name, "health": user_char_health, "strength": user_char_strength, "defense": user_char_defense, "speed": user_char_speed, "xp": 0, "backstory": character_backstory, "address": character_address}
    print(f"The name of your character is: {user_char_name}")
    characters.append(user_character)
    return characters