def printall (k) :
    print (k)
    
def fib(n) :
    sequence = []
    i = 0
    a = 1
    
    while i < n - 1 : # n개의 피보나치 수열이 출력되게끔 n번 반복
       print (a)
       sequence.append (a)
       a = sequence[i-1] + sequence[i]
       i = i + 1
    
    return sequence

def daramji () :
    print ("daramji")
    
def bigdaramji () :
    print ("daramji " * 100)