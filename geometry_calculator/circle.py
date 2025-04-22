#Max Holdaway - Geometry Calculator: Circle Class
import math

class circle:
    def __init__(self, radius, name):
        self.radius = radius
        self.diameter = round((radius * 2), 2)
        self.name = name
        self.type = "Circle"

    def __str__(self):
        return f"These are the attributes of your circle:\nName of circle: {self.name}\nRadius of your circle: {self.radius}\nDiameter of your circle: {self.diameter}"

    def show_name(self):
        return self.name

    def calc_perimeter(self):
        perimeter = self.diameter * math.pi
        perimeter = round(perimeter, 2)
        return perimeter
    
    def calc_area(self):
        area = (math.pi * self.radius) ** 2
        area = round(area, 2)
        return area