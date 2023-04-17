def rst(a, b, c) : 
    return a + b + c

def ret() : 
    return p, q # 10과 20을 반환

a = float(input("a 입력 : "))
b = float(input("b 입력 : "))
c = float(input("c 입력 : "))
p = float(input("p 입력 : "))
q = float(input("q 입력 : "))

sum = rst (a, b, c)
r1, r2 = ret() # r1에 p, r2에 q을 차례대로 저장

print (sum)
print (r1)
print (r2)