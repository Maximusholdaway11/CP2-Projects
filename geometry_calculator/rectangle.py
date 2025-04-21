#Max Holdaway - Geometry Calculator: Rectangle Class / Square Class

class rectangle:
    def __init__(self, length, width, check_square, name):
        if check_square == False:
            self.length = length
            self.width = width
            self.name = name
            self.type = "Rectangle"
        else:
            self.length = length
            self.width = length
            self.name = name
            self.type = "Square"
    
    def __str__(self):
        return f"These are the attributes of your {self.type}:\nName of {self.type}: {self.name}\nLength of {self.type}: {self.length}\nWidth of {self.type}: {self.width}"

    def show_name(self):
        return f"{self.name}"

    def calc_perimeter(self):
        perimeter = self.length_1 + self.length_2 + self.width_1 + self.width_2
        return perimeter
    
    def calc_area(self):
        area = self.length_1 * self.width_1
        area = round(area, 2)
        return area
    
class square(rectangle):
    def calc_perimeter(self):
        return super().calc_perimeter()
    
    def calc_area(self):
        return super().calc_area()
    