# lambda formula = 함수의 몸체가 없는 함수
# lf는 딱 한번 사용하는 함수를 만드는 곳에 사용됨 (linux, shell 할 때 자주 쓰임)

# 단항 연산자 : ++a, a-- ...
# 이항 연산자 : x + y ...

# 삼항 연산자 : (x > y) : a: b; => x가 y보다 크면 a, 아니면 b

'''if x > y :
    rst = a
else :
    rst = b'''
    
def ssum (x, y) :
    return x + y

print (ssum(2, 3))

rst = lambda x, y : x + y
print (rst(2, 3))

rst2 = lambda x, y, z : x - y - z
print (rst2(3 ,2, 1))