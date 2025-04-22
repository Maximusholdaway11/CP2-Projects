# Max Holdaway - Geometry Calculator: Triangle Class

#Triangle Class
class triangle:
    def __init__(self, base, height, side_1, side_2, side_3, name):
        self.base = base
        self.height = height
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = name
        self.type = "Triangle"
    
    #Custom __str__ method that shows attributes of the triangle
    def __str__(self):
        return f"These are the attributes of your triangle:\nName of triangle: {self.name}\nSide one of triangle: {self.side_1}\nSide two of triangle: {self.side_2}\nSide three if triangle: {self.side_3}\nBase of triangle: {self.base}\nHeight of triangle: {self.height}"

    #Returns name of class instance
    def show_name(self):
        return self.name

    #Returns perimeter of class instance
    def calc_perimeter(self):
        perimeter = self.side_1 + self.side_2 + self.side_3
        return perimeter
    
    #Returns area of class instance
    def calc_area(self):
        area = 0.5*(self.base * self.height)
        area = round(area, 2)
        return area

    #Static Method for showing perimeter formula
    @staticmethod
    def show_perimeter_formula():
        return "I added up all three triangle sides to find the perimeter."
    
    #Static Method for showing area formula
    @staticmethod
    def show_area_formula():
        return "I used base times height to find the area."