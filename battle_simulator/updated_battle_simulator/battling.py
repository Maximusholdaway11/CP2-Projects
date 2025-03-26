#Max Holdaway Updated Battle Simulator: Battling function(s)

#I use this to copy characters for battle use and not change the character in the character list
import copy

#InquirerPy used for user inputs
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator

#Function to select the character the user will use
def select_user_character(characters):
    if characters != [] and len(characters) >= 2:
        character_choice = inquirer.select(
            message="Pick your character:",
            choices=[char.get('name') for char in characters],
        ).execute()
        character = ""
        for char in characters:
            if character_choice == char['name']:
                character = copy.deepcopy(char)
        return character
    else:
        return ""

#Function to select the character the computer will use
def select_com_character(characters, user_character_choice):
    if characters != [] and len(characters) >= 2:
        while True:
            character_choice = inquirer.select(
                message="Pick the Computers character:",
                choices=[char.get('name') for char in characters],
            ).execute()
            character = ""
            for char in characters:
                if character_choice == char['name']:
                    if character_choice != user_character_choice:
                        character = copy.deepcopy(char)
                        return character
                    else:
                        print("You cannot choose the same character twice please try again.")
                        continue
    else:
        return ""

#Function to run the battling part of the battle simulator
def battling(characters):
    def get_winner():
        if user_character['health'] <= 0:
            print("Enemy has sadly beaten you.")
            return "Player Beaten"
        elif com_character['health'] <= 0:
            print("You have beaten the enemy congrats!")
            return "Enemy Beaten"
        else:
            return "Nobody"
    def enemy_player_attack(if_temp_defense):
        if if_temp_defense == True:
            user_temp_defense = user_character["defense"] + 2
            enemy_og_damage = com_character["strength"]
            enemy_reduced_damage = enemy_og_damage - user_temp_defense
            if enemy_reduced_damage <= 0:
                print(f"The enemy has attacked but didn't do any damage.")
            else:
                user_character["health"] = user_character["health"] - enemy_reduced_damage
                if user_character["health"] == 0:
                    user_character["health"] = 1
                print(f"The enemy has attacked and done {enemy_reduced_damage} damage your health is {user_character["health"]}.")
                battle_winner = get_winner()
                return battle_winner
        elif if_temp_defense == False:
            user_og_damage = user_character["strength"]
            user_reduced_damage = user_og_damage - com_character["defense"]
            if user_reduced_damage < 0:
                user_reduced_damage = 0
            com_character["health"] = com_character["health"] - user_reduced_damage
            if com_character['health'] < 0:
                com_character['health'] = 0
            print(f"You have succesfully done {user_reduced_damage} and the enemy is at {com_character["health"]} health.")
            battle_winner = get_winner()
            if battle_winner == "Enemy Beaten":
                return battle_winner
            elif battle_winner == "Player Beaten":
                return battle_winner
            else:
                enemy_og_damage = com_character["strength"]
                enemy_reduced_damage = enemy_og_damage - user_character["defense"]
                if enemy_reduced_damage <= 0:
                    print(f"The enemy has attacked but didn't do any damage.")
                else:
                    print(f"The enemy has attacked and done {enemy_reduced_damage} damage your health is {user_character["health"]}.")
                    user_character['health'] = user_character['health'] - enemy_reduced_damage
                    if user_character['health'] < 0:
                        user_character['health'] = 0
                    battle_winner = get_winner()
                    if battle_winner == "Player Beaten":
                        return battle_winner
                    elif battle_winner == "Enemy Beaten":
                        return battle_winner
                    else:
                        return "Nobody"
    def enemys_attack():
        enemy_og_damage = com_character["strength"]
        enemy_reduced_damage = enemy_og_damage - user_character["defense"]
        if enemy_reduced_damage <= 0:
            print(f"The enemy has attacked but didn't do any damage.")
            battle_winner = get_winner()
            return battle_winner
        else:
            user_character['health'] = user_character['health'] - enemy_reduced_damage
            print(f"The enemy has attacked and done {enemy_reduced_damage} damage your health is {user_character["health"]}.")
            battle_winner = get_winner()
            return battle_winner
    def players_attack():
        user_og_damage = user_character["strength"]
        user_reduced_damage = user_og_damage - com_character["defense"]
        if user_reduced_damage <= 0:
            user_reduced_damage = 0
        com_character["health"] = com_character["health"] - user_reduced_damage
        print(f"You have succesfully done {user_reduced_damage} and the enemy is at {com_character["health"]} health.")
        battle_winner = get_winner()
        return battle_winner
    user_character = select_user_character(characters)
    if user_character != "":
        com_character = select_com_character(characters, user_character['name'])
    else:
        print("There are no characters for you to select please create at least two characters to use this.")
        return ""
    if user_character != "" and com_character != "":
        print(f"The battle has started its {user_character['name']} vs. {com_character['name']}.")
        while True:
            if user_character["speed"] > com_character["speed"]:
                print("You were faster than the enemy.")
                from InquirerPy import inquirer
                from InquirerPy.base.control import Choice
                from InquirerPy.separator import Separator
                user_input = inquirer.select(
                    message="What do you want to do?:",
                    choices=[
                        "Attack",
                        "Defend (which increases normal defense by 2 and allows you to survive attacks no matter what (useful if you have high speed))",
                        "Surrender"
                    ],
                ).execute()
                if user_input == "Attack":
                    battle_winner = enemy_player_attack(False)
                    if battle_winner == "Player Beaten":
                        break
                    elif battle_winner == "Enemy Beaten":
                        for character in characters:
                            if user_character['name'] == character['name']:
                                character['xp'] = character['xp'] + 1
                        break
                    else:
                        continue
                elif user_input == "Defend":
                    battle_winner = enemy_player_attack(True)
                    if battle_winner == "Player Beaten":
                        break
                    elif battle_winner == "Enemy Beaten":
                        for character in characters:
                            if user_character['name'] == character['name']:
                                character['xp'] = character['xp'] + 1
                                print(f"{user_character['name']} has gained one xp point!")
                                return characters
                    else:
                        continue
                elif user_input == "Surrender":
                    print("You have surrendered to the enemy battle has ended.")
                    break
            elif user_character["speed"] < com_character["speed"]:
                print("The enemy was faster than you.")
                battle_winner = enemys_attack()
                if battle_winner == "Player Beaten":
                    break
                elif battle_winner == "Enemy Beaten":
                    for character in characters:
                        if user_character['name'] == character['name']:
                            character['xp'] = character['xp'] + 1
                            print(f"{user_character['name']} has gained one xp point!")
                            return characters
                else:
                    continue
                from InquirerPy import inquirer
                from InquirerPy.base.control import Choice
                from InquirerPy.separator import Separator
                user_input = inquirer.select(
                    message="What do you want to do?:",
                    choices=[
                        "Attack",
                        "Surrender"
                    ],
                ).execute()
                if user_input == "Attack":
                    battle_winner = players_attack()
                elif user_input == "Surrender":
                    print("You have surrendered to the enemy battle has ended.")
                    break
                if battle_winner == "Player Beaten":
                    break
                elif battle_winner == "Enemy Beaten":
                    for character in characters:
                        if user_character['name'] == character['name']:
                            character['xp'] = character['xp'] + 1
                            print(f"{user_character['name']} has gained one xp point!")
                            return characters
                else:
                    continue
            elif user_character["speed"] == com_character["speed"]:
                print("Your speeds are the same player is going first.")
                from InquirerPy import inquirer
                from InquirerPy.base.control import Choice
                from InquirerPy.separator import Separator
                user_input = inquirer.select(
                    message="What do you want to do?:",
                    choices=[
                        "Attack",
                        "Defend (which increases normal defense by 2 and allows you to survive attacks no matter what (useful if you have high speed))",
                        "Surrender"
                    ],
                ).execute()
                if user_input == "Attack":
                    battle_winner = enemy_player_attack(False)
                elif user_input == "Defend":
                    battle_winner = enemy_player_attack(True)
                elif user_input == "Surrender":
                    print("You have surrendered to the enemy battle has ended.")
                    break
                if battle_winner == "Player Beaten":
                    break
                elif battle_winner == "Enemy Beaten":
                    for character in characters:
                        if user_character['name'] == character['name']:
                            character['xp'] = character['xp'] + 1
                            print(f"{user_character['name']} has gained one xp point!")
                            return characters
                else:
                    continue
    else:
        print("You havent created any characters please try again.")