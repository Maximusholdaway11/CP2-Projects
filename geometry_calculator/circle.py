#Max Holdaway - Geometry Calculator: Circle Class
import math

class circle:
    def __init__(self, radius, name):
        self.radius = radius
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def calc_perimeter(self):
        diameter = self.radius * 2
        perimeter = diameter * math.pi
        return perimeter
    
    def calc_area(self):
        area = (math.pi * self.radius) ** 2
        return area