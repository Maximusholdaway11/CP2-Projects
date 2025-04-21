#Max Holdaway - Geometry Calculator: Comparison Calculations

def higher_perimeter(shape_1, shape_2):
    perimeter_1 = shape_1.calc_perimeter()
    perimeter_2 = shape_1.calc_perimeter()
    if perimeter_1 > perimeter_2:
        print(f"{shape_1.show_name}'s perimeter is bigger than {shape_2.show_name}'s perimeter.")
    elif perimeter_2 > perimeter_1:
        print(f"{shape_2.show_name}'s perimeter is bigger than {shape_1.show_name}'s perimeter.")
    elif perimeter_1 == perimeter_2:
        print("Both shapes have the same perimeter.")
    else:
        print("Unexepected Error has occured please try again.")

def higher_area(shape_1, shape_2):
    area_1 = shape_1.calc_area()
    area_2 = shape_1.calc_area()
    if area_1 > area_2:
        print(f"{shape_1.show_name}'s area is bigger than {shape_2.show_name}'s area.")
    elif area_2 > area_1:
        print(f"{shape_2.show_name}'s area is bigger than {shape_1.show_name}'s area.")
    elif area_1 == area_2:
        print("Both shapes have the same area.")
    else:
        print("Unexepected Error has occured please try again.")