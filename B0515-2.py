'''
정보 은닉 (public -> private)

1. public : 변수가 사용자에게도 보임 (외부에서 보임)
2. private : interface 안에서만 사용, 사용자에게 변수를 감춤 (외부에서 보이지 않음 + 외부에서 변수 변경 금지)
3. protected : 같은 class의 같은 계열에서만 사용 (권한을 주면 보임 / 허용이 되어진 한도 내에서 공개)
'''

# private (한정자) 사용법 : 앞에 __ 붙이기 (외부에서 변경 금지)

class car :
    def __init__ (self, velocity, color, model) :
        self.__velocity = velocity # 한정자 (private)
        self.__color = color
        self.__model = model
        
    def printall (self) :
        print (self.__velocity, self.__color, self.__model)
        
    def drive (self, a) :
        self.__velocity = a # 매개변수 a를 써서 괄호 안에 수를 입력할 수 있게끔 함
        
    def move (self, p, r, q) :
        pass # 그냥 다음 코드 줄로 넘어가는 매소드
    
car = car(0, "silver", "sonata")

car.printall()
