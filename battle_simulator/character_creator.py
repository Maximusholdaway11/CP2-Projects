#Ttitle
import csv

def load_characters(characters):
    with open("battle_simulator/characters.csv") as file:
        file_csv_reader = csv.reader(file)
        for row in file_csv_reader:
            if row[0] != "":
                characters.append(dict("name", row[0], "health", row[1], "strength", row[2], "defense", row[3], "speed", row[4]))

def display_character_info(user_char_input, characters):
    print("Here is your character information")
    for dict_ in characters:
        if dict_["name"] == user_char_input:
            print(f"{dict_["name"]}'s stats are Health: {dict_["health"]}, Strength: {dict_["strength"]}, Defense: {dict_["defense"]}, Speed: {dict_["speed"]}.")

def character_creator(characters, type):
    def int_checker(user_input):
        int_checker = False
        while int_checker == False:
            if user_input.isnumeric == True:
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
    user_character = {"name", user_char_name, "health", user_char_health, "strength", user_char_strength, "defense", user_char_defense, "speed", user_char_speed}
    characters.append(user_character)
    return characters