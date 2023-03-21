# 임규연 (lky473736)

import math # math 라이브러리에서 매소드 및 다양한 기능들을 이용한다

# 참고 : https://pybasall.tistory.com/147

in_val1 = int(input("입력 : "))
in_val2 = int(input("입력 : "))

# 지수계산 # C언어에선 다음과 같이 표기=> power (in_val1, in_val2)
rst = math.pow (in_val1, in_val2)
# 같은 표현 : rst = in_val1 ** in_val2 

print ("Rst = ", rst)
print (math.pi) # 매소드를 사용할 때는 온점을 기준으로 라이브러리의 이름을 표기해준다