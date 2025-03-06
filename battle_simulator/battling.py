#Max Holdaway Battle Simulator: Battling function(s)
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

def player_turn(user_char_selection, user_com_selection, characters):
    def character_selector(name, characters):
        for character in characters:
            if name == character["name"]:
                selected_character = character
        return selected_character
    print(f"The battle has started its {user_char_selection} vs. {user_com_selection}.")
    user_character = character_selector(user_char_selection, characters)
    com_character = character_selector(user_com_selection, characters)
    while True:
        if user_character["speed"] > com_character["speed"]:
            print("1. Attack")
            print("2. Items (item menu)")
            print("3. Defend (gives you a defense bonus and you will no matter what live the enemy attack if you do this (only guaranteed on the first use))")
            print("4. Pass (regens mana for spells and such)")
            user_input = input("What do you want to do?: ")
            if user_input.isnumeric():
                user_input = int(user_input)
                if user_input == 1:
                    user_og_damage = user_character["strength"]
                    user_reduced_damage = user_og_damage - com_character["defense"]
                    if user_reduced_damage < 0:
                        user_reduced_damage = 0
                    com_character["health"] = com_character["health"] - user_reduced_damage
                    print(f"You have succesfully done {user_reduced_damage} and the enemy is at {com_character["health"]} health.")
            else:
                print("Please type in a number.")