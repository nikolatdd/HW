class Shape():
    def calculateSurface(self,width,height):
        self.width = width
        self.height = height
    def calculateCircle(self,r):
        self.r = r
class Triangle(Shape): 
    def calculateSurfaceTriangle(self,width,height):    
        Shape.calculateSurface(self,width,height) 
        return float(width*height)

class Rectangle(Shape):
    def calculateSurfaceRectangle(self,width,height):
        Shape.calculateSurface(self,width,height) 
        return float(height*(width/2))
class Circle(Shape):
    def calculateCircleSurface(self,r):
        Shape.calculateCircle(self,r)
        return (r**2)*3.14 

triangle = Triangle()
print(triangle.calculateSurfaceTriangle(2,4))
rectangle = Rectangle()
print(rectangle.calculateSurfaceRectangle(2,4))
circle = Circle()
print(circle.calculateCircleSurface(4))