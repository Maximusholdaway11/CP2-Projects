#Max Holdaway Battle Simulator: Battling function(s)
import copy

def character_selection_view(characters):
    for character in characters:
        print(f"""{character["name"]}:
              Health: {character["health"]}
              Strength: {character["strength"]}
              Defense: {character["defense"]}
              Speed: {character["speed"]}\n""")

def select_character(characters):
    character_selection_view(characters)
    print("This is the character selector please choose your character.")
    user_char_selection = input("Which character do you want to choose?: ")
    return user_char_selection

def select_com_character(characters):
    print("This is the computer character selection.")
    character_selection_view(characters)
    user_com_char_selection = input("Which character will the computer use?: ")
    return user_com_char_selection

def battling(user_char_selection, user_com_selection, characters):
    def get_winner():
        if user_character['health'] == 0:
            print("Enemy has sadly beaten you.")
            return "Player Beaten"
        elif com_character['health'] == 0:
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
            print(f"The enemy has attacked and done {enemy_reduced_damage} damage your health is {user_character["health"]}.")
            battle_winner = get_winner()
            return battle_winner
    def players_attack():
        user_og_damage = user_character["strength"]
        user_reduced_damage = user_og_damage - com_character["defense"]
        if user_reduced_damage < 0:
            user_reduced_damage = 0
        com_character["health"] = com_character["health"] - user_reduced_damage
        print(f"You have succesfully done {user_reduced_damage} and the enemy is at {com_character["health"]} health.")
        battle_winner = get_winner()
        return battle_winner
    def character_selector(name, characters):
        for character in characters:
            if name == character["name"]:
                selected_character = copy.deepcopy(character)
        return selected_character
    def check_winner(player_character, com_character):
        if player_character['health'] == 0:
            return "Player Died"
        elif com_character['health'] == 0:
            return "Computer Died"
        else:
            return "No one has won"
    print(f"The battle has started its {user_char_selection} vs. {user_com_selection}.")
    user_character = character_selector(user_char_selection, characters)
    com_character = character_selector(user_com_selection, characters)
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
            elif user_input == "Defend":
                battle_winner = enemy_player_attack(True)
            elif user_input == "Surrender":
                print("You have surrendered to the enemy battle has ended.")
                break
        elif user_character["speed"] < com_character["speed"]:
            print("The enemy was faster than you.")
            battle_winner = enemys_attack()
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
                if user_char_selection == character['name']:
                    user_character['xp'] = user_character['xp'] + 1
                    character = copy.deepcopy(user_character)
                    return characters
        else:
            continue
        if battle_winner == "Player Beaten":
            break
        elif battle_winner == "Enemy Beaten":
            break