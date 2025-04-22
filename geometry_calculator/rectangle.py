#Max Holdaway - Geometry Calculator: Rectangle Class / Square Class

class rectangle:
    def __init__(self, length, width, name):
        self.length = length
        self.width = width
        self.name = name
        self.type = "Rectangle"
    
    def __str__(self):
        return f"These are the attributes of your {self.type}:\nName of {self.type}: {self.name}\nLength of {self.type}: {self.length}\nWidth of {self.type}: {self.width}"

    def show_name(self):
        return self.name

    def calc_perimeter(self):
        perimeter = self.length + self.length + self.width + self.width
        return perimeter
    
    def calc_area(self):
        area = self.length * self.width
        area = round(area, 2)
        return area
    
    @staticmethod
    def show_perimeter_formula():
        return f"The formula I used to get the perimeter of the rectangle is length + length + width + width."

    @staticmethod
    def show_area_formula():
        return f"The formula I used to get the area of the rectangle is length times width."

class square(rectangle):
    def __init__(self, length, name):
        super().__init__(length, length, name)
        self.type = 'Square'

    def calc_perimeter(self):
        return super().calc_perimeter()
    
    def calc_area(self):
        return super().calc_area()
    
    def show_name(self):
        return super().show_name()
    
    @staticmethod
    def show_perimeter_formula():
        return f"The formula I used to get the perimeter of the square is length + length + width + width."

    @staticmethod
    def show_area_formula():
        return "The formula I used to get the area of the square is length times width."