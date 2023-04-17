# 등차수열 n의 합공식 (return으로 표현)

def sum (start, end) :
    sum = 0
    for i in range (start, end + 1) :
        sum = sum + i
    return sum

startingpoint = int(input("starting? : "))
endingpoint = int(input("ending? : "))
val = sum (startingpoint, endingpoint)
print ("summation : ", val)