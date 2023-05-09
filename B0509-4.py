import math

class circle :
    def __init__ (self, rad = 0) :
        self.rad = rad
        
    def area(self) :
        return math.pi * self.rad * self.rad
    
    def peri(self) :
        return math.pi * 2 * self.rad
    
cir = circle(10)

print (cir.area()) # 면적
print (cir.peri()) # 둘레