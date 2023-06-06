class animal :
    def __init__ (self, age = 0) :
        self.age = age
        
    def eat (self) :
        print ("동물이 밥을 먹습니다.")
        
class dog (animal) : # 자식 클래스는 모든 부모 클래스의 매소드나 변수를 상속받는다
    def __init__ (self, age = 0, name = "") :
        super().__init__ (age = 20)
        self.name = name
        
# 상속 받을 때 만일 자식 클래스와 부모 클래스의 매소드명이 같을 때
# --> 자식 클래스의 매소드가 우선시된다
        
d = dog()
d.eat()
print (d.age)

d.name = "mingky"
print (d.name)

# 다중 상속 : 어떤 class가 여러 개의 클래스에서 상속함
'''
class b1 :
    pass
    
class b2 :
    pass
    
class multiderived (b1, b2) :
    pass
    '''