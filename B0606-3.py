# 매소드 overwriting
# 자식 클래스의 매소드가 부모 클래스의 매소드를 덮어씌움 (재정의)

import math

class shape :
    def __init__ (self) :
        pass
    
    def draw (self) :
        print ("draw가 호출됨")
        
    def getarea (self) :
        print ("getarea가 호출됨")

class circle (shape) :
    def __init__ (self, rad = 0) :
        self.rad = rad
        super().__init__ ()
        
    def draw (self) :
        print ("원을 그립니다")
        
    def getarea (self) :
        return math.pi * self.rad ** 2
    
c = circle (10)
c.draw()
print (c.getarea())