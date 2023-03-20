import math
PI = 3.141592

rad = int(input("입력 = "))

area = rad * rad * math.pi # 3.141592 * PI 선언
print ("area = " + str(area)) # area를 잠깐 문자열로 취급해서 표현 
# = print ("area = ", area) # area를 수로 취급해서 표현

# 정수 나눗셈 : // (값 중 정수만 출력)
# 실수 나눗셈 : / (값을 전부 표현)
# 할당연산자 : 한번에 여러 개의 변수에 값을 할당할 수 있다.
# example) x, y, z = 3, 4, 5
# example) x, y = y, x (x와 y의 저장되어 있는 값을 교환한다)
