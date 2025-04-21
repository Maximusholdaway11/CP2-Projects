# Max Holdaway - Geometry Calculator: Triangle Class

class triangle:
    def __init__(self, base, height, side_1, side_2, side_3, name):
        self.base = base
        self.height = height
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = name
        self.type = "Triangle"
    
    def __str__(self):
        return f"These are the attributes of your triangle:\nName of triangle: {self.name}\nSide one of triangle: {self.side_1}\nSide two of triangle: {self.side_2}\nSide three if triangle: {self.side_3}\nBase of triangle: {self.base}\nHeight of triangle: {self.height}"

    def show_name(self):
        return f"{self.name}"

    def calc_perimeter(self):
        perimeter = self.side_1 + self.side_2 + self.side_3
        return perimeter
    
    def calc_area(self):
        area = 0.5*(self.base * self.height)
        area = round(area, 2)
        return area