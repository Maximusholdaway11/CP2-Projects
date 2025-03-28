#Max Holdaway Battle Simulator: Character Creator function(s)
import csv

#Function to save characters to csv file
def save_characters(characters):
    with open("battle_simulator/characters.csv", "w") as file:
        file_csv_writer = csv.writer(file)
        for character in characters:
            file_csv_writer.writerow(character.values())

#Function to load characters from the csv file
def load_characters(characters):
    with open("battle_simulator/characters.csv", "r") as file:
        file_csv_reader = csv.reader(file)
        for row in file_csv_reader:
            if row[0] != "":
                characters.append({"name": row[0], "health": int(row[1]), "strength": int(row[2]), "defense": int(row[3]), "speed": int(row[4]), "xp": int(row[5])})
        return characters

#Function to display a characters information
def display_character_info(user_char_input, characters):
    print("Here is your character information")
    for dict_ in characters:
        if dict_["name"] == user_char_input:
            print(f"{dict_["name"]}'s stats are Health: {dict_["health"]}, Strength: {dict_["strength"]}, Defense: {dict_["defense"]}, Speed: {dict_["speed"]}. Oh and {dict_['name']} also has {dict_['xp']} experience points.")

#Function to create a character
def character_creator(characters):
    def int_checker(user_input, type):
        int_checker = False
        while int_checker == False:
            if user_input.isnumeric() == True:
                int_checker = True
            else:
                print("Please input a number")
                user_input = input(f"What is your characters {type}?: ")
        else:
            return user_input
    print("This is a character creator.")
    user_char_name = input("What is your characters name?: ")
    user_char_health = input("What is your characters health?: ")
    user_char_health = int_checker(user_char_health, "health")
    user_char_health = int(user_char_health)
    user_char_strength = input("What is your characters strength?: ")
    user_char_strength = int_checker(user_char_strength, "strength")
    user_char_strength = int(user_char_strength)
    user_char_defense = input("What is your characters defense?: ")
    user_char_defense = int_checker(user_char_defense, "defense")
    user_char_defense = int(user_char_defense)
    user_char_speed = input("What is your characters speed?: ")
    user_char_speed = int_checker(user_char_speed, "speed")
    user_char_speed = int(user_char_speed)
    user_character = {"name": user_char_name, "health": user_char_health, "strength": user_char_strength, "defense": user_char_defense, "speed": user_char_speed, "xp": 0}
    characters.append(user_character)
    return characters