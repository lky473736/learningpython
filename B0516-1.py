import random

class dice :
    def __init__ (self, value = 1, size = 5) : # 주사위 생성
        self.value = value
        self.size = size
        
    def printall (self) :
        print ("value : ", self.value, "/ size : ", self.size)
        
    def printvalue (self) :
        print ("current value : ", self.value)
    
    def roll (self) :
        self.value = random.randint(1, 6)
        print ("roll : ", self.value)
        
        
a = int(input("first value : "))  
b = int(input("first size : "))     
d = dice (a, b)

d.printall()
d.printvalue()
d.roll()
d.printall()