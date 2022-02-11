class Rectagle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"{self.x}, {self.y}, {self.width}, {self.height}"

class Right_triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a}, {self.b}"

rectangle = Rectagle(5, 10, 50, 100)
rt = Right_triangle(3, 5)
print(rectangle)
print(rt)






