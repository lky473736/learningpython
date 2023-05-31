# 객체 과제 (파이썬 - 오기욱 교수님)
# 202334734 컴퓨터공학전공 임규연

# 클래스 me를 구현하였으며, 함수는 아래와 같이 구현하였습니다.
# get_old : 나이 먹기
# get_height : 키 커지기
# diet : 다이어트
# blooddonation : 헌혈 시스템 

class me :
    def __init__ (self, old, height, weight, country, blood, bloodvolume) :
        self.old = old
        self.height = height
        self.weight = weight
        self.__country = country
        self.blood = blood 
        self.bloodvolume = bloodvolume
        
    def printall (self) :
        print ("임규연의 정보")
        print ("나이 : ", self.old)
        print ("키 : ", self.height)
        print ("몸무게 : ", self.weight)
        print ("국적 : ", self.__country)
        print ("혈액형 : ", self.blood)
        print ("혈액량 : ", self.bloodvolume)
        
    def get_old (self) :
        self.old = self.old + 1
        print ("나이를 한살 더 먹었습니다. 임규연의 나이는 : ", self.old)
        
    def get_height (self, plus_height) :
        self.height = self.height + plus_height
        print ("키가 커졌습니다. 임규연의 지금 키는 : ", self.height)
        
    def diet (self, minus_weight) :
        self.weight = self.weight - minus_weight
        print ("다이어트에 성공했습니다. 임규연의 지금 체중은 : ", self.weight)
        
    def blooddonation (self) :
        print ("헌혈 시스템에 접속하셨습니다. 임규연의 혈액형은 ", self.blood, "입니다.")
        bloodtype = input ("혈액을 이식시킬 분의 혈액형을 입력해주세요. : ")
        
        match bloodtype : # python 3.10 버젼에 생긴 match-case를 이용해 조건문을 표현
            case 'a' :
                print ("수혈이 불가능합니다.")
                print ("프로그램을 종료합니다.")
                exit()
                
            case 'b' :
                print ("수혈이 가능합니다.")
            
            case 'o' :
                print ("수혈이 불가능합니다.")
                print ("프로그램을 종료합니다.")
                exit()
                
            case 'ab' :
                print ("소량수혈이 가능합니다.")
                
            case _ :
                print ("혈액형이 잘못 입력되었습니다. 프로그램을 종료합니다.")
                exit()

        while True :
            print ("임규연의 현재 혈액량은 ", self.bloodvolume, "입니다.")  
            minus_blood = int(input("어느 용량만큼 수혈하실 건가요? : "))
            
            if minus_blood > self.bloodvolume :
                print ("수혈할 혈액량이 현재 혈액량보다 많습니다. 다시 입력해주세요.")
                
            else :
                break
        
        self.bloodvolume = self.bloodvolume - minus_blood
        print ("헌혈을 완료하였습니다. 임규연의 현재 혈액량은 ", self.bloodvolume, "입니다.")
                    
                
lgy = me (20, 178, 65, 'south korea', 'b', 3000) # lgy라는 객체에 값 입력

while True : 
    print ()
    lgy.printall()
    print ()
    print ("1 : 나이 먹기 / 2 : 키 커지기 / 3 : 다이어트 / 4 : 헌혈 시스템 / 5 : 종료")
    mode = int(input("사용하실 함수의 번호를 입력하십시요. : "))
    
    match mode : 
        case 1 :
            lgy.get_old()
        
        case 2 :
            a = int(input("키를 어느 정도로 키울까요? : "))
            lgy.get_height(a)
            
        case 3 :
            b = int(input("다이어트를 어느 정도로 할까요? : "))
            lgy.diet(b)
            
        case 4 : 
            lgy.blooddonation()
        
        case 5 :
            print ("프로그램을 종료합니다.")
            exit()