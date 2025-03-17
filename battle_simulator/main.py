#Max Holdaway Battle Simulator: Main Function / User Interface
import battling as battle_functions
import character_creator as char_functions
character_list = []

def main(character_list):
    character_list = char_functions.load_characters()
    while True:
        from InquirerPy import inquirer
        from InquirerPy.base.control import Choice
        from InquirerPy.separator import Separator
        user_input = inquirer.select(
            message="What do you want to do?:",
            choices=[
                "Character management",
                "Battle manangment",
                "Exit (will auto save all current characters)"
            ],
        ).execute()
        if user_input == "Character management":
            while True:
                user_input = inquirer.select(
                message="What do you want to do?:",
                choices=[
                    "Create a character",
                    "Display a characters information",
                    "Exit"
                ],
            ).execute()
                if user_input == "Create a character":
                    character_list = char_functions.character_creator(character_list)
                elif user_input == "Display a characters information":
                    user_char_choice = input("What is the name of the character you want to view?: ")
                    char_functions.display_character_info(user_char_choice, character_list)
                elif user_input == "Exit":
                    print("Exiting Character manangement.")
                    break
        elif user_input == "Battle management":
            