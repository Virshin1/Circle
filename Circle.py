class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
rad=int(input("Enter radius"))
circle=Circle(rad)
print(f"Area= {circle.area()}")
print(f"Perimeter= {circle.perimeter()}")