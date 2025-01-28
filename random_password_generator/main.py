#Max Holdaway Random Password Generator

import random

#Creating a list of letters to use for passwords
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Creating a list of special characters to use for passwords
special_characters_list = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "|", ";", ":", "'", ",", "<", ".", ">", "/", "?"]

#function for getting the upper or lowercase or both in passwords
def if_upper_or_lower(upper_lower_choice):
    password_letter = ""
    if upper_lower_choice.lower() in "lower":
        random_lower_letter = random.choice(alphabet_list)
        random_lower_letter = random_lower_letter.lower()
        password_letter = random_lower_letter
        return password_letter
    elif upper_lower_choice.lower() in "upper":
        random_upper_letter = random.choice(alphabet_list)
        random_upper_letter = random_upper_letter.upper()
        password_letter = random_upper_letter
        return password_letter
    elif upper_lower_choice.lower() in "both":
        random_lower_letter = random.choice(alphabet_list)
        random_lower_letter = random_lower_letter.lower()
        random_upper_letter = random.choice(alphabet_list)
        random_upper_letter = random_upper_letter.upper()
        letter_select_list = [random_lower_letter, random_upper_letter]
        password_letter = random.choice(letter_select_list)
        return password_letter
    else:
        return print("You have not put an accepted choice in please try again.")

#function for getting the number in passwords
def if_numbers(number_choice):
    password_letter = ""
    if number_choice.lower() in "yes":
        random_number = random.randint(1, 100)
        random_number = str(random_number)
        password_letter = random_number
        return password_letter
    elif number_choice.lower() in "no":
        return print("No numbers will be added to your password.")
    else:
        return print("You have not put an accepted choice in please try again.")

#function for getting the special characters in passwords
def if_special_characters(special_character_choice):
    password_letter = ""
    if special_character_choice.lower() in "yes":
        random_special_character = random.choice(special_characters_list)
        password_letter = random_special_character
        return password_letter
    elif special_character_choice.lower() in "no":
        return print("There will be no special characters in your password.")
    else:
        return print("You have not put an accepted choice in please try again.")

#function for choosing a random character to add ot the password based on user specifications
def password_character_choice(special_choice_password, num_choice_password, up_low_choice_password):
    random_num_choice = random.randint(1, 3)
    if random_num_choice == 1:
        return if_upper_or_lower(up_low_choice_password)
    elif random_num_choice == 2 and special_choice_password in "yes":
        return if_numbers(num_choice_password)
    elif random_num_choice == 3 and num_choice_password in "yes":
        return if_special_characters(special_choice_password)
    else:
        return if_upper_or_lower(up_low_choice_password)

#function for making the password itself
def password_assembler(password_length, special_choice, num_choice, up_low_choice):
    password = ""
    for x in range(password_length):
        password += password_character_choice(special_choice, num_choice, up_low_choice)
    return password

#main function that runs the UI and gives four passwords
def main():
    print("This is a password generator that generates four passwords per use and based on specifications.")
    user_up_low_choice = str(input("Do you want just uppercase letters, just lowercase letters, or both in your password? (type lower for lowercase, upper for uppercase, and both for both): "))
    user_special_choice = str(input("Do you want special characters in your password? (just type yes or no): "))
    user_num_choice = str(input("Do you want numbers in your password? (just type yes or no): "))
    user_password_length = int(input("How long do you want your password to be?: "))
    user_password_one = password_assembler(user_password_length, user_special_choice, user_num_choice, user_up_low_choice)
    user_password_two = password_assembler(user_password_length, user_special_choice, user_num_choice, user_up_low_choice)
    user_password_three = password_assembler(user_password_length, user_special_choice, user_num_choice, user_up_low_choice)
    user_password_four = password_assembler(user_password_length, user_special_choice, user_num_choice, user_up_low_choice)
    print(f"""Here is your passwords: 
          password 1: {user_password_one}
          password 2: {user_password_two}
          password 3: {user_password_three}
          password 4: {user_password_four}""")
    
main()