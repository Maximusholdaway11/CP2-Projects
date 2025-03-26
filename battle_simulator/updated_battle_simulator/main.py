#Max Holdaway Updated Battle Simulator: Main Function / User Interface

#Importing all the functions from my other pages
import battling as battle_functions
import character_creator as char_functions
import character_data_frames as data_frame_functions

#This is the InquirerPy library and it has been used to create all of the custom user interfaces you may see. You may need to use (pip3 install InquirerPy) to use my program if it does not work copy this website link "https://inquirerpy.readthedocs.io/en/latest/"
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

#Main Function / User Interface
def main():
    character_list = []
    character_list = char_functions.load_characters(character_list)
    while True:
        user_input = inquirer.select(
            message="What do you want to do?:",
            choices=[
                "Character Management",
                "Battle Simulator",
                "Stat Statistics",
                "Exit (will save all current characters)"
            ],
        ).execute()
        if user_input == "Character Management":
            while True:
                user_input = inquirer.select(
                message="What do you want to do?:",
                choices=[
                    "Create a character",
                    "Display a characters stats",
                    "Display a characters backstory and address",
                    "Exit (the character manager)"
                ],
            ).execute()
                if user_input == "Create a character":
                    character_list = char_functions.character_creator(character_list)
                    char_functions.save_characters(character_list)
                elif user_input == "Display a characters information":
                    if character_list != []:
                        character_has_been_shown = False
                        while character_has_been_shown == False:
                            character_has_been_shown = char_functions.display_character_info_bar_graph(character_list)
                    else:
                        print("You have no characters to use please create a character first before using this.")
                elif user_input == "Display a characters backstory and address":
                    char_functions.show_address_and_backstory(character_list)
                elif user_input == "Exit (the character manager)":
                    print("Exited Character manangement.")
                    break
        elif user_input == "Battle Simulator":
            battle_functions.battling(character_list)
            char_functions.save_characters(character_list)
        elif user_input == "Stat Statistics":
            character_list_data_frame = data_frame_functions.load_characters_into_data_frame(character_list)
            if len(character_list_data_frame) > 0:
                data_frame_functions.characters_min_max_median_mean(character_list_data_frame)
            else:
                print("No characters are created please add characters before doing this.")
        elif user_input == "Exit (will save all current characters)":
            print("Hope this battle simulator was fun goodybye!")
            char_functions.save_characters(character_list)
            break

main()