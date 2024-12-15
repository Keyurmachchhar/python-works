class Shape:
    '''Shape Class'''

    x = None
    y = None

    def area(self):
        print("Area of square is :",(self.x*self.y))

    def perimeter(self):
        print("Perimeter of square is :",((2 * self.x) + (2 * self.y)))

obj = Shape()
obj.x = 3
obj.y = 2

print(obj.__doc__)
obj.area()
obj.perimeter()