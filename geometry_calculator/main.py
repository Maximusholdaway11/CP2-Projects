#Max Holdaway - Geometry calculator: Main Function / User Interface
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
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
                    print("Your number cannot be less than zero or equal zero.")
        else:
            try:
                user_num = float(user_num)
                if user_num > 0:
                    return round(float(user_num), 2)
                else:
                    print("Your number cannot be less than zero or equal zero.")
            except:
                print("Your number cannot be less than zero or equal zero.")

def check_str(message):
    while True:
        user_str = inquirer.text(message=message).execute()
        if user_str == "":
            print("You need to type something.")
        else:
            return user_str

def main():
    shape_list = []
    print("This is a geometry calculator where you can create shapes, look at the attributes for them, find their specific areas / perimeters, and compare those areas / perimeters.")
    while True:
        user_selection = inquirer.select(message="Which option do you want to do:", choices=['Create shapes', 'View attributes on a shape', 'Calculate area / perimeter of shapes', 'Compare area / perimeter of shapes', 'Sort shapes by area or perimeter', 'Exit']).execute()
        if user_selection == 'Create shapes':
            while True:
                user_input = inquirer.select(message="What type of shape do you want to create or do you want to exit?:", choices=['Rectangle', 'Square', 'Triangle', 'Circle', 'Exit']).execute()
                if user_input == "Rectangle":
                    user_length = check_num_negative_zero("Please type the length of your rectangle:")
                    user_width = check_num_negative_zero("Please type the width of your rectangle:")
                    user_rectangle_name = check_str("Please type the name of your rectangle:")
                    user_rectangle = rectangle(int(user_length), int(user_width), user_rectangle_name)
                    shape_list.append(user_rectangle)
                elif user_input == "Square":
                    user_side = check_num_negative_zero("Please type the one side length of your square:")
                    user_square_name = check_str("Please type the name of your square:")
                    user_square = square(user_side, user_square_name)
                    shape_list.append(user_square)
                elif user_input == "Triangle":
                    user_side_1 = check_num_negative_zero("Please give the first side length of your triangle:")
                    user_side_2 = check_num_negative_zero("Please give the second side length of your triangle:")
                    user_side_3 = check_num_negative_zero("Please give the third side length of your triangle:")
                    user_base = check_num_negative_zero("Please give the base of your triangle:")
                    user_height = check_num_negative_zero("Please give the height of your triangle:")
                    user_triangle_name = check_str("Please type the name of your triangle:")
                    user_triangle = triangle(user_base, user_height, user_side_1, user_side_2, user_side_3, user_triangle_name)
                    shape_list.append(user_triangle)
                elif user_input == "Circle":
                    user_radius = check_num_negative_zero("Please give the radius of your circle:")
                    user_circle_name = check_str("Please type the name of your circle:")
                    user_circle = circle(user_radius, user_circle_name)
                    shape_list.append(user_circle)
                else:
                    break
        elif user_selection == "Calculate area / perimeter of shapes":
            while True:
                user_input = inquirer.select(message='What do you want to do?:', choices=['Area', 'Perimeter', 'Exit']).execute()
                if user_input == 'Area':
                    user_shape = inquirer.select(message='What is the shape you want to calculate area for?:', choices=[shape.name for shape in shape_list]).execute()
                    for shape in shape_list:
                        if user_shape == shape.name:
                            user_area = shape.calc_area()
                            print(f'The area of {shape.show_name()} is {user_area}')
                elif user_input == 'Perimeter':
                    user_shape = inquirer.select(message='What is the shape you want to calculate perimeter for?:', choices=[shape.name for shape in shape_list]).execute()
                    for shape in shape_list:
                        if user_shape == shape.name:
                            user_perimeter = shape.calc_perimeter()
                            print(f'The perimeter of {shape.show_name()} is {user_perimeter}')
                else:
                    break
        elif user_selection == "Compare area / perimeter of shapes":
            while True:
                user_input = inquirer.select(message='What do you want to do?:', choices=['Area', 'Perimeter', 'Exit']).execute()
                if user_input == "Area":
                    user_shape_1 = inquirer.select(message='What is the first shape you want to compare area for?:', choices=[shape.name for shape in shape_list]).execute()
                    user_shape_2 = inquirer.select(message='What is the second shape you want to compare area for?:', choices=[shape.name for shape in shape_list]).execute()
                    for shape in shape_list:
                        if shape.name == user_shape_1:
                            shape_1 = shape
                    for shape in shape_list:
                        if shape.name == user_shape_2:
                            shape_2 = shape
                    try:
                        compare_area(shape_1, shape_2)
                    except:
                        print("Unable to find your shape.")
                elif user_input == "Perimeter":
                    user_shape_1 = inquirer.select(message='What is the first shape you want to compare perimeter for?:', choices=[shape.name for shape in shape_list]).execute()
                    user_shape_2 = inquirer.select(message='What is the second shape you want to compare perimeter for?:', choices=[shape.name for shape in shape_list]).execute()
                    for shape in shape_list:
                        if shape.name == user_shape_1:
                            shape_1 = shape
                    for shape in shape_list:
                        if shape.name == user_shape_2:
                            shape_2 = shape
                    try:
                        compare_perimeter(shape_1, shape_2)
                    except:
                        print("Unable to find your shape.")
                else:
                    break
        elif user_selection == "Sort shapes by area or perimeter":
            user_input = inquirer.select(message="What do you want to do?:", choices=["Area", "Perimeter", "Exit"]).execute()
            if user_input == "Perimeter":
                sorted_list = sort_by_perimeter(shape_list)
                print(f"This is the sorted list(in least to greatest):\n{[shape.name for shape in sorted_list]}")
            elif user_input == "Area":
                sorted_list = sort_by_area(shape_list)
                print(f"This is the sorted list(in least to greatest):\n{[shape.name for shape in sorted_list]}")
            else:
                break
        elif user_selection == "View attributes on a shape":
            while True:
                user_input = inquirer.select(message="Do you want to view attributes or exit?:", choices=['View Attributes', 'Exit']).execute()
                if user_input == 'View Attributes':
                    user_shape = inquirer.select(message='What is the shape you want to view attributes for?:', choices=[shape.name for shape in shape_list]).execute()
                    for shape in shape_list:
                        if shape.name == user_shape:
                            user_shape = shape
                    print(user_shape)
                else:
                    break
        else:
            print("Hope this calculator was useful goodbye!")
            break

main()