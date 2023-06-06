# 상위 클래스 = 부모 클래스
# 하위 클래스 (파일 클래스) = 자식 클래스

# 상속 (inheritance) : 기존의 존재하는 상위 클래스로부터 코드와 데이터를 이어받고 자신이 필요한 기능을 추가하는 방법

# 상속은 일반화 관계를 추구함 (관계 : 연관화, 직관화, 일반화)
# 상속은 is - a 관계임
# 예시 : BMW는 자동차이다. (자동차가 부모 클래스, BMW는 자식 클래스)
# 꽃은 식물이다. (식물이 부모 클래스, 꽃은 자식 클래스)

'''
부모클래스 먼저 만들고 자식클래스 만들기

class 자식클래스 (부모클래스) :
    def 매소드1(self~~) :

    def 매소드2(self~~) :
'''

class car :
    def __init__ (self, make, model, color, price) : # 생성자
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        
    def printall (self) :
        return self.make, self.model, self.color, self.price
    

class ecar (car) : # 상속 받아짐. 따라서 make, model, color, price 또한 상속받아짐
    def __init__ (self, battery, make, model, color, price) :
        super().__init__(make, model, color, price) # super(). == 생성자 호출. 상속받을 때 꼭 써야 하는 부분 (키워드)
        self.battery = battery
        
    def setbattery (self, battery) :
        self.battery = battery
        
    def getbattery (self) :
        return self.battery
        
mycar = ecar(0, "sonata", "s", "silver", 10000)

print (mycar.printall()) 
# printall은 부모 클래스에 있는 것인데 자식 클래스으로 상속하였기 때문에 printall을 자식 클래스에서 사용 가능함

mycar.setbattery (1000)
print(mycar.getbattery())

# 원래 부모 클래스와 자식 클래스의 변수가 같을 경우 충돌이 일어나나, 객체의 특성 상 overwriting으로 재정의됨.
