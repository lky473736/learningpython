items = {"레쓰비" : 10,
         "코카콜라" : 7,
         "포카칩" : 4,
         "사발면" : 120,
         "삼다수" : 1024}

print ("현재 재고")
for i in items :
    print (i, items[i])
    
mode = int(input("1은 재고 추가, 2는 검색 기능 : "))

if mode == 1 :
    while True :
        print ("그만 추가하려면 key에 0 입력")
        plus_itemkey = input("재고 key 이름 : ")
        
        if plus_itemkey == '0' :
            break
        
        plus_itemvalue = input("재고 수 : ")
        items[plus_itemkey] = plus_itemvalue
        
elif mode == 2 :
    while True :
        print ("그만 검색하려면 key에 0 입력")
        sear = input("key 입력 : ")
        if sear == '0' :
            break
        
        print (items[sear])