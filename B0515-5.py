class monster : 
    normal = 10
    
    def __init__ (self) :
        self.__health = monster.normal
        
    def eat (self) :
        self.__health = monster.normal + 10
        
    def attack (self) :
        self.__health = monster.normal - 10
        
    def state (self) :
        print ("현재 상태 : ", self.__health)
        
monster = monster()

while True :
    monster.state()
    mode = int(input("0은 eat, 1은 attack, 2는 종료 : "))
    
    if mode == 0 :
        monster.eat()
        
    elif mode == 1 :
        monster.attack()
        
    else :
        break