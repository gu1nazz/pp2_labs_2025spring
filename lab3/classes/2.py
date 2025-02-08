class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2


shape = Shape()
square = Square(10)

print("Shape area:", shape.area())  
print("Square area:", square.area())

length = int(input("Enter the length of the square: "))
square = Square(length)
square.area()
