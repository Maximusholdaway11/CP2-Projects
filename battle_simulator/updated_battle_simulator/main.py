#Max Holdaway Updated Battle Simulator: Main Function / User Interface

#Importing all the functions from my other pages
import battling as battle_functions
import character_creator as char_functions

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
                "Exit (will auto save all current characters)"
            ],
        ).execute()
        if user_input == "Character Management":
            while True:
                user_input = inquirer.select(
                message="What do you want to do?:",
                choices=[
                    "Create a character",
                    "Display a characters information",
                    "Exit (the character manager)"
                ],
            ).execute()
                if user_input == "Create a character":
                    character_list = char_functions.character_creator(character_list)
                elif user_input == "Display a characters information":
                    user_char_choice = input("What is the name of the character you want to view?: ")
                    char_functions.display_character_info(user_char_choice, character_list)
                elif user_input == "Exit (the character manager)":
                    print("Exited Character manangement.")
                    break
        elif user_input == "Battle Simulator":
            battle_functions.battling(character_list)
        elif user_input == "Exit (will auto save all current characters)":
            print("Hope this battle simulator was fun goodybye!")
            char_functions.save_characters(character_list)
            break

main()