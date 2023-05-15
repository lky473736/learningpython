'''
getters : 게터
setters : 세터
'''

class car :
    def __init__ (self, velocity = 0, color = None, model = None) :
        self.__velocity = velocity # 한정자 (private)
        self.__color = color
        self.__model = model
        
    def printall (self) :
        print (self.__velocity, self.__color, self.__model)
        
    def getvelocity (self) :
        return self.__velocity # getters
    
    def setvelocity (self, v) :
        self.__velocity = v # setters
    
    def drive (self) :
        self.__velocity = 70
        print (self.__velocity)
    
car = car()

# car 안에 변수를 넣지 않으면 arguments를 찾을 수 없다는 오류 발생 -> 따라서 init에서 초기 설정값을 세팅해주면 됨

car.printall()

car.drive()

car.printall()