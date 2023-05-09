# 객체, 클래스, tkinter, 파일

# 객체지향 조건
# 1) class가 만들져야 함
# 2) 상속
# 3) 캡슐화 (encapsulation)
# 4) 정보은닉
# 5) 다용성 (overwriting, overloading)

# SA/SD -> 절차 지향 프로그래밍 : procedure를 기반
# 객체 지향 프로그래밍 : 데이터와 함수를 한 덩어리로 묶어서 생각

# 객체 : attribute(변수형태), action(매소드형태)
# 클래스로부터 만들어지는 객체 : 인스턴스 (instance)

class counter : 
    def __init__(self) : # 생성자
        self.count = 0 # 초기 변수 세팅
        
    def incre(self) : # 매소드
        self.count += 1

a = counter() # a는 객체다 (instance -> class)
a.incre()
print ("객체 a : ", a.count)

b = counter()
b.incre()
print ("객체 b : ", b.count)
