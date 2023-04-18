# recursion : 자기 자신을 호출하여 문제를 해결

def fac (n) :
    if n == 1 :
        return 1
    
    else :
        return n * fac (n-1) # n * fac (n-1) = n * n-1 * fac (n-2) * ......
    
n = int(input("정수 입력 : "))
print (fac(n))

