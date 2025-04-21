#Max Holdaway - Geometry calculator: Main Function / User Interface
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import user_numValidator
from circle import *
from rectangle import *
from triangle import *
from comparisons import *

def check_num_negative_zero(message):
    while True:
        user_num = inquirer.text(message=message).execute()
        if user_num.isnumeric():
                user_num = int(user_num)
                if user_num >= 0:
                    return user_num
                else:
                    print("Your number cannot be less than zero or equal to zero.")
        else:
            try:
                user_num = float(user_num)
                if user_num > 0:
                    return round(float(user_num), 2)
                else:
                    print("Your number cannot be less than zero or equal to zero.")
            except:
                print("Please type in a number that is not less than zero (you can include decimals).")

def check_str(message):
    while True:
        user_str = inquirer.text(message=message)
        if user_str == "":
            print("You need to type something.")
        else:
            return user_str

def main():
    shape_list = []
    print("This is a geometry calculator where you can create shapes, look at the attributes for them, find their specific areas / perimeters, and compare those areas / perimeters.")
    while True:
        user_input = inquirer.select(message="Which option do you want to do:", choices=['Create shapes', 'Calculate area / perimeter of shapes', 'Compare area / perimeter of shapes', 'Exit']).execute()
        if user_input == 'Create shapes':
            user_input = inquirer.select(message="What type of shape do you want to create?:", choices=['Rectangle', 'Square', 'Triangle', 'Circle']).execute()
            if user_input == "Rectangle":
                user_length = check_num_negative_zero("Please type the length of your rectangle:")
                user_width = check_num_negative_zero("Please type the width of your rectangle:")
                user_rectangle_name = check_str("Please type the name of your rectangle.")
                user_rectangle = rectangle(int(user_length), int(user_width), False, user_rectangle_name)
                shape_list.append(user_rectangle)
            