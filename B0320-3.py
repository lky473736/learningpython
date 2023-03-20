# # : 주석
# """ : 따옴표 세개 안에 있는 것 : 전체 주석

print ("화씨 및 섭씨온도 변환")

# def : 함수 지정 (반환값을 하나만 가질 수 있음) 
# 반환값을 여러가지 가지고 싶다면 포인터를 사용할 수 있음 

def function1 () : 
        ftemp = str(input("화씨온도 : "))
        ftemp = int(ftemp)
        ctemp = (ftemp-32.0)*5.0/9.0
        print ("섭씨온도 :", ctemp)
        
def function2 () :
        ctemp = str(input("섭씨온도 : "))
        ctemp = int(ctemp)
        ftemp = ctemp*1.8 + 32
        print ("화씨온도 :", ftemp)

while True:  # = while True : 무한정 반복하기 (= for i in range(True))
    
    selection = int (input("화씨면 1, 섭씨면 2 : ")) 
    
    if selection == 1 : # 조건문 사용하여 선택지 갈림길 만들기
        function1()

    elif selection == 2 : 
        function2()
    
    else :
        print ("선택번호 잘못됨.")
        break
    
    # 참고 : https://blockdmask.tistory.com/440