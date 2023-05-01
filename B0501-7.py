lists = []

while True :
    in_val = input("입력 : ")
    lists.append(in_val)
    
    if in_val == 'ok' :
        break
    
print (lists)

rem = input ("삭제할 자료 입력 : ")

if rem in lists :
    lists.remove (rem)

print (lists)