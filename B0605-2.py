# def : 일반함수
# lambda formula : 람다함수

# 1 일반함수로 표현

def celsius (t) :
    return (5.0 / 9.0) * (t - 32.0)

ftemp = [x * 10 for x in range(6)]

ctemp = list(map(celsius, ftemp))

print (ctemp)

# 2 lambda formula로 표현

ftemp = [x * 10 for x in range(6)]
ctemp = []

for i in ftemp :
    ct = lambda x : (5.0 / 9.0) * (x - 32.0) 
    ctemp.append (ct(i)) 

print (ctemp)