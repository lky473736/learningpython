from math import pi
# math 라이브러리에서 Pi를 불러온다.
# or import math

rad = int (input("입력 : "))

area = math.pi * rad * rad
#pi = 3.1415926535...

peri = 2 * math.pi * rad

print ("원의 면적은 " + str(area))
# or print ("원의 면적은", area) 

print ("원의 둘레는 " + str(peri))

# 변수의 이름 : 내용을 알 수 있도록 길게
# 변수의 이름 중간에 공백 x (언더하이픈 사용)
# 변수의 이름 중에서 사용하면 안되는 것
# 6pack, mid score, class, money#
# 예약어는 변수의 이름으로 사용할 수 없다.

