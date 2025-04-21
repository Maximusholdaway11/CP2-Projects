# Max Holdaway - Geometry Calculator: Triangle Class

class triangle:
    def __init__(self, base, height, side_1, side_2, side_3, name):
        self.base = base
        self.height = height
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = name
    
    def __str__(self):
        return f"{self.name}"

    def calc_perimeter(self):
        perimeter = self.side_1 + self.side_2 + self.side_3
        return perimeter
    
    def calc_area(self):
        area = self.base * self.height
        return area