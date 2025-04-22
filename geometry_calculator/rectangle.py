#Max Holdaway - Geometry Calculator: Rectangle Class / Square Class

#Rectangle class
class rectangle:
    def __init__(self, length, width, name):
        self.length = length
        self.width = width
        self.name = name
        self.type = "Rectangle"
    
    #Custom __str__ method that shows attributes of the rectangle
    def __str__(self):
        return f"These are the attributes of your {self.type}:\nName of {self.type}: {self.name}\nLength of {self.type}: {self.length}\nWidth of {self.type}: {self.width}"

    #Returns name of class instance
    def show_name(self):
        return self.name

    #Returns perimeter of class instance
    def calc_perimeter(self):
        perimeter = self.length + self.length + self.width + self.width
        return perimeter
    
    #Returns area of class instance
    def calc_area(self):
        area = self.length * self.width
        area = round(area, 2)
        return area
    
    #Static Method for showing perimeter formula
    @staticmethod
    def show_perimeter_formula():
        return f"The formula I used to get the perimeter of the rectangle is length + length + width + width."

    #Staatic Method for showing area formula
    @staticmethod
    def show_area_formula():
        return f"The formula I used to get the area of the rectangle is length times width."

#Square class (I'm not about to repeat everything I just said above relating to formulas for practically the same class)
class square(rectangle):
    #Getting __init__ from rectangle but making length and width the same
    def __init__(self, length, name):
        super().__init__(length, length, name)
        self.type = 'Square'

    #Getting calc perimeter from rectangle
    def calc_perimeter(self):
        return super().calc_perimeter()
    
    #Getting calc area from rectangle
    def calc_area(self):
        return super().calc_area()
    
    #Getting show name from rectangle
    def show_name(self):
        return super().show_name()
    
    @staticmethod
    def show_perimeter_formula():
        return f"The formula I used to get the perimeter of the square is length + length + width + width."

    @staticmethod
    def show_area_formula():
        return "The formula I used to get the area of the square is length times width."