#Max Holdaway - Geometry Calculator: Rectangle Class / Square Class

class rectangle:
    def __init__(self, length_1, length_2, width_1, width_2, if_square, name):
        if if_square == False:
            self.length_1 = length_1
            self.length_2 = length_2
            self.width_1 = width_1
            self.width_2 = width_2
            self.name = name
        else:
            self.length_1 = length_1
            self.length_2 = length_1
            self.width_1 = length_1
            self.width_2 = length_1
            self.name = name
    
    def __str__(self):
        return f"{self.name}"

    def calc_perimeter(self):
        perimeter = self.length_1 + self.length_2 + self.width_1 + self.width_2
        return perimeter
    
    def calc_area(self):
        area = self.length_1 * self.width_1
        return area
    
class square(rectangle):
    def calc_perimeter(self):
        return super().calc_perimeter()
    
    def calc_area(self):
        return super().calc_area()
    