score = int(input("점수 입력: "))
sel = int(input("면접 통과? (1 : pass, 0 : nonpass) : "))

def pandan():
    if score >= 60 and sel == 1 :
       print ("합격")
    else : 
       print ("실패")
    return rst

'''if score >= 90 :
    print ("학점 A")
elif 90 > score >= 80 : 
    print ("학점 B")
elif 80 > score >= 70 :
    print ("학점 C")
elif 70 > score >= 60 :
    print ("학점 D")
elif 60 > score >= 50 :
    print ("학점 F. 노력하세요.")'''
    
rst = pandan()

if score >= 60 and sel == 1 :
    print(rst)
    
else : 
    print(rst)
    
# 다중 if문 = 선택구조
# 기본 제어 구조 : 순차구조, 선택구조, 반복구조

# 반복문
# for문, while문 ...
# 전형적인 반복문 형태
# 1) for i in list
# 2) for i in range(10)
# 3) for i in range(1, 10, 3) : 1부터 시작해서 10까지 3씩 건너뛰어감 (1, 4, 7, 10)
# 4) while 조건 : 조건에는 논리연산자나 관계연산자가 들어간다
# 5) while True : 무한반복

# 연산은 조합이 가능하다. (and와 or 연산으로 가능)
# example) if a > 3 and a < 8
# example) if a != 3 or a == 2