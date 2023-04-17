# default argument & non-changable argument

def defa_ar (a, b = 10) : # b = default argument. 매개변수이면서 이미 값이 지정된 애
    rst = a + b
    return rst

def cals (x, y, z) : # x, y, z = keyword argument
    return x + y + z

def v_cals(*args) : # non-changable argument. 변수 앞에 * 입력
    sum = 0
    for i in args :
        sum = sum + i
    print (sum)

rst = defa_ar (100) # 매개변수의 갯수에 맞추지 않아도 default argument에 의해서 110이 출력
print(rst)

rst2 = defa_ar (100, 200) # default argument를 실시간으로 200으로 재정의함 -> 300 출력
print (rst2)

rst3 = cals (y = 1, x = 2, z = 3) 
# 매개변수의 순서가 엉망이더라도 재정렬해서 연산해줌 
# (딕셔너리처럼 이름 붙여야함)
print (rst3)

v_cals (300) # 300 나올거임
v_cals (10, 20, 30, 40, 50) # 리스트의 component를 다 더해버림 