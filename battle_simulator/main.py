#Max Holdaway Battle Simulator: Main Function / User Interface
import battling
import character_creator
character_list = []

def main(character_list):
    character_list = character_creator.load_characters()
    