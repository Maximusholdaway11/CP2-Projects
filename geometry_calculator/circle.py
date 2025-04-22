#Max Holdaway - Geometry Calculator: Circle Class
import math

#Circle class
class circle:
    def __init__(self, radius, name):
        self.radius = radius
        self.diameter = round((radius * 2), 2)
        self.name = name
        self.type = "Circle"

    #Custom __str__ method that shows attributes of the circle
    def __str__(self):
        return f"These are the attributes of your circle:\nName of circle: {self.name}\nRadius of your circle: {self.radius}\nDiameter of your circle: {self.diameter}"

    #Returns name of class instance
    def show_name(self):
        return self.name
    
    #Returns perimeter of class instance
    def calc_perimeter(self):
        perimeter = self.diameter * math.pi
        perimeter = round(perimeter, 2)
        return perimeter
    
    #Returns area of class instance
    def calc_area(self):
        area = (math.pi * self.radius) ** 2
        area = round(area, 2)
        return area

    #Static Method for showing perimeter formula
    @staticmethod
    def show_perimeter_formula():
        return "To get the 'perimeter' of the circle (circumfrence) I multiplied the diameter with pi."
    
    #Static Method for showing perimeter formula
    @staticmethod
    def show_area_formula():
        return "To get the area of the circle I did 2 times pi times the radius."