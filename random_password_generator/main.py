#Max Holdaway Random Password Generator

import string

import random

alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

special_characters_list = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "|", ";", ":", "'", ",", "<", ".", ">", "/", "?"]

def if_upper_or_lower(upper_lower_choice, password):
    password = str(password)
    if upper_lower_choice.lower() == "only lower":
        random_lower_letter = random.choice(alphabet_list)
        random_lower_letter = random_lower_letter.lower()
        password += random_lower_letter
        return password
    elif upper_lower_choice.lower() == "only upper":
        random_upper_letter = random.choice(alphabet_list)
        random_upper_letter = random_upper_letter.upper()
        password += random_upper_letter
        return password
    elif upper_lower_choice.lower() == "both":
        random_lower_letter = random.choice(alphabet_list)
        random_lower_letter = random_lower_letter.lower()
        random_upper_letter = random.choice(alphabet_list)
        random_upper_letter = random_upper_letter.upper()
        letter_select_list = [random_lower_letter, random_upper_letter]
        password += random.choice(letter_select_list)
        return password
    else:
        return print("You have not put an accepted choice in please try again.")
    
def if_numbers(number_choice, password):
    password = str(password)
    if number_choice.lower() == "numbers":
        random_number = random.randint(1, 100)
        random_number = str(random_number)
        password += random_number
        return password
    elif number_choice.lower():
        return print("No numbers will be added to your password.")
    else:
        return print("You have not put an accepted choice in please try again.")
    
def if_special_characters(special_character_choice, password):
    password = str(password)
    if special_character_choice.lower() == "yes":
        random_special_character = random.choice(special_characters_list)
        password += random_special_character
        return password
    elif special_character_choice.lower() == "no":
        return print("There will be no special characters in your password.")
    else:
        return print("You have not put an accepted choice in please try again.")

def password_assembler(password_length, password, s_choice, num_choice, up_low_choice):
    function_list = []
    for x in range(password_length):
        pass