#Max Holdaway Battle Simulator: Main Function / User Interface
import battling
import character_creator
character_list = []

def main(character_list):
    character_list = character_creator.load_characters()
    while True:
        from InquirerPy import inquirer
        from InquirerPy.base.control import Choice
        from InquirerPy.separator import Separator
        user_input = inquirer.select(
            message="What do you want to do?:",
            choices=[
                "Create a character",
                "Battle with characters",
                "Exit"
            ],
        ).execute()