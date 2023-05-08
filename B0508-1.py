# homework2.py의 모범답안

slist = []
sel = 0

while True :
    print ("slist 현재 상태 : ", slist)
    sel = input("입력 : ")
    
    if sel == '1' :
        nums = input("stack 입력 : ")
        slist.append(nums)
        
    elif sel == '2' :
        if len(slist) == 0 :
            print ("ERROR. slist의 요소가 없어 pop할 수 없습니다.")
        slist.pop()
        print("pop 결과 : ", slist)
        
    else :
        break