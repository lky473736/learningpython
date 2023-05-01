lists = []
# list = 어떤 타입의 자료라도 저장 가능. 여러 데이터를 박스에 넣는 느낌.
# list 또한 객체임

for i in range (3) :
    in_val = input("리스트에 넣을 값을 넣으시오 : ")
    lists.append(in_val) 
    
print (lists)

'''while True : 
    in_val = input("리스트에 넣을 값을 넣으시오 : ")
    lists.append(in_val)
    
    if in_val == "ok" : # ok 입력하면 while문 탈출하기
        break
    
print (lists)'''

# append : 차례대로 리스트에 자료를 집어넣는다