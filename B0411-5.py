in_val = int(input("원하는 n단을 입력하세요 : "))

for i in range (9) : # i = 0 ~ 8 이기 때문에
    print (in_val * (i + 1)) # i + 1를 해주면서 1 ~ 9로 만들어줌
    print ("%s * %s = %s" %(in_val, i + 1, in_val * (i + 1))) # mapping 
    
''' 
while문으로 작성

i = 1

while i < 9 :
   print ("%s * %s = %s" %(in_val * i = in_val * i))
   i = i + 1
'''