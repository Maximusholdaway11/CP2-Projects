#Title
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