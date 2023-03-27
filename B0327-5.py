import math

rad = float(input("반지름 입력 : "))

rst = 4 / 3 * math.pi * (rad ** 2)

print ("반지름 " + str(rad) + "의 구의 부피는 " + str(rst))

# stdin 오류 생길 때는 입력창에 exit() 쳐서 프로세스 초기화하기