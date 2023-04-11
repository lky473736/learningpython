# 등차수열 n에서의 합 공식

sum = 0
f_val = 0
i = 1

n = int(input("number : "))

while i <= n :
    sum = sum + 1
    i = i + 1
    f_val = f_val + sum
    print (f_val)
    
print ("합은 = " + str(f_val))
