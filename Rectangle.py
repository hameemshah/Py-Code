class Rectangle:
    length = 0
    breadth = 0
    def __init__(self, l, b): #Assign Method Name
        self.length = l #Assigning `l` argument into field `length`
        self.breadth = b #Assigning `b` argument into field `breathl`
        self.area()
    def area(self):
        area = self.length * self.breadth
        print(f"The area of rectangle is {area}")
        
r1 = Rectangle(10, 20)
r2 = Rectangle(100, 200)
