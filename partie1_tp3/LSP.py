# After applying LSP (correct design)
class Shape:
    def get_area(self):
        raise NotImplementedError("Must be implemented by the subclass")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def get_area(self):
        return self.side_length * self.side_length
# Client code that expects a Shape
def print_area(shape):
    print(f"Area: {shape.get_area()}")

if __name__ == '__main__':
# Creating a rectangle and a square
    rect = Rectangle(5,10)
    square = Square(3)
    print_area(rect) 
    print_area(square) 