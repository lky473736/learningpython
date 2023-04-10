# 아래는 전부 같은 표현이다.

#1
abc = [1, 2, 3, 4, 5] # 리스트 구조 : 문자건 숫자건 돌릴 수 있음

for i in abc : 
    print ("#1", i)
    
#2
for i in [1, 2, 3, 4, 5] : # 리스트 구조
    print ("#2", i)
    
#3
for i in range (5) : # 5 => 0 ~ 4 (스타트가 0부터 진행)
    print ("#3", i + 1)
    
#4
for i in range (1, 6) :
    print ("#4", i)
    
#5
for i in range (1, 6, 1) : # (start, end (n-1), step)
    print ("#5", i)